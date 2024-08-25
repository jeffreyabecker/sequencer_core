from midi import MessageStatus
from midi.MidiMessage import MidiMessage


class SongPositionPointer(MidiMessage):
    def __init__(self, beats):
        super().__init__(MessageStatus.SongPositionPointer)
        self.beats =  beats
    def toBytes(self):
        return [self.status, self.beats & 0x7F, (self.beats >> 7) & 0x7F]