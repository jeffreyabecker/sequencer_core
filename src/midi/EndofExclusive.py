from midi import MessageStatus
from midi.MidiMessage import MidiMessage


class EndofExclusive(MidiMessage):
    def __init__(self, status):
        super().__init__(MessageStatus.EndOfExclusive)
    def toBytes(self):
        return [self.status]