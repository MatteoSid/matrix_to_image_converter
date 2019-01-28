from skimage.io import imsave
import os
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from pathlib import Path

os.system('clear')

def converter(path, file_name, extension, log = 'OFF'):
    # innerarray contiene le stringhe corrispondenti alle righe della matrice
    innerarray=[]

    # array è un array di array che contiene tutte le righe
    array=[]

    #altezza e larghezza della matrice trasformata
    w=0
    h=0

    file_ = Path(path + file_name + extension)

    if file_.is_file():
        with open(path + file_name + extension , "r") as fileobj:
            for line in fileobj:  
                w=0
                for ch in line:
                    if ch!='\n': # escludo i caratteri di andata a capo
                        innerarray.append(int(ch))
                        w=w+1
                h=h+1
                array.append(innerarray)
                innerarray=[]
        if log == 'ON':
            print('\nImmagine salvata alla posizione: ' + path + file_name + '.png')
            print('L\'immagine ha dimensione [h,w] = [' + str(h) + ', ' + str(w) + '].\n')

        array=np.asarray(array)

        fig = plt.figure(frameon=False, figsize=(w,h))

        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        plt.style.use('grayscale')

        ax.imshow(array, aspect='auto')

        fig.savefig(path + file_name + '.png' ,dpi=1)
    else:
        print('\nNessun file trovato al percorso: ' + path + '\n')
