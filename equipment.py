import pygame, sys
from pygame.locals import *
from misc import miscMethods

#Set dimensions of the screen


mainClock = pygame.time.Clock()
#pygame.mixer.pre_init(44100, 16, 2, 4096)
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
check = pygame.image.load('assets/images/check.png')
clothEquip = pygame.mixer.Sound('assets/sound/clothequip.wav')
leatEquip = pygame.mixer.Sound('assets/sound/leatequip.wav')
metalEquip = pygame.mixer.Sound('assets/sound/metalequip.wav')

def initializeCharacter():
    characterInfo = {}
    #Number of Attacks performed per round
    characterInfo['NumAttacks'] = 0
    #Damage given each attack
    characterInfo['AttDmg'] = 0
    #Value added to each attack
    characterInfo['AttMod'] = 0
    #How fast the character moves in the overworld
    characterInfo['Speed'] = 0
    #How much dmg is mitigated from each hit
    characterInfo['Armor'] = 0
    #What type of damage is used
    characterInfo['DamageType'] = ""
    return characterInfo

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
    equipmentInfo['ammo1'] = {}
    equipmentInfo['ammo2'] = {}
    equipmentInfo['ammo3'] = {}
    equipmentInfo['weapon1'] = {}
    equipmentInfo['weapon2'] = {}
    equipmentInfo['weapon3'] = {}


    #Create equipment displays using above specs

    ################
    #Basic CLothing#
    ################

    equipmentInfo['helmet1']['Button'] = pygame.Rect(50,50,equipmentSize, equipmentSize)
    equipmentInfo['helmet1']['Image'] = pygame.image.load('assets/images/pimp.png')
    equipmentInfo['helmet1']['Equiped'] = False
    equipmentInfo['helmet1']['Name'] = "Cloth Hat"
    equipmentInfo['helmet1']['Speed'] = 1

    equipmentInfo['helmet2']['Button'] = pygame.Rect(equipmentSpace + 50,50,equipmentSize, equipmentSize)
    equipmentInfo['helmet2']['Image'] = pygame.image.load('assets/images/archer.png')
    equipmentInfo['helmet2']['Equiped'] = False
    equipmentInfo['helmet2']['Name'] = "Leather Cap"
    equipmentInfo['helmet2']['Armor'] = 1

    equipmentInfo['helmet3']['Button'] = pygame.Rect(2*equipmentSpace + 50,50,equipmentSize, equipmentSize)
    equipmentInfo['helmet3']['Image'] = pygame.image.load('assets/images/bucket.png')
    equipmentInfo['helmet3']['Equiped'] = False
    equipmentInfo['helmet3']['Name'] = "Skull Cap"
    equipmentInfo['helmet3']['Armor'] = 2
    equipmentInfo['helmet3']['Speed'] = -1

    equipmentInfo['jacket1']['Button'] = pygame.Rect(50,equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['jacket1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['jacket1']['Equiped'] = False
    equipmentInfo['jacket1']['Name'] = "Cloth Jacket"
    equipmentInfo['jacket1']['Speed'] = 1

    equipmentInfo['jacket2']['Button'] = pygame.Rect(equipmentSpace + 50,equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['jacket2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['jacket2']['Equiped'] = False
    equipmentInfo['jacket2']['Name'] = "Leather Jacket"
    equipmentInfo['jacket2']['Armor'] = 1

    equipmentInfo['jacket3']['Button'] = pygame.Rect(2*equipmentSpace + 50,equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['jacket3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['jacket3']['Equiped'] = False
    equipmentInfo['jacket3']['Name'] = "Flak Vest"
    equipmentInfo['jacket3']['Armor'] = 2
    equipmentInfo['jacket3']['Speed'] = -1

    equipmentInfo['pants1']['Button'] = pygame.Rect(50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['pants1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['pants1']['Equiped'] = False
    equipmentInfo['pants1']['Name'] = "Cloth Pants"
    equipmentInfo['pants1']['Speed'] = 1

    equipmentInfo['pants2']['Button'] = pygame.Rect(equipmentSpace + 50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['pants2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['pants2']['Equiped'] = False
    equipmentInfo['pants2']['Name'] = "Leather Pants"
    equipmentInfo['pants2']['Armor'] = 1

    equipmentInfo['pants3']['Button'] = pygame.Rect(2*equipmentSpace + 50,3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['pants3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['pants3']['Equiped'] = False
    equipmentInfo['pants3']['Name'] = "Ballistic Pants"
    equipmentInfo['pants3']['Armor'] = 2
    equipmentInfo['pants3']['Speed'] = -1

    #############
    #Accessories#
    #############

    equipmentInfo['belt1']['Button'] = pygame.Rect(50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['belt1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['belt1']['Equiped'] = False
    equipmentInfo['belt1']['Name'] = "Healing Potions"
    equipmentInfo['belt1']['Effect'] = "Fully Heals on use"

    equipmentInfo['belt2']['Button'] = pygame.Rect(equipmentSpace + 50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['belt2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['belt2']['Equiped'] = False
    equipmentInfo['belt2']['Name'] = "Armor Potions"
    equipmentInfo['belt2']['Effect'] = "Doubles Armor for next battle"

    equipmentInfo['belt3']['Button'] = pygame.Rect(2*equipmentSpace + 50,2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['belt3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['belt3']['Equiped'] = False
    equipmentInfo['belt3']['Name'] = "Damage Potions"
    equipmentInfo['belt3']['Effect'] = "Doubles damage for next battle"

    equipmentInfo['boots1']['Button'] = pygame.Rect(50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['boots1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['boots1']['Equiped'] = False
    equipmentInfo['boots1']['Name'] = "Victorias"
    equipmentInfo['boots1']['Speed'] = 2

    equipmentInfo['boots2']['Button'] = pygame.Rect(equipmentSpace + 50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['boots2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['boots2']['Equiped'] = False
    equipmentInfo['boots2']['Name'] = "Insulated Boots"
    equipmentInfo['boots2']['Effect'] = "Reduces elemental damage by half"

    equipmentInfo['boots3']['Button'] = pygame.Rect(2*equipmentSpace + 50,4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['boots3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['boots3']['Equiped'] = False
    equipmentInfo['boots3']['Name'] = "Shock Absorbers"
    equipmentInfo['boots3']['Effect'] = "Eliminates fall damage"

    equipmentInfo['goggles1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),50,equipmentSize, equipmentSize)
    equipmentInfo['goggles1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['goggles1']['Equiped'] = False
    equipmentInfo['goggles1']['Name'] = "Thermal Vision"
    equipmentInfo['goggles1']['Effect'] = "Enables Thermal Vision"

    equipmentInfo['goggles2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),50,equipmentSize, equipmentSize)
    equipmentInfo['goggles2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['goggles2']['Equiped'] = False
    equipmentInfo['goggles2']['Name'] = "Increased Perception"
    equipmentInfo['goggles2']['AttMod'] = 3

    equipmentInfo['goggles3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),50,equipmentSize, equipmentSize)
    equipmentInfo['goggles3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['goggles3']['Equiped'] = False
    equipmentInfo['goggles3']['Name'] = "Eagle Vision"
    equipmentInfo['goggles3']['NumAttacks'] = 1

    equipmentInfo['wrist1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['wrist1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['wrist1']['Equiped'] = False
    equipmentInfo['wrist1']['Name'] = "Dart Launcher"
    equipmentInfo['wrist1']['Effect'] = "Shoots tranquilizer darts"

    equipmentInfo['wrist2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['wrist2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['wrist2']['Equiped'] = False
    equipmentInfo['wrist2']['Name'] = "Electric Net"
    equipmentInfo['wrist2']['Effect'] = "Traps enemies"

    equipmentInfo['wrist3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['wrist3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['wrist3']['Equiped'] = False
    equipmentInfo['wrist3']['Name'] = "Grappling Hook"
    equipmentInfo['wrist3']['Effect'] = "Allows access to higher areas"

    equipmentInfo['gloves1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['gloves1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['gloves1']['Equiped'] = False
    equipmentInfo['gloves1']['Name'] = "Itchy Fingers"
    equipmentInfo['gloves1']['AttMod'] = 3

    equipmentInfo['gloves2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['gloves2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['gloves2']['Equiped'] = False
    equipmentInfo['gloves2']['Name'] = "Steady Hands"
    equipmentInfo['gloves2']['NumAttacks'] = 1

    equipmentInfo['gloves3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),2*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['gloves3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['gloves3']['Equiped'] = False
    equipmentInfo['gloves3']['Name'] = "Insulated Gloves"
    equipmentInfo['gloves3']['Effect'] = "Reduces elemental damage by half"

    equipmentInfo['ammo1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['ammo1']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['ammo1']['Equiped'] = False
    equipmentInfo['ammo1']['Name'] = "Steel Rounds"
    equipmentInfo['ammo1']['Type'] = "Steel"

    equipmentInfo['ammo2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['ammo2']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['ammo2']['Equiped'] = False
    equipmentInfo['ammo2']['Name'] = "Silver Rounds"
    equipmentInfo['ammo2']['Type'] = "Silver"

    equipmentInfo['ammo3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),3*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['ammo3']['Image'] = pygame.image.load('assets/images/question.png')
    equipmentInfo['ammo3']['Equiped'] = False
    equipmentInfo['ammo3']['Name'] = "Non-Lethal Rounds"
    equipmentInfo['ammo3']['Type'] = "Non-Lethal"

    equipmentInfo['weapon1']['Button'] = pygame.Rect((WIDTH - equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['weapon1']['Image'] = pygame.image.load('assets/images/pistols.png')
    equipmentInfo['weapon1']['Equiped'] = False
    equipmentInfo['weapon1']['Name'] = "Dual Pistols"
    equipmentInfo['weapon1']['NumAttacks'] = 6
    equipmentInfo['weapon1']['AttDmg'] = 6

    equipmentInfo['weapon2']['Button'] = pygame.Rect((WIDTH - 2*equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['weapon2']['Image'] = pygame.image.load('assets/images/rifle.png')
    equipmentInfo['weapon2']['Equiped'] = False
    equipmentInfo['weapon2']['Name'] = "Rifle"
    equipmentInfo['weapon2']['NumAttacks'] = 2
    equipmentInfo['weapon2']['AttDmg'] = 18

    equipmentInfo['weapon3']['Button'] = pygame.Rect((WIDTH - 3*equipmentSpace-15),4*equipmentSpace+50,equipmentSize, equipmentSize)
    equipmentInfo['weapon3']['Image'] = pygame.image.load('assets/images/bow.png')
    equipmentInfo['weapon3']['Equiped'] = False
    equipmentInfo['weapon3']['Name'] = "Flamethrower"
    equipmentInfo['weapon3']['NumAttacks'] = 8
    equipmentInfo['weapon3']['AttDmg'] = 2

    return equipmentInfo

def displayStats(characterInfo):
    #Calculate and display character stats
    armor = "Armor: " +  str(characterInfo['Armor'])
    speed = "Speed: " + str(characterInfo['Speed'])
    attackDamage = characterInfo['NumAttacks'] * (characterInfo['AttDmg'] + characterInfo['AttMod'])
    damage = "Damage: " + str(attackDamage)
    damageType = 'Damage Type: ' + characterInfo['DamageType']

    miscMethods.draw_text(armor, font, BLACK, screen, 700,100)
    miscMethods.draw_text(speed, font, BLACK, screen, 700,140)
    miscMethods.draw_text(damage, font, BLACK, screen, 700,180)
    miscMethods.draw_text(damageType, font, BLACK, screen, 700,220)

def calculateStats(equipmentInfo):
    characterInfo = initializeCharacter()
    for item in equipmentInfo:
        if equipmentInfo[item]['Equiped']:
            for key in equipmentInfo[item]:
                if key=='Armor':
                    characterInfo['Armor'] += equipmentInfo[item][key]
                if key=='Speed':
                    characterInfo['Speed'] += equipmentInfo[item][key]
                if key=='NumAttacks':
                    characterInfo['NumAttacks'] += equipmentInfo[item][key]
                if key=='AttDmg':
                    characterInfo['AttDmg'] += equipmentInfo[item][key]
                if key=='AttMod':
                    characterInfo['AttMod'] += equipmentInfo[item][key]



    return characterInfo

def determineDamageType(equipmentInfo, DamageType):
    if equipmentInfo['ammo1']['Equiped']:
        if equipmentInfo['weapon3']['Equiped']:
            DamageType = "Molten Steel"
        else:
            DamageType = equipmentInfo['ammo1']['Name']
    if equipmentInfo['ammo2']['Equiped']:
        if equipmentInfo['weapon3']['Equiped']:
            DamageType = "Molten Silver"
        else:
            DamageType = equipmentInfo['ammo2']['Name']
    if equipmentInfo['ammo3']['Equiped']:
        if equipmentInfo['weapon3']['Equiped']:
            DamageType = "CS Gas"
        else:
            DamageType = equipmentInfo['ammo3']['Name']

    return DamageType

def drawEquipment(equipmentList):
    #create buttons for equipment
    for item in equipmentList:
        pygame.draw.rect(screen, WHITE, equipmentList[item]['Button'])

    #write names above equipment, will remove later
    for item in equipmentList:
        x = equipmentList[item]['Button'].left
        y = equipmentList[item]["Button"].top + 5
        miscMethods.draw_text(item, font, BLACK, screen, x,y)

def equipGear(equipmentInfo, click):
    mx, my = pygame.mouse.get_pos()
    item1 = ""
    item2 = ""
    temp = ""
    #Equips only one of each item type
    for item in equipmentInfo:
        if equipmentInfo[item]['Button'].collidepoint((mx,my)):
            displayGear(equipmentInfo[item])
        if equipmentInfo[item]['Button'].collidepoint((mx,my)) and click:
            equipmentInfo[item]['Equiped'] = True
            temp = item
            if '1' in temp:
                item1 = temp.replace('1', '2')
                item2 = temp.replace('1', '3')
                pygame.mixer.Sound.play(clothEquip)
            if '2' in temp:
                item1 = temp.replace('2', '1')
                item2 = temp.replace('2', '3')
                pygame.mixer.Sound.play(leatEquip)
            if '3' in temp:
                item1 = temp.replace('3', '1')
                item2 = temp.replace('3', '2')
                pygame.mixer.Sound.play(metalEquip)

            equipmentInfo[item1]['Equiped'] = False
            equipmentInfo[item2]['Equiped'] = False


        if equipmentInfo[item]['Equiped']:
            screen.blit(check, (equipmentInfo[item]['Button'].left, equipmentInfo[item]['Button'].top))

    return equipmentInfo

def displayGear(item):
    #Writes gear stats on lower screen
    y = 880
    miscMethods.draw_text(item['Name'], font, BLACK, screen, 700,y)
    text = ""
    for key in item:
        if key!= 'Button' and key!='Image' and key!='Equiped' and key!='Name':
            y+=40
            text = key + ": " + str(item[key])
            miscMethods.draw_text(text, font, BLACK, screen, 700,y)


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
        characterInfo = calculateStats(equipmentInfo)
        characterInfo['DamageType'] = determineDamageType(equipmentInfo, characterInfo['DamageType'])
        displayStats(characterInfo)
        #test = pygame.image.load('symbol.png')

        for item in equipmentInfo:
            screen.blit(equipmentInfo[item]['Image'], (equipmentInfo[item]['Button'].left+15, equipmentInfo[item]['Button'].top+20))

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

#characterInfo = initializeCharacter()
equipmentInfo = initializeGear()
equipment(equipmentInfo)
