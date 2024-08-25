from midi import MessageStatus
from midi.MidiChannelNoteMessage import MidiChannelNoteMessage


class PolyphonicKeyPressure(MidiChannelNoteMessage):
    def __init__(self, channel, note, velocity):
        super().__init__(MessageStatus.PolyphonicKeyPressure, channel, note, velocity)