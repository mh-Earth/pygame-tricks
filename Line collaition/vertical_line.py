import pygame
import time
import math

def distains(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(dist)
    return dist

# ______________________________________________________________________________________________________________________
def vertical_line(boll_position_x,boll_position_y,line_position_x,line_start_y,line_end_y,line_width):
    global boll_X_V

    if distains(boll_position_x,boll_position_y,line_position_x,boll_position_y)<line_width+5 and (boll_position_y>line_start_y and boll_position_y<line_end_y):
        boll_X_V*=-1
# ______________________________________________________________________________________________________________________

if __name__=="__main__":

    display_hight=800
    display_wight=800
    running=True
    # ___________________________
    display=pygame.display.set_mode((display_hight,display_wight))
    pygame.display.set_caption("vertical_line")
    # ___________________________
    boll_position_x=30
    boll_position_y=510
    boll_X_V=10
    boll_Y_V=11
    # ___________________________

    clock=pygame.time.Clock()
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
        pygame.draw.line(display, ((255,255,0)), (400,100), (400,750), 5)

        boll_position_x+=boll_X_V
        boll_position_y+=boll_Y_V
        vertical_line(boll_position_x,boll_position_y,400,100,750,10)
        clock.tick(40)
        pygame.display.update()






