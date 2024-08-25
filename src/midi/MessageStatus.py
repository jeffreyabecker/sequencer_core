from enum import IntEnum


class MessageStatus(IntEnum):
    # Channel Specific messages
    NoteOff = 0x80
    NoteOn = 0x90
    PolyphonicKeyPressure = 0xA0
    ControlChange = 0xB0 # has special values 120-127
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
