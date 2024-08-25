from midi import MessageStatus
from midi.MidiChannelMessage import MidiChannelMessage


class ChannelPressure(MidiChannelMessage):
    def __init__(self, channel, pressure):
        super().__init__(MessageStatus.ChannelPressure, channel)
        self.pressure = pressure
    def toBytes(self):
        return [self.statusAndChannel, self.pressure]