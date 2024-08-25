from midi import MessageStatus
from midi.SystemRealtimeMessage import SystemRealtimeMessage


class Continue(SystemRealtimeMessage):
    def __init__(self):
        super().__init__(MessageStatus.Continue)