from midi import MessageStatus
from midi.MidiChannelNoteMessage import MidiChannelNoteMessage


class NoteOn(MidiChannelNoteMessage):
    def __init__ (self, channel, note, velocity):
        super().__init__(MessageStatus.NoteOn, channel, note, velocity)