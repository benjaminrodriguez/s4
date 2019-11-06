import pyinotify
# http://github.com/seb-m/pyinotify/wiki/Tutorial


class EventHandler(pyinotify.ProcessEvent):
    @staticmethod
    def process_IN_CREATE(event):
        print("Creating:", event.pathname)

    @staticmethod
    def process_IN_DELETE(event):
        print("Removing:", event.pathname)


wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/tmp', mask, rec=True)

notifier.loop()
