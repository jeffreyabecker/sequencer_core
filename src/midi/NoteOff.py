from midi import MessageStatus
from midi.MidiChannelNoteMessage import MidiChannelNoteMessage


class NoteOff(MidiChannelNoteMessage):
    def __init__(self, channel, note, velocity):
        super().__init__(MessageStatus.NoteOff, channel, note, velocity)