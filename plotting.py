import pygame
import sys
import math
import pyfirmata

# Initilizing Measurements
CM = 44.55         # Pixel
ROTRANGE = 270     # Degree
LINLENGTH = 7 * CM # Cm     # This value will be measured
PORT = "COM3"               # You should change this value according to the port that Arduino is connected
DEADZONE = 0.7 * CM         # This value also will be measured

# Read from Arduino
board = pyfirmata.Arduino(PORT)

it = pyfirmata.util.Iterator(board)
it.start()

pin_a0 = board.get_pin("a:0:i")
pin_a1 = board.get_pin("a:1:i")

# Initilizing Screen
pygame.init()
pygame.display.set_caption("Screen Output")
SIZE = WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode(SIZE)

# RGB Colors
background_color = 240, 240, 240
line_color = 80 , 80 , 200
cursor_color = 150 , 10 , 10

# Initilizing Font 
font = pygame.font.Font(None,16)

# Main Loop
running = True
while running:
    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    

    # Processing inputs
    Vrot = pin_a0.read() 
    Vlin = pin_a1.read()

    r = DEADZONE + Vlin*LINLENGTH
    angle = Vrot*ROTRANGE*(math.pi/180)
    tetha = -angle + 45*(math.pi/180)
    
    x = r*math.cos(tetha)
    y = r*math.sin(tetha)



    # Carrying the origin into 0
    x += WIDTH/2
    y += HEIGHT/2

    
    # Screen manipulations
    screen.fill(background_color)

    # Drawing Axes
    pygame.draw.line(screen,line_color,(WIDTH/2,0),(WIDTH/2,HEIGHT),width = 1)
    pygame.draw.line(screen,line_color,(0,HEIGHT/2),(WIDTH,HEIGHT/2),width = 1)

    # Drawing grid
    for i in range(19):
        text = font.render(str(i-9)+ " cm",True,(0,0,0))

        i = i*CM-1

        screen.blit(text,(WIDTH/2,-i+HEIGHT))
        screen.blit(text,(i,HEIGHT/2))

        pygame.draw.line(screen,line_color,(i,0),(i,HEIGHT),width = 1)
        pygame.draw.line(screen,line_color,(0,i),(WIDTH,i),width = 1)


    # Drawing cursor
    pygame.draw.line(screen,cursor_color,(WIDTH/2,HEIGHT/2),(x,y),width = 2)
    pygame.draw.circle(screen,cursor_color,(x,y),radius=8)
    pygame.draw.circle(screen,(0,0,0),(x,y),radius=2)

    # Drawing Values
    values = font.render(f"r={round(r/CM,2)} cm,Θ={round(angle*(180/math.pi),2)}°",True,(60,0,0))
    screen.blit(values,(x+10,y+10))


    pygame.display.update()