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
    equipmentInfo = {}
    equipmentInfo['helmet1'] = {}
    equipmentInfo['helmet2'] = {}
    equipmentInfo['helmet3'] = {}
    equipmentInfo['jacket1'] = {}
    equipmentInfo['jacket2'] = {}
    equipmentInfo['jacket3'] = {}
    equipmentInfo['belt1'] = {}
    equipmentInfo['belt2'] = {}
    equipmentInfo['belt3'] = {}
    equipmentInfo['pants1'] = {}
    equipmentInfo['pants2'] = {}
    equipmentInfo['pants3'] = {}
    equipmentInfo['boots1'] = {}
    equipmentInfo['boots2'] = {}
    equipmentInfo['boots3'] = {}
    equipmentInfo['goggles1'] = {}
    equipmentInfo['goggles2'] = {}
    equipmentInfo['goggles3'] = {}
    equipmentInfo['wrist1'] = {}
    equipmentInfo['wrist2'] = {}
    equipmentInfo['wrist3'] = {}
    equipmentInfo['gloves1'] = {}
    equipmentInfo['gloves2'] = {}
    equipmentInfo['gloves3'] = {}
    equipmentInfo['bandolier1'] = {}
    equipmentInfo['bandolier2'] = {}
    equipmentInfo['bandolier3'] = {}
    equipmentInfo['weapon1'] = {}
    equipmentInfo['weapon2'] = {}
    equipmentInfo['weapon3'] = {}


    #Create equipment displays using above specs
    equipmentInfo['helmet1']['Button'] = pygame.Rect(50,50,equipmentSize, equipmentSize)
    equipmentInfo['helmet1']['Image'] = pygame.image.load('pimp.png')
    equipmentInfo['helmet1']['Equiped'] = False
    equipmentInfo['helmet1']['Name'] = "Helm of Shaded Vision"
    equipmentInfo['helmet1']['Bonus'] = "+1 Perception"

    equipmentInfo['helmet2']['Button'] = pygame.Rect(equipmentSpace + 50,50,equipmentSize, equipmentSize)
    equipmentInfo['helmet2']['Image'] = pygame.image.load('archer.png')
    equipmentInfo['helmet2']['Equiped'] = False

    equipmentInfo['helmet3']['Button'] = pygame.Rect(2*equipmentSpace + 50,50,equipmentSize, equipmentSize)
    equipmentInfo['helmet3']['Image'] = pygame.image.load('bucket.png')
    equipmentInfo['helmet3']['Equiped'] = False

    equipmentInfo['jacket1']['Button'] = pygame.Rect(50,equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['jacket1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['jacket1']['Equiped'] = False

    equipmentInfo['jacket2']['Button'] = pygame.Rect(equipmentSpace + 50,equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['jacket2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['jacket2']['Equiped'] = False

    equipmentInfo['jacket3']['Button'] = pygame.Rect(2*equipmentSpace + 50,equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['jacket3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['jacket3']['Equiped'] = False

    equipmentInfo['belt1']['Button'] = pygame.Rect(50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['belt1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['belt1']['Equiped'] = False

    equipmentInfo['belt2']['Button'] = pygame.Rect(equipmentSpace + 50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['belt2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['belt2']['Equiped'] = False

    equipmentInfo['belt3']['Button'] = pygame.Rect(2*equipmentSpace + 50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['belt3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['belt3']['Equiped'] = False

    equipmentInfo['pants1']['Button'] = pygame.Rect(50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['pants1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['pants1']['Equiped'] = False

    equipmentInfo['pants2']['Button'] = pygame.Rect(equipmentSpace + 50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['pants2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['pants2']['Equiped'] = False

    equipmentInfo['pants3']['Button'] = pygame.Rect(2*equipmentSpace + 50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['pants3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['pants3']['Equiped'] = False

    equipmentInfo['boots1']['Button'] = pygame.Rect(50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['boots1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['boots1']['Equiped'] = False

    equipmentInfo['boots2']['Button'] = pygame.Rect(equipmentSpace + 50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['boots2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['boots2']['Equiped'] = False

    equipmentInfo['boots3']['Button'] = pygame.Rect(2*equipmentSpace + 50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['boots3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['boots3']['Equiped'] = False

    equipmentInfo['goggles1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),50,equipmentSize, equipmentSize)
    equipmentInfo['goggles1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['goggles1']['Equiped'] = False

    equipmentInfo['goggles2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),50,equipmentSize, equipmentSize)
    equipmentInfo['goggles2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['goggles2']['Equiped'] = False

    equipmentInfo['goggles3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),50,equipmentSize, equipmentSize)
    equipmentInfo['goggles3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['goggles3']['Equiped'] = False

    equipmentInfo['wrist1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['wrist1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['wrist1']['Equiped'] = False

    equipmentInfo['wrist2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['wrist2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['wrist2']['Equiped'] = False

    equipmentInfo['wrist3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['wrist3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['wrist3']['Equiped'] = False

    equipmentInfo['gloves1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['gloves1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['gloves1']['Equiped'] = False

    equipmentInfo['gloves2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['gloves2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['gloves2']['Equiped'] = False

    equipmentInfo['gloves3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['gloves3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['gloves3']['Equiped'] = False

    equipmentInfo['bandolier1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['bandolier1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['bandolier1']['Equiped'] = False

    equipmentInfo['bandolier2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['bandolier2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['bandolier2']['Equiped'] = False

    equipmentInfo['bandolier3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['bandolier3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['bandolier3']['Equiped'] = False

    equipmentInfo['weapon1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['weapon1']['Image'] = pygame.image.load('question.png')
    equipmentInfo['weapon1']['Equiped'] = False

    equipmentInfo['weapon2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['weapon2']['Image'] = pygame.image.load('question.png')
    equipmentInfo['weapon2']['Equiped'] = False

    equipmentInfo['weapon3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['weapon3']['Image'] = pygame.image.load('question.png')
    equipmentInfo['weapon3']['Equiped'] = False

    return equipmentInfo

def drawEquipment(equipmentList):

    for item in equipmentList:
        pygame.draw.rect(screen, WHITE, equipmentList[item]['Button'])

    """for item in equipmentList:
        x = equipmentList[item]['Button'].left
        y = equipmentList[item]["Button"].top + 5
        miscMethods.draw_text(item, font, BLACK, screen, x,y)"""

def equipGear(equipmentInfo, click):
    mx, my = pygame.mouse.get_pos()
    item1 = ""
    item2 = ""
    temp = ""
    for item in equipmentInfo:
        if equipmentInfo[item]['Button'].collidepoint((mx,my)) and item == 'helmet1':
            displayGear(equipmentInfo[item])
        if equipmentInfo[item]['Button'].collidepoint((mx,my)) and click:
            equipmentInfo[item]['Equiped'] = True
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

            equipmentInfo[item1]['Equiped'] = False
            equipmentInfo[item2]['Equiped'] = False

        if equipmentInfo[item]['Equiped']:
            screen.blit(check, (equipmentInfo[item]['Button'].left, equipmentInfo[item]['Button'].top))

    return equipmentInfo

def displayGear(item):
    miscMethods.draw_text(item['Name'], font, BLACK, screen, 700,930)
    miscMethods.draw_text(item['Bonus'], font, BLACK, screen, 700,980)

def equipment(equipmentInfo):

    while(True):
        screen.fill(GREY)
        #draw_text('Main Menu', font, WHITE, screen, 20, 20)
        #Get my mouse position
        #mx, my = pygame.mouse.get_pos()

        #Rect(X ALighn, Y Align, Width, Height)
        #Create paper doll with above specs
        character = pygame.Rect(668, 50, 584, equipmentSpace*5-30)

        #draw buttons
        drawEquipment(equipmentInfo)

        pygame.draw.rect(screen, WHITE, character)
        #test = pygame.image.load('symbol.png')

        for item in equipmentInfo:
            screen.blit(equipmentInfo[item]['Image'], (equipmentInfo[item]['Button'].left, equipmentInfo[item]['Button'].top+20))

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

        equipmentInfo = equipGear(equipmentInfo, click)

        #update display
        pygame.display.update()
        mainClock.tick(60)

#remove in real version
equipmentInfo = initializeGear()
equipment(equipmentInfo)
