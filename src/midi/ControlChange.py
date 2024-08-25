from midi import MessageStatus
from midi.MidiChannelMessage import MidiChannelMessage


class ControlChange(MidiChannelMessage):
    def __init__(self, channel, control, value):
        super().__init__(MessageStatus.ControlChange, channel)
        self.control = control
        self.value = value
    def toBytes(self):
        return [self.statusAndChannel, self.control, self.value]