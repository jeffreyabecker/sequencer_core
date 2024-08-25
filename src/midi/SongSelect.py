from midi import MessageStatus
from midi.MidiMessage import MidiMessage


class SongSelect(MidiMessage):
    def __init__(self, songNumber):
        super().__init__(MessageStatus.SongSelect)
        self.songNumber= songNumber
    def toBytes(self):
        return [self.status, self.songNumber]