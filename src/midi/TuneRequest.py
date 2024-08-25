from midi import MessageStatus
from midi.MidiMessage import MidiMessage


class TuneRequest(MidiMessage):
    def __init__(self):
        super().__init__(MessageStatus.TODO)
    def toBytes(self):
        return [self.status]