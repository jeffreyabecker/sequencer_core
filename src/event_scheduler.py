

class EventSchedulerEvent:
    def __init__(self, timestamp, count, interval, callback):
        self._timestamp = timestamp
        self.count = count
        self.interval = interval
        self._callback = callback

    def shouldRun(self, now):
        return self.count != 0 and (now - self._timestamp) % self.interval == 0

    def run(self):
        if (self.count != 0):
            self._callback()
            self.count -= 1
        return self.count == 0


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

    def tick(self, count=1):
        for i in range(count):
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
