import os
import pyinotify

DIRECTORY = '/tmp/test'

class EventHandler(pyinotify.ProcessEvent):

    @staticmethod
    def process_IN_CREATE(event):
        print("Creating:", event.pathname)
        if os.path.isfile(event.pathname):
            os.remove(event.pathname)
            print('File removed')

    @staticmethod
    def process_IN_DELETE(event):
        print("Removing:", event.pathname)


wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(DIRECTORY, mask, rec=True)

notifier.loop()
