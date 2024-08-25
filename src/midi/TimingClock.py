from midi import MessageStatus
from midi.SystemRealtimeMessage import SystemRealtimeMessage


class TimingClock(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.TimingClock)