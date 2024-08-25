from midi import MessageStatus
from midi.MidiChannelMessage import MidiChannelMessage


class ProgramChange(MidiChannelMessage):
    def __init__(self, channel, programNumber):
        super().__init__(MessageStatus.ProgramChange, channel)
        self.programNumber =  programNumber

    def toBytes(self):
        return [self.statusAndChannel, self.programNumber]