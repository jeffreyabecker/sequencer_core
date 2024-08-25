from midi.MidiChannelMessage import MidiChannelMessage


class MidiChannelNoteMessage(MidiChannelMessage):
    def __init__(self, status, channel, note, velocity):
        super().__init(status, channel)
        self.note = note
        self.velocity = velocity
    def toBytes(self):
        return [self.statusAndChannel, self.note.value, self.velocity]