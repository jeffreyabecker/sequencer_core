from midi import MessageStatus
from midi.SystemRealtimeMessage import SystemRealtimeMessage


class Start(SystemRealtimeMessage):
    def __init__(self, status):
        super().__init__(MessageStatus.Start)