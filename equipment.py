import pygame, sys
from pygame.locals import *
from misc import miscMethods

#Set dimensions of the screen


mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
font = pygame.font.Font(None, 48)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (125,125,125)
equipmentSize = 176
equipmentSpace = 206
check = pygame.image.load('check.png')

def initializeGear():
    equiped = {}
    equipmentList = {}
    equipmentImages = {}

    #Create equipment displays using above specs
    equipmentList['helmet1'] = pygame.Rect(50,50,equipmentSize, equipmentSize)
    equipmentImages['helmet1'] = pygame.image.load('pimp.png')
    equiped['helmet1'] = False

    equipmentList['helmet2'] = pygame.Rect(equipmentSpace + 50,50,equipmentSize, equipmentSize)
    equipmentImages['helmet2'] = pygame.image.load('archer.png')
    equiped['helmet2'] = False

    equipmentList['helmet3'] = pygame.Rect(2*equipmentSpace + 50,50,equipmentSize, equipmentSize)
    equipmentImages['helmet3'] = pygame.image.load('bucket.png')
    equiped['helmet3'] = False

    equipmentList['jacket1'] = pygame.Rect(50,equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['jacket1'] = False

    equipmentList['jacket2'] = pygame.Rect(equipmentSpace + 50,equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['jacket2'] = False

    equipmentList['jacket3'] = pygame.Rect(2*equipmentSpace + 50,equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['jacket3'] = False

    equipmentList['belt1'] = pygame.Rect(50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['belt1'] = False

    equipmentList['belt2'] = pygame.Rect(equipmentSpace + 50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['belt2'] = False

    equipmentList['belt3'] = pygame.Rect(2*equipmentSpace + 50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['belt3'] = False

    equipmentList['pants1'] = pygame.Rect(50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['pants1'] = False

    equipmentList['pants2'] = pygame.Rect(equipmentSpace + 50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['pants2'] = False

    equipmentList['pants3'] = pygame.Rect(2*equipmentSpace + 50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['pants3'] = False

    equipmentList['boots1'] = pygame.Rect(50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['boots1'] = False

    equipmentList['boots2'] = pygame.Rect(equipmentSpace + 50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['boots2'] = False

    equipmentList['boots3'] = pygame.Rect(2*equipmentSpace + 50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['boots3'] = False

    equipmentList['goggles1'] = pygame.Rect((WIDTH - equipmentSpace-15),50,equipmentSize, equipmentSize)
    equiped['goggles1'] = False

    equipmentList['goggles2'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),50,equipmentSize, equipmentSize)
    equiped['goggles2'] = False

    equipmentList['goggles3'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),50,equipmentSize, equipmentSize)
    equiped['goggles3'] = False

    equipmentList['wrist1'] = pygame.Rect((WIDTH - equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['wrist1'] = False

    equipmentList['wrist2'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['wrist2'] = False

    equipmentList['wrist3'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['wrist3'] = False

    equipmentList['gloves1'] = pygame.Rect((WIDTH - equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['gloves1'] = False

    equipmentList['gloves2'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['gloves2'] = False

    equipmentList['gloves3'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['gloves3'] = False

    equipmentList['bandolier1'] = pygame.Rect((WIDTH - equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['bandolier1'] = False

    equipmentList['bandolier2'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['bandolier2'] = False

    equipmentList['bandolier3'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['bandolier3'] = False

    equipmentList['weapon1'] = pygame.Rect((WIDTH - equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['weapon1'] = False

    equipmentList['weapon2'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['weapon2'] = False

    equipmentList['weapon3'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equiped['weapon3'] = False

    return equiped, equipmentList, equipmentImages

def drawEquipment(equipmentList):

    for item in equipmentList:
        pygame.draw.rect(screen, WHITE, equipmentList[item])

    for item in equipmentList:
        x = equipmentList[item].left
        y = equipmentList[item].top + 5
        miscMethods.draw_text(item, font, BLACK, screen, x,y)

def equipGear(equipmentList, gearEquip, click):
    mx, my = pygame.mouse.get_pos()
    item1 = ""
    item2 = ""
    temp = ""
    for item in equipmentList:
        if equipmentList[item].collidepoint((mx,my)) and click:
            equiped[item] = True
            temp = item
            if '1' in temp:
                item1 = temp.replace('1', '2')
                item2 = temp.replace('1', '3')
            if '2' in temp:
                item1 = temp.replace('2', '1')
                item2 = temp.replace('2', '3')
            if '3' in temp:
                item1 = temp.replace('3', '1')
                item2 = temp.replace('3', '2')

            equiped[item1] = False
            #print(equipmentList[item1])
            equiped[item2] = False

    for item in equiped:
        if equiped[item]:
            screen.blit(check, (equipmentList[item].left, equipmentList[item].top))

    return gearEquip

def equipment(equiped, equipmentList, equipmentImages):

    while(True):
        screen.fill(GREY)
        #draw_text('Main Menu', font, WHITE, screen, 20, 20)
        #Get my mouse position
        mx, my = pygame.mouse.get_pos()
        #Rect(X ALighn, Y Align, Width, Height)
        #Create paper doll with above specs

        character = pygame.Rect(668, 50, 584, equipmentSpace*5-30)




        #Button does stuff when clicked

        #draw buttons
        drawEquipment(equipmentList)

        pygame.draw.rect(screen, WHITE, character)
        #test = pygame.image.load('symbol.png')

        for item in equipmentImages:
            screen.blit(equipmentImages[item], (equipmentList[item].left, equipmentList[item].top+20))




        click = False
        #check for button event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        equiped = equipGear(equipmentList, equiped, click)

        #update display
        pygame.display.update()
        mainClock.tick(60)

#remove in real version
equiped, equipmentList, equipmentImages = initializeGear()
equipment(equiped, equipmentList, equipmentImages)
