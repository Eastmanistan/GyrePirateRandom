"""To do:
    use formFactor = video1.video_format .height and .width to center video in window by changeing anchor of .blit().

    build larger function to enompass play back and the player.play call.

    import system and use a sys.exit(1) call to end playback

    figure out out to create a loop


"""

import pyglet
import random
import time


filmIndex = {"A1":"A1.mp4", "A2":"A2.mp4","A3":"A3.mp4", "A4":"A4.mp4", "A5":"A5.mp4","A6":"A6.mp4",
             "B1":"B1.mp4", "B2":"B2.mp4","B3":"B3.mp4", "B4":"B4.mp4", "B5":"B5.mp4","B6":"B6.mp4",
             "C1":"C1.mp4", "C2":"C2.mp4","C3":"C3.mp4", "C4":"C4.mp4", "C5":"C5.mp4","C6":"C6.mp4"}

track = ["A", "B","C"]

window = pyglet.window.Window()
window.set_size(1280,720)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()

def orderFilm():  #creates a randomized play order
    slot = ""  # slot is the place holder variable to build builtFilm
    builtFilm = [] #list to hold the order
    for i in range(1,4): #upper end of range is based on how many scenes are in a single playthrough
        slot = track[random.randint(0,2)] + str(i)
        builtFilm.append(slot)
    return builtFilm



def loadVideo(builtFilm):  #queues the files to play
    for i in builtFilm:
        video = pyglet.media.load(filmIndex[i])
        player.queue(video)

def on_key_press(self, symbol, modifiers):

        if symbol == pyglet.window.key.SPACE:
            playPause()

        elif symbol == pyglet.window.key.P:
            self.player.pause()


        elif symbol == pyglet.window.key.ESCAPE:
            player.pause()
            player.close()
            #sys.exit(1)

def playPause():
    if player.playing:
        player.pause()
    else:
        self.player.play()

def do_it():
    builtFilm = orderFilm()
    loadVideo(builtFilm)
    print builtFilm
    player.play()

"""i = 0
t0 = time.clock()

do_it()
while i < 3:
    if (time.clock() - t0) > 40:
        do_it()
        t0= time.clock()
        i += 1
        print i
"""

@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:

        player.get_texture().blit(0,0)

if __name__ == '__main__':

    i = 0
    t0 = time.clock()
    do_it()


    if (time.clock() - t0) > 40:
        do_it()
        t0 = time.clock()
        i += 1
        print i

    pyglet.app.run()