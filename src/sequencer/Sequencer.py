from array import array
from midi.Drums import Drums
from sequencer import EventScheduler, Track


TICKS_PER_MINUTE = 6000
DEFAULT_NOTE_MAPPING = [Drums.]


# TODO Handle Sending https://en.wikipedia.org/wiki/MIDI_beat_clock
class Sequencer:
    def __init__(self, tempo =  120, notes=[]):
        self._beatCounter = 0
        self._tempo = tempo
        self.tracks = [None]*32
        if(notes.count == 0):
            notes = DEFAULT_NOTE_MAPPING
        for i in range(notes.count):
            self.tracks[i] = Track(notes[i])        
        self._eventScheduler = EventScheduler()
        self._beatEvent = self._eventScheduler.setEvent(
            -1, (TICKS_PER_MINUTE / self._tempo), lambda: self._beat())
        

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, value):
        self._tempo = value
        self._beatEvent.interval = (TICKS_PER_MINUTE / self._tempo)

    def _beat(self):
        pass
