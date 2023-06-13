import sys
import pygame as pg
import math


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True,False)]*8

    kt_img=pg.image.load("ex01-20230613/fig/3.png")
    kt_img=pg.transform.flip(kt_img,True,False)
    kt_img=pg.transform.rotozoom(kt_img,10,1.0)
    #kt2_img=pg.transform.rotozoom(kt_img,10,1.0)
    #slist=[kt_img,kt2_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr*0.8%1600
        for i in range(16):
            screen.blit(bg_imgs[i], [1600*i-x, 0])
        #screen.blit(slist[1*(tmr%100//50)],[300,200])
        screen.blit(pg.transform.rotozoom(kt_img,1.2*math.sin(tmr*0.08),1.0),[300,200])
    

        pg.display.update()
        tmr += 1

        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()