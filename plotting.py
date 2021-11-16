import pygame
import sys
import math
import pyfirmata

############### Initilizing #################
# Initilizing Measurements
CM = 44.55           # Pixel
ROTRANGE = 270       # Degree
LINLENGTH = 6.6 * CM # Cm     # This value will be measured
PORT = "COM3"                 # You should change this value according to the port that Arduino is connected
DEADZONE = 0.0 * CM           # This value also will be measured


# Initilizing Arduino

board = pyfirmata.Arduino(PORT)

it = pyfirmata.util.Iterator(board)
it.start()

pin_a0 = board.get_pin("a:0:i")
pin_a1 = board.get_pin("a:1:i")


# Initilizing Screens
pygame.init()
pygame.display.set_caption("Screen Output")
programIcon = pygame.image.load('favicon.png')
pygame.display.set_icon(programIcon)

SIZE = WIDTH, HEIGHT = 800, 800
CM_PER_SCREEN = math.ceil(WIDTH/CM)

screen = pygame.display.set_mode(SIZE)
pygame.mouse.set_visible(False)

# InitilizingScreen Options
toggle_projection = False

# Initilizing RGB Colors
background_color = 240, 240, 240
line_color = 80 , 80 , 200
cursor_color = 150 , 10 , 10

# Initilizing Fonts 
font = pygame.font.Font(None,16)
big_font = pygame.font.Font(None,54)

# Initilizing Intro
intro = True
intro_screen = pygame.image.load('cover.png')

################# Main Loop ######################
running = True
while running:
    # Keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # Exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g: toggle_projection = not(toggle_projection) # Toggle Projections

    ################# Processing Information ######################
    Vrot = pin_a0.read() 
    Vlin = pin_a1.read()

    r = DEADZONE + Vlin*LINLENGTH
    tetha = (1-Vrot)*ROTRANGE*(math.pi/180)
    angle = -tetha + 45*(math.pi/180)
    
    x = r*math.cos(angle)
    y = r*math.sin(angle)



    # Carrying the origin into 0
    x += WIDTH/2
    y += HEIGHT/2

    
    ################# Drawing Background ######################
    screen.fill(background_color)

    # Drawing Axes
    pygame.draw.line(screen,line_color,(WIDTH/2,0),(WIDTH/2,HEIGHT),width = 1)
    pygame.draw.line(screen,line_color,(0,HEIGHT/2),(WIDTH,HEIGHT/2),width = 1)

    # Drawing grid
    for i in range(CM_PER_SCREEN):
        text = font.render(str(i-9)+ " cm",True,(0,0,0))

        i = i*CM-1

        pygame.draw.line(screen,line_color,(i,0),(i,HEIGHT),width = 1)
        pygame.draw.line(screen,line_color,(0,i),(WIDTH,i),width = 1)
        pygame.draw.circle(screen,line_color,(i,HEIGHT/2),radius=3)
        pygame.draw.circle(screen,line_color,(WIDTH/2,i),radius=3)

        screen.blit(text,(WIDTH/2+5,-i+HEIGHT+5))
        screen.blit(text,(i+5,HEIGHT/2+5))

    ################# Drawing Variables ######################
    # Drawing Projections
    if toggle_projection:
        pygame.draw.line(screen,(255,100,100),(x,HEIGHT/2),(x,y),width = 2)
        pygame.draw.line(screen,(255,100,100),(WIDTH/2,y),(x,y),width = 2)
        pygame.draw.circle(screen,(255,100,100),(x,HEIGHT/2),radius=4)
        pygame.draw.circle(screen,(255,100,100),(WIDTH/2,y),radius=4)

    # Drawing cursor
    pygame.draw.line(screen,cursor_color,(WIDTH/2,HEIGHT/2),(x,y),width = 2)
    pygame.draw.circle(screen,cursor_color,(x,y),radius=8)
    pygame.draw.circle(screen,(0,0,0),(x,y),radius=2)

    # Drawing Cursor Description
    value_text = f"r={round(r/CM,2)} cm,Θ={round(tetha*(180/math.pi),2)}°"
    values = font.render(value_text,True,(60,0,0))
    screen.blit(values,(x+10,y+10))

    # Drawing info box
    pygame.draw.rect(screen,background_color,pygame.Rect(0, HEIGHT-CM*2+15, WIDTH, CM*2+15))
    info_text = f"r={round(r/CM,2)}cm  Θ={round(tetha*(180/math.pi),2)}°  x={round(x/CM-9,2)}cm  y={-(round(y/CM-9,2))}cm"
    desc = big_font.render(info_text,True,line_color)
    screen.blit(desc,(20,HEIGHT-4*CM/3))
    
    # Drawing Intro
    if intro:
        screen.blit(intro_screen,(0,0))
        if pygame.mouse.get_pressed()[0]: intro = 0
    
    # Drawing mouse info
    m_x, m_y = pygame.mouse.get_pos()
    loc = (m_x+10,m_y+10)
    if m_x > 720:
        loc = (m_x-80,m_y+10)
    mouse_info = f"x={round(m_x/CM-9,2)}, y={round(-m_y/CM+9,2)}"
    m_desc = font.render(mouse_info,True,(60,0,0))
    screen.blit(m_desc,loc)
    pygame.draw.circle(screen,(0,0,0),(m_x,m_y),radius=2)

    pygame.display.update()
