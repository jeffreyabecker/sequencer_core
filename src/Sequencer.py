from midi import NoteOff, NoteOn, Drums
from event_scheduler import EventScheduler


class Beat:
    def __init__(self, duration, velocity=63):
        self.velocity = velocity
        self.duration = duration

    def messages(self, note, channel):
        return [
            {'at': 0, 'message': NoteOn(channel, note, self.velocity)},
            {'at': self.duration, 'message': NoteOff(
                channel, note, self.velocity)}
        ]


class Track:
    def __init__(self, note):
        self.note = note
        self.beats = [None]*32

    def beat(self, beatIndex, output):
        if (beatIndex < self.beats.count and self.beats[beatIndex] != None):
            output.send()


DEFAULT_NOTE_MAPPING = [
    Drums.Bass_Drum_1,
    Drums.Electric_Snare,
    Drums.Low_Tom,
    Drums.Low_Conga,
    Drums.Open_Hi_Conga,
    Drums.Claves,
    Drums.Hand_Clap,
    Drums.Maracas,
    Drums.Cowbell,
    Drums.Crash_Cymbal_1,
    Drums.Open_Hi_Hat,
    Drums.Closed_Hi_Hat
]


# TODO Handle Sending https://en.wikipedia.org/wiki/MIDI_beat_clock
class Sequencer:
    def __init__(self, tempo=120, notes=[], ticksPerMinute=6000):
        self._beatCounter = 0
        self._tempo = tempo
        self.tracks = [None]*32
        if (notes.count == 0):
            notes = DEFAULT_NOTE_MAPPING
        for i in range(notes.count):
            self.tracks[i] = Track(notes[i])
        self._eventScheduler = EventScheduler()
        self._ticksPerMinute = ticksPerMinute
        self._beatEvent = self._eventScheduler.setEvent(
            -1, (ticksPerMinute / self._tempo), lambda: self._beat())

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, value):
        self._tempo = value
        self._beatEvent.interval = (self._ticksPerMinute / self._tempo)

    def _beat(self):
        pass

    def tick(self, count=1):
        self._eventScheduler.tick(count)
