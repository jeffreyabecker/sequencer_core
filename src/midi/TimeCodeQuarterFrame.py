from midi import MessageStatus
from midi.MidiMessage import MidiMessage


class TimeCodeQuarterFrame(MidiMessage):
    def __init__(self, messageType, values):
        super().__init__(MessageStatus.TimeCodeQuarterFrame)
        self.messageType = messageType
        self.values = values
    def toBytes(self):
        return [self.status, ((self.messageType << 4) & 0x70) | (self.values & 0x0F)]