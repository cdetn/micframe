import pygame as pg
import numpy as np
import os

try:
    import sounddevice as sd
except ModuleNotFoundError:
    input('''sounddevice module not installed.
use pip or equivalent to install it.\n
press return to exit''')
    exit()

config = {"folder": "baby/", "sensitivity": 10,
          "width": 240, "height": 320,
          "min": 1, "low": 65, "max": 90,
          "ext": "jpg"}

if os.path.isfile('config.txt'):
    print('loading config.txt')
    with open('config.txt', 'r') as file:
        for line in file.readlines():
            if line.startswith('#'):continue
            d = line.strip().split('=')
            if len(d) > 1:
                key = d[0].lower()
                value = '='.join(d[1:])
                if value.isdigit():value = int(value)
                config[key] = value
                
        file.close()

else:
    print('writing default config.txt')
    with open('config.txt', 'w') as file:
        file.write('''# default config for camera eating baby
# use # at the start to comment out a line''')
        for key in config.keys():
            file.write('\n{}={}'.format(key, config[key]))
        file.close()


frame_images = [
    pg.image.load(config['folder']+file) for file in os.listdir(config['folder'])
    if file.endswith(config['ext'])]

def callback_event(indata, outdata, frames, time, status):
    volume_norm = (np.linalg.norm(indata)*config['sensitivity']) + (config['low']-1)
    if volume_norm >= config['max']:volume_norm = config['max']-1
    window.blit(frame_images[int(volume_norm)], (0, 0))
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

window = pg.display.set_mode((config['width'], config['height']), pg.HWSURFACE)


with sd.Stream(callback=callback_event):
    sd.sleep(-1)
