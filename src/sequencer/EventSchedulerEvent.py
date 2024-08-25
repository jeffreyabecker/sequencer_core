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
