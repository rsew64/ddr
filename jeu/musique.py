import time
http://www.pygame.org/docs/ref/music.html

class Musique:
    def __init__ (self):
        self.playtime = 0
        self.musicduration = 10

    def timecalc (self):
        while self.playtime<self.musicduration:
            self.playtime += 1
            time.sleep(1)
        pass
