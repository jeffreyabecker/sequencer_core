class Track:
    def __init__(self, note):
        self.note = note
        self.beats = [None]*32
    
    def beat(self, beatIndex, output):
        if(beatIndex < self.beats.count and self.beats[beatIndex] != None):
            output.send()