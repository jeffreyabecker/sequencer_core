from midi.MidiMessage import MidiMessage


class SystemRealtimeMessage(MidiMessage):
    def __init__(self, status):
        super().__init__(status)
    def toBytes(self):
        return [self.status]