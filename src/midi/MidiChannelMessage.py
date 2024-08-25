from midi.MidiMessage import MidiMessage


class MidiChannelMessage(MidiMessage):
    def __init__(self, status, channel):
        super().__init__(status)
        self.channel = channel
        self.statusAndChannel = (self.status & 0xF0) | (self.channel & 0x0F)