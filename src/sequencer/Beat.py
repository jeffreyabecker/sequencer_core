from midi import NoteOn, NoteOff


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
