import pygame
import time
import math

def distains(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(dist)
    return dist
# ______________________________________________________________________________________________________________________
def horizontal_line(boll_position_y,boll_position_x,line_position_y,line_start_x,line_end_x,line_width,line_position_x=200):
    global boll_Y_V

    if distains(boll_position_y,boll_position_x,line_position_y,boll_position_x)<line_width+5 and (boll_position_x>line_start_x and boll_position_x<line_end_x):
        boll_Y_V*=-1
# ______________________________________________________________________________________________________________________



if __name__=="__main__":

    # ___________________________
    display_hight=800
    display_wight=800
    running=True
    # ___________________________
    display=pygame.display.set_mode((display_hight,display_wight))
    pygame.display.set_caption("horizontal_line")
    # ___________________________
    boll_position_x=30
    boll_position_y=510
    boll_X_V=11
    boll_Y_V=10
    # ___________________________
    clock=pygame.time.Clock()
    # ___________________________
    while running:
        display.fill((0,0,0))
        if boll_position_x>display_wight-5:
            boll_X_V*=-1
        if boll_position_x<5:
            boll_X_V*=-1

        if boll_position_y>display_hight-5:
            boll_Y_V*=-1
        if boll_position_y<5:
            boll_Y_V*=-1

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()

        pygame.draw.circle(display, ((0,255,0)), ((boll_position_x,boll_position_y)), 10)
        pygame.draw.line(display, ((255,255,0)), (200,200), (750,200),5)
        boll_position_x+=boll_X_V
        boll_position_y+=boll_Y_V

        # ______________________________________________________________________________________________________________________
        horizontal_line(boll_position_y,boll_position_x,200,200,750,10)
        # ______________________________________________________________________________________________________________________
        clock.tick(40)
        pygame.display.update()






