import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame, sys
from pygame.locals import *
                    
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0), FULLSCREEN | RESIZABLE)

# Colors
color_list = [(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,0,255),(255,255,0)]
c_red, c_green, c_blue, c_cyan, c_magenta, c_yellow = color_list

# Font
font = pygame.font.Font('Delight_Candles.ttf', 40)
clear_surf = font.render('Clear', False, (150,150,150))
clear_rect = clear_surf.get_rect(center=(350,45))

exit_surf = font.render('Exit', False, (150,150,150))
exit_rect = exit_surf.get_rect(center=(1150,45))

# Variables
touch_list = []
lines_list = []
color = 0
border_loc = (0,0)

running = True
while running:    
    
    for event in pygame.event.get():
        
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            pygame.quit()
            sys.exit()
        
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((0,0), FULLSCREEN | RESIZABLE)
            lines_list.clear()
            screen.fill((0,0,0))
            if screen.get_height() >= 1000:
                if color == c_red:
                    border_loc = (55,500)
                elif color == c_green:
                    border_loc = (55, 600)
                elif color == c_blue:
                    border_loc = (55, 700)
                elif color == c_cyan:
                    border_loc = (55, 800)
                elif color == c_magenta:
                    border_loc = (55, 900)
                elif color == c_yellow:
                    border_loc = (55, 1000)
            elif screen.get_height() < 1000:
                if color == c_red:
                    border_loc = (500,50)
                elif color == c_green:
                    border_loc = (600, 50)
                elif color == c_blue:
                    border_loc = (700, 50)
                elif color == c_cyan:
                    border_loc = (800, 50)
                elif color == c_magenta:
                    border_loc = (900, 50)
                elif color == c_yellow:
                    border_loc = (1000, 50)
            
        elif event.type == FINGERDOWN:
            if red.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                color = c_red
                if screen.get_height() >= 1000: border_loc = (55, 500)
                else: border_loc = (500, 50)
            
            elif green.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                color = c_green
                if screen.get_height() >= 1000: border_loc = (55, 600)
                else: border_loc = (600, 50)
            
            elif blue.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                color = c_blue
                if screen.get_height() >= 1000: border_loc = (55, 700)
                else: border_loc = (700, 50)
            
            elif cyan.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                color = c_cyan
                if screen.get_height() >= 1000: border_loc = (55, 800)
                else: border_loc = (800, 50)
            
            elif magenta.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                color = c_magenta
                if screen.get_height() >= 1000: border_loc = (55, 900)
                else: border_loc = (900, 50)
            
            elif yellow.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                color = c_yellow
                if screen.get_height() >= 1000: border_loc = (55, 1000)
                else: border_loc = (1000, 50)
                   
            elif exit_rect.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                running = False
                pygame.quit()
                sys.exit()
                
            elif clear_rect.collidepoint((screen.get_width() * event.x), (screen.get_height() * event.y)):
                lines_list.clear()
                screen.fill((0,0,0))
            
            else:
                touch_list = [tuple((int(screen.get_width() * event.x), int(screen.get_height() * event.y)))]
                
        elif event.type == FINGERMOTION:
            touch_list.append(tuple((int(screen.get_width() * event.x), int(screen.get_height() * event.y))))
        
        elif event.type == FINGERUP:
            if touch_list and color:
                lines_list.append(tuple((list(touch_list), (color))))
            touch_list = [] 
    
    screen.fill((0,0,0))
    
    if screen.get_height() >= 1000:
        red = pygame.draw.circle(screen, (255,0,0), (55, 500), 40)
        green = pygame.draw.circle(screen, (0,255,0), (55, 600), 40)
        blue = pygame.draw.circle(screen, (0,0,255), (55, 700), 40)
        cyan = pygame.draw.circle(screen, (0,255,255), (55, 800), 40)
        magenta = pygame.draw.circle(screen, (255,0,255), (55, 900), 40)
        yellow = pygame.draw.circle(screen, (255,255,0), (55, 1000), 40)
 
        clear_rect = clear_surf.get_rect(center=(55,410))
        exit_rect = exit_surf.get_rect(center=(55,1100))
   
    else:
        red = pygame.draw.circle(screen, (255,0,0), (500, 50), 40)
        green = pygame.draw.circle(screen, (0,255,0), (600, 50), 40)
        blue = pygame.draw.circle(screen, (0,0,255), (700, 50), 40)
        cyan = pygame.draw.circle(screen, (0,255,255), (800, 50), 40)
        magenta = pygame.draw.circle(screen, (255,0,255), (900, 50), 40)
        yellow = pygame.draw.circle(screen, (255,255,0), (1000, 50), 40)
        
        clear_rect = clear_surf.get_rect(center=(350,50))
        exit_rect = exit_surf.get_rect(center=(1125,50))

    screen.blit(clear_surf, clear_rect)
    screen.blit(exit_surf, exit_rect)
    
    if color:
        pygame.draw.circle(screen, (255,255,255), border_loc, 41, 25)
             
    if len(touch_list) >= 2:
        pygame.draw.aalines(screen, color, False, touch_list)
    
    if lines_list and color:
        for line in lines_list:
            pygame.draw.aalines(screen, line[1], False, line[0])
    
    pygame.display.update()
    clock.tick(60)