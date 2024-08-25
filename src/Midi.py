
# Statuses
from enum import IntEnum


class MessageStatus(IntEnum):
    # Channel Specific messages
    NoteOff = 0x80
    NoteOn = 0x90
    PolyphonicKeyPressure = 0xA0
    ControlChange = 0xB0  # has special values 120-127
    ProgramChange = 0xc0
    ChannelPressure = 0xd0
    PitchBendChange = 0xe0
    # System Common Messages
    SystemExclusive = 0xf0
    TimeCodeQuarterFrame = 0xf1
    SongPositionPointer = 0xf2
    SongSelect = 0xf3
    TuneRequest = 0xf6
    EndofExclusive = 0xf7
    # System Realtime messages
    TimingClock = 0xf8
    Start = 0xfa
    Continue = 0xfb
    Stop = 0xfc
    ActiveSensing = 0xfe
    Reset = 0xff

# Base Classes


class MidiMessage():
    def __init__(self, status):
        self.status = status

    def toBytes(self):
        raise NotImplementedError()


class MidiChannelMessage(MidiMessage):
    def __init__(self, status, channel):
        super().__init__(status)
        self.channel = channel
        self.statusAndChannel = (self.status & 0xF0) | (self.channel & 0x0F)


class MidiChannelNoteMessage(MidiChannelMessage):
    def __init__(self, status, channel, note, velocity):
        super().__init(status, channel)
        self.note = note
        self.velocity = velocity

    def toBytes(self):
        return [self.statusAndChannel, self.note.value, self.velocity]


class SystemRealtimeMessage(MidiMessage):
    def __init__(self, status):
        super().__init__(status)

    def toBytes(self):
        return [self.status]

# Channel Specific messages


class NoteOff(MidiChannelNoteMessage):
    def __init__(self, channel, note, velocity):
        super().__init__(MessageStatus.NoteOff, channel, note, velocity)


class NoteOn(MidiChannelNoteMessage):
    def __init__(self, channel, note, velocity):
        super().__init__(MessageStatus.NoteOn, channel, note, velocity)


class PolyphonicKeyPressure(MidiChannelNoteMessage):
    def __init__(self, channel, note, velocity):
        super().__init__(MessageStatus.PolyphonicKeyPressure, channel, note, velocity)


class ControlChange(MidiChannelMessage):
    def __init__(self, channel, control, value):
        super().__init__(MessageStatus.ControlChange, channel)
        self.control = control
        self.value = value

    def toBytes(self):
        return [self.statusAndChannel, self.control, self.value]


class ProgramChange(MidiChannelMessage):
    def __init__(self, channel, programNumber):
        super().__init__(MessageStatus.ProgramChange, channel)
        self.programNumber = programNumber

    def toBytes(self):
        return [self.statusAndChannel, self.programNumber]


class ChannelPressure(MidiChannelMessage):
    def __init__(self, channel, pressure):
        super().__init__(MessageStatus.ChannelPressure, channel)
        self.pressure = pressure

    def toBytes(self):
        return [self.statusAndChannel, self.pressure]


class PitchBendChange(MidiChannelMessage):
    def __init__(self, channel, value):
        super().__init__(MessageStatus.PitchBendChange, channel)
        self.value = value

    def toBytes(self):
        return [self.statusAndChannel, ((self.value + 0x2000)) & 0x7F, (((self.value + 0x2000) >> 7)) & 0x7F]

# System Common Messages

# SystemExclusive doesnt exist


class TimeCodeQuarterFrame(MidiMessage):
    def __init__(self, messageType, values):
        super().__init__(MessageStatus.TimeCodeQuarterFrame)
        self.messageType = messageType
        self.values = values

    def toBytes(self):
        return [self.status, ((self.messageType << 4) & 0x70) | (self.values & 0x0F)]


class SongPositionPointer(MidiMessage):
    def __init__(self, beats):
        super().__init__(MessageStatus.SongPositionPointer)
        self.beats = beats

    def toBytes(self):
        return [self.status, self.beats & 0x7F, (self.beats >> 7) & 0x7F]


class SongSelect(MidiMessage):
    def __init__(self, songNumber):
        super().__init__(MessageStatus.SongSelect)
        self.songNumber = songNumber

    def toBytes(self):
        return [self.status, self.songNumber]


class TuneRequest(MidiMessage):
    def __init__(self):
        super().__init__(MessageStatus.TODO)

    def toBytes(self):
        return [self.status]


class EndofExclusive(MidiMessage):
    def __init__(self, status):
        super().__init__(MessageStatus.EndOfExclusive)

    def toBytes(self):
        return [self.status]

# System Realtime messages


class TimingClock(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.TimingClock)


class Start(SystemRealtimeMessage):
    def __init__(self, status):
        super().__init__(MessageStatus.Start)


class Continue(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.Continue)


class Stop(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.Stop)


class ActiveSensing(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.ActiveSensing)


class Reset(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.Reset)


__NOTE_VALUES_HZ = [
    8.1758, 8.662, 9.177, 9.7227, 10.3009, 10.9134, 11.5623, 12.2499, 12.9783, 13.75, 14.5676, 15.4339,
    16.3516, 17.3239, 18.354, 19.4454, 20.6017, 21.8268, 23.1247, 24.4997, 25.9565, 27.5, 29.1352, 30.8677,
    32.7032, 34.6478, 36.7081, 38.8909, 41.2034, 43.6535, 46.2493, 48.9994, 51.9131, 55, 58.2705, 61.7354,
    65.4064, 69.2957, 73.4162, 77.7817, 82.4069, 87.3071, 92.4986, 97.9989, 103.8262, 110, 116.5409, 123.4708,
    130.8128, 138.5913, 146.8324, 155.5635, 164.8138, 174.6141, 184.9972, 195.9977, 207.6523, 220, 233.0819, 246.9417,
    261.6256, 277.1826, 293.6648, 311.127, 329.6276, 349.2282, 369.9944, 391.9954, 415.3047, 440, 466.1638, 493.8833,
    523.2511, 554.3653, 587.3295, 622.254, 659.2551, 698.4565, 739.9888, 783.9909, 830.6094, 880, 932.3275, 987.7666,
    1046.5023, 1108.7305, 1174.6591, 1244.5079, 1318.5102, 1396.9129, 1479.9777, 1567.9817, 1661.2188, 1760, 1864.655, 1975.5332,
    2093.0045, 2217.461, 2349.3181, 2489.0159, 2637.0205, 2793.8259, 2959.9554, 3135.9635, 3322.4376, 3520, 3729.3101, 3951.0664,
    4186.009, 4434.9221, 4698.6363, 4978.0317, 5274.0409, 5587.6517, 5919.9108, 6271.927, 6644.8752, 7040, 7458.6202, 7902.1328,
    8372.0181, 8869.8442, 9397.2726, 9956.0635, 10548.0818, 11175.3034, 11839.8215, 12543.854

]


class Note():
    def __init__(self, value):
        self.value = value & 0x7F

    def frequency(self):
        return __NOTE_VALUES_HZ[self.value]

    @classmethod
    def __offset(cls, octave):
        return (12 * ((octave & 0x7F) - 1))

    @classmethod
    def G(cls, octave):
        return Note(31 + cls.__offset(octave))

    @classmethod
    def FSharp(cls, octave):
        return Note(30 + cls.__offset(octave))

    @classmethod
    def Gb(cls, octave):
        return Note(30 + cls.__offset(octave))

    @classmethod
    def F(cls, octave):
        return Note(29 + cls.__offset(octave))

    @classmethod
    def E(cls, octave):
        return Note(28 + cls.__offset(octave))

    @classmethod
    def DSharp(cls, octave):
        return Note(27 + cls.__offset(octave))

    @classmethod
    def Eb(cls, octave):
        return Note(27 + cls.__offset(octave))

    @classmethod
    def D(cls, octave):
        return Note(26 + cls.__offset(octave))

    @classmethod
    def CSharp(cls, octave):
        return Note(25 + cls.__offset(octave))

    @classmethod
    def Db(cls, octave):
        return Note(25 + cls.__offset(octave))

    @classmethod
    def C(cls, octave):
        return Note(24 + cls.__offset(octave))

    @classmethod
    def B(cls, octave):
        return Note(35 + cls.__offset(octave))

    @classmethod
    def ASharp(cls, octave):
        return Note(34 + cls.__offset(octave))

    @classmethod
    def Bb(cls, octave):
        return Note(34 + cls.__offset(octave))

    @classmethod
    def A(cls, octave):
        return Note(33 + cls.__offset(octave))

    @classmethod
    def GSharp(cls, octave):
        return Note(32 + cls.__offset(octave))

    @classmethod
    def Ab(cls, octave):
        return Note(32 + cls.__offset(octave))


class Drums:
    Acoustic_Bass_Drum = Note(35)
    Ride_Cymbal_2 = Note(59)
    Bass_Drum_1 = Note(36)
    Hi_Bongo = Note(60)
    Side_Stick = Note(37)
    Low_Bongo = Note(61)
    Acoustic_Snare = Note(38)
    Mute_Hi_Conga = Note(62)
    Hand_Clap = Note(39)
    Open_Hi_Conga = Note(63)
    Electric_Snare = Note(40)
    Low_Conga = Note(64)
    Low_Floor_Tom = Note(41)
    High_Timbale = Note(65)
    Closed_Hi_Hat = Note(42)
    Low_Timbale = Note(66)
    High_Floor_Tom = Note(43)
    High_Agogo = Note(67)
    Pedal_Hi_Hat = Note(44)
    Low_Agogo = Note(68)
    Low_Tom = Note(45)
    Cabasa = Note(69)
    Open_Hi_Hat = Note(46)
    Maracas = Note(70)
    Low_Mid_Tom = Note(47)
    Short_Whistle = Note(71)
    Hi_Mid_Tom = Note(48)
    Long_Whistle = Note(72)
    Crash_Cymbal_1 = Note(49)
    Short_Guiro = Note(73)
    High_Tom = Note(50)
    Long_Guiro = Note(74)
    Ride_Cymbal_1 = Note(51)
    Claves = Note(75)
    Chinese_Cymbal = Note(52)
    Hi_Wood_Block = Note(76)
    Ride_Bell = Note(53)
    Low_Wood_Block = Note(77)
    Tambourine = Note(54)
    Mute_Cuica = Note(78)
    Splash_Cymbal = Note(55)
    Open_Cuica = Note(79)
    Cowbell = Note(56)
    Mute_Triangle = Note(80)
    Crash_Cymbal_2 = Note(57)
    Open_Triangle = Note(81)
    Vibraslap = Note(58)
