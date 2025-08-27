import pygame as pg

print('Setup Start')
pg.init()
window = pg.display.set_mode(size=(800, 600))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # Close Window
            quit()  # end pygame
