# Print out realtime audio volume as ascii bars
import pygame as pg, sounddevice as sd, numpy as np, os

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print("|" * int(volume_norm))

#with sd.Stream(callback=print_sound):
    #sd.sleep(duration * 1000)

src_folder = 'baby/'
frame_min = 1
frame_low = 65
frame_max = 89
frame_images = [pg.image.load(src_folder+file) for file in os.listdir(src_folder) if file.endswith('.jpg')]

sensitivity = 10

def callback_event(indata, outdata, frames, time, status):
    volume_norm = (np.linalg.norm(indata)*sensitivity) + frame_low
    if volume_norm > frame_max:volume_norm = frame_max
    window.blit(frame_images[int(volume_norm)], (0, 0))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

window = pg.display.set_mode((240, 320), pg.HWSURFACE)

with sd.Stream(callback=callback_event):
    sd.sleep(-1)
