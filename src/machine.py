from sequencer import Sequencer
class Machine:
    def __init__(self):
        self.sequencer = Sequencer
        self.trackIndex = 0
        
        
    def tick(self, count = 1):
        self.sequencer.tick(count)