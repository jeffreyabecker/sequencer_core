from sequencer.EventScheduler import EventSchedulerEvent


class EventScheduler:
    def __init__(self):
        self._events = []
        self.tickCounter = 0
        self.running = False

    def setEvent(self, count, interval, callback):
        event = EventSchedulerEvent(
            self.tickCounter, count, interval, callback)
        self._events.append(event)
        return event

    def clearEvent(self, event):
        self._events.remove(event)

    def tick(self):
        if (self.running):
            self.tickCounter += 1

            toRun = []
            for e in self._events:
                if (e.shouldRun(self.tickCounter)):
                    toRun.append(e)

            for e in toRun:
                shouldRemove = e.run()
                if (shouldRemove):
                    self._events.remove(e)
