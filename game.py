#CHRISTIAN JENSEN & Robert Pallante
from __future__ import print_function
import pygame, sys, random, time
from pygame.locals import *
#=================================
pygame.font.init
pygame.init()
pygame.event.set_blocked(VIDEORESIZE)   #Non-resizable window
window = pygame.display.set_mode((550, 600))   #Window size
pygame.display.set_caption('2048')
#=========Gobal Varis==============
score = 0
finalscore = 0
numnames = [0,2,4,8,16,32,64,128,256,512,1024,2048]
numblocks = []
bg = pygame.Surface(window.get_size())
bg.fill((138,138,138))
#==============music===============
#pygame.mixer.music.load('theme.ogg')
#pygame.mixer.music.play()
#==============Functions============
#Score write system/not working yet 
def scoring():
    with open ("score.txt", "a") as es: #opens score keeping
        
        print ("==================")
        print ("==================")
        n4s = raw_input("Whats your name?: ")
        print(score,n4s,  file = es) #prints score to file
#======================== MENU ========================
def menu():
    while True:
        scoretextfont=pygame.font.Font(None,36)
        losetextfont=pygame.font.Font(None,72)
        pygame.mouse.set_visible(True)
        window.fill((204,204,204))
        losetextfont.set_underline(True)
        losetextfont.set_bold(True)
        title=losetextfont.render('2048 py edition',1,(255,255,0))
        titlepos = title.get_rect(center=(278,200))
        window.blit(title,titlepos)
        losetextfont.set_underline(False)
        losetextfont.set_bold(False)
        playbutton=losetextfont.render('PLAY',1,(0,0,0),(0,102,153))
        playbuttonpos=playbutton.get_rect(center=(278,350))
        window.blit(playbutton,playbuttonpos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if playbuttonpos.collidepoint(event.pos):
                    return None
#======================== main program===================
menu()
window = pygame.display.set_mode((185,185)) #resizes the window for gameplay to look good 
#start of game
for x in numnames: ##Appends image locations
    numname = "data/images/%i.jpg"%x
    numblocks.append(numname)

block_images = []
for x in numblocks: ##Appends images
    blockimg = pygame.image.load(x).convert()
    block_images.append(blockimg)

allimages = []
###################
axislocs = [[[5,5],[50,5],[95,5],[140,5]],
            [[5,50],[50,50],[95,50],[140,50]],
            [[5,95],[50,95],[95,95],[140,95]],
            [[5,140],[50,140],[95,140],[140,140]]]

flaggrid = [[0,0,0,0], ##This list is used to determine if a point in the grid is inhabited.
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

def igrid(aimgs, als, imgs):  ##Appends image with a location
    row = 0
    column = 0
    img_row = []
    for x in range(16):
        img = imgs[0]
        loc = als[row][column]
        img_row.append([img,loc])
        column+=1
        if column == 4:
            aimgs.append(img_row)
            img_row = []
            row+=1
            column = 0
    return aimgs

def initial(aimgs):  ##Blits the images to screen
    for x in range (16):
        for r in range(4):
            for c in range(4):
                point = aimgs[r][c]
                window.blit(*point) #Unpacks the list

def firstblocks(aimgs,b_i,fg):
    flag = 0
    b_flag = 0 ##Will be used to prevent generation of two 4 blocks
    while flag < 2:
        rr = random.randint(0,3)
        rc = random.randint(0,3)
        randnum = random.randint(1,10)
        if fg[rr][rc] == 0:
            if randnum < 10: ##Gives a 10% chance of a 4 generating
                print (aimgs[rr][rc])
                aimgs[rr][rc][0] = b_i[1]
            elif b_flag == 1:  ##Prevents two fours from generating initially
                print (aimgs[rr][rc])
                aimgs[rr][rc][0] = b_i[1]
            else:
                print (aimgs[rr][rc])
                aimgs[rr][rc][0] = b_i[2]
                b_flag+=1
            fg[rr][rc]+=1
            flag+=1
    initial(aimgs)
    return fg
####################
def keystrokes(aimgs,fg,als,move,b_i):
    if move == "down":
        rr = 0
        rc = 0
        for x in xrange(0,16):
            if (fg[rr][rc] == 1):
                fg[rr][rc] = 0
                fg[3][rc] = 1
                temp_img = aimgs[rr][rc][0]
                aimgs[rr][rc][0] = b_i[0]
                if aimgs[3][rc][0] == temp_img:
                    aimgs[3][rc][0] = b_i[2]
                else:
                    aimgs[3][rc][0] = temp_img
            rc+=1
            if rc == 4:
                rc = 0
                rr+=1
    if move == "up":
        rr = 0
        rc = 0
        for x in xrange(0,16):
            if (fg[rr][rc] == 1):
                fg[rr][rc] = 0
                fg[0][rc] = 1
                temp_img = aimgs[rr][rc][0]
                aimgs[rr][rc][0] = b_i[0]
                aimgs[0][rc][0] = temp_img
            rc+=1
            if rc == 4:
                rc = 0
                rr+=1
    if move == "right":
        rr = 0
        rc = 0
        for x in xrange(0,16):
            if (fg[rr][rc] == 1):
                fg[rr][rc] = 0
                fg[rr][3] = 1
                temp_img = aimgs[rr][rc][0]
                aimgs[rr][rc][0] = b_i[0]
                aimgs[rr][3][0] = temp_img
            rc+=1
            if rc == 4:
                rc = 0
                rr+=1
    if move == "left":
        rr = 0
        rc = 0
        for x in xrange(0,16):
            if (fg[rr][rc] == 1):
                fg[rr][rc] = 0
                fg[rr][0] = 1
                temp_img = aimgs[rr][rc][0]
                aimgs[rr][rc][0] = b_i[0]
                aimgs[rr][0][0] = temp_img
            rc+=1
            if rc == 4:
                rc = 0
                rr+=1
    return (aimgs,fg)
            
##    elif move == "up":
##        print ("move up")
##        
##    elif move == "right":
##        print ("move right")
##        
##    elif move == "left":
##        print ("move left")
####################
window.blit(bg, (0,0))

allimages=igrid(allimages,axislocs,block_images)

initial(allimages)
firstblocks(allimages,block_images,flaggrid)

pygame.display.update()
print (flaggrid)
##################
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if (event.key == K_DOWN):
                move = "down"
                keystrokes(allimages,flaggrid,axislocs,move,block_images)
                initial(allimages)
                print (flaggrid)
            if (event.key == K_UP):
                move = "up"
                keystrokes(allimages,flaggrid,axislocs,move,block_images)
                initial(allimages)
                print (flaggrid)
            if (event.key == K_RIGHT):
                move = "right"
                keystrokes(allimages,flaggrid,axislocs,move,block_images)
                initial(allimages)
                print (flaggrid)
            if (event.key == K_LEFT):
                move = "left"
                keystrokes(allimages,flaggrid,axislocs,move,block_images)
                initial(allimages)
                print (flaggrid)
    pygame.display.update()
