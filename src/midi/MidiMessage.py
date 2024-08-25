
class MidiMessage():
    def __init__(self, status):
        self.status = status

    def toBytes(self):
        raise NotImplementedError()
