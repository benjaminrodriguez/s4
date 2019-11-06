import os
import queue
import pyinotify

DIRECTORY = '/tmp/test'

class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, *args, **kwargs):
        self.queue = queue.Queue()
        super().__init__(*args, **kwargs)

    def process_IN_CREATE(self, event):
        file_path = event.pathname
        if os.path.isdir(file_path):
            # On s'occupe des fichiers uniquements
            return
        # Création d'un fichier
        try:
            deleted = self.queue.get_nowait()
        except queue.Empty:
            deleted = ""

        if deleted == file_path:
            print('We re-created this file !')
        else:
            os.remove(file_path)
            self.queue.put(file_path)
            print('{}: you cannot create me !'.format(file_path))

    def process_IN_DELETE(self, event):
        file_path = event.pathname
        if os.path.isdir(file_path):
            # On s'occupe des fichiers uniquements
            return
        # Suppression d'un fichier
        try:
            created = self.queue.get_nowait()
        except queue.Empty:
            created = ""

        if created == file_path:
            print('We deleted this file !')
        else:
            with open(file_path, 'w') as fd:
                fd.write('I\'m still here!\n')
            self.queue.put(file_path)
            print('{}: you cannot delete me !'.format(file_path))


wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(DIRECTORY, mask, rec=True)

notifier.loop()
