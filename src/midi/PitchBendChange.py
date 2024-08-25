from midi import MessageStatus
from midi.MidiChannelMessage import MidiChannelMessage


class PitchBendChange(MidiChannelMessage):
    def __init__(self, channel, value):
        super().__init__(MessageStatus.PitchBendChange, channel)
        self.value =  value

    def toBytes(self):
        return [self.statusAndChannel, ((self.value + 0x2000))&0x7F, (((self.value + 0x2000) >> 7))&0x7F]