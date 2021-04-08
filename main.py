import core
from jeu.fleche import Fleches
from jeu.musique import Musique

fleches = Fleches()
musique = Musique()
vitesse = 1

def setup ():
    print("Setup START---------")
    core.fps = 10
    core.WINDOW_SIZE = [500, 500]

def run ():

    while musique.timecalc():
        fleches.afficher(core)
        while fleches.position.y < core.WINDOW_SIZE[1]:
            fleches.position.y += vitesse
            print(fleches.position)
        print(musique.playtime)

if __name__ == '__main__':
    core.main(setup, run)

