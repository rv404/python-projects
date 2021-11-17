"""
Ways to get the full size and the available size of a mobile screen:
- pygame.display.list_modes() -> list[tuple(full width: int, full height: int)]
- pygame.display.Info().current_w -> available width: int
- pygame.display.Info().current_h -> available height: int
* Note: values update automatically when the phone's screen' orientation changes.

* Be sure to add the pygame.RESIZABLE flag to the pygame.display.set_modes() and check for event.type == VIDEORESIZE events in the event loop (so that you can reset the set_modes method) if you want to check sizes in both landscape and portrait orientations without needing to close the program.

* Class should be called in a boilerplate pygame file with an existing display surface, game loop, and event loop (that includes VIDEORESIZE checks). Display surface can be set with: DISPSURF = pygame.display.set_modes((0,0), pygame.FULLSCREEN | pygame.RESIZABLE) to get a fullscreen surface.
"""

class GetScreenSize():
    def __init__(self):
        self.list_modes = pygame.display.list_modes()
        
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
       
        self.string = ""
        self.font = pygame.font.Font(None, 35)
        self.close_font = pygame.font.Font(None, 40)
        
        self.close_surf = self.close_font.render(" Close ", True, (255, 255, 255), (200, 0, 0))
        self.close_rect = self.close_surf.get_rect()
                                
    def draw(self, screen):
        # Update variables in case screen has been resized since the Class was instantiated
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        
        self.list_modes = pygame.display.list_modes()
        if len(self.list_modes) <= 1:
            self.list_modes = self.list_modes[0]
            self.string = f"Available screen mode: {self.list_modes}"
        else:
            self.string = f"Available screen modes: {self.list_modes}"
        
        font_surf = self.font.render(self.string, True, (255, 255, 255))
        font_rect = font_surf.get_rect()
        font_rect.center = (int(self.width / 2), int(self.height / 2) - 75)
    
        font_surf2 = self.font.render(f"Current available width: {self.width}px", True, (255, 255, 255))
        font_rect2 = font_surf2.get_rect()
        font_rect2.center = (int(self.width / 2), int(self.height / 2))      
        
        font_surf3 = self.font.render(f"Current available height: {self.height}px", True, (255, 255, 255))
        font_rect3 = font_surf3.get_rect()
        font_rect3.center = (int(self.width / 2), int(self.height / 2) + 75)      
        
        self.close_rect.center = (int(self.width / 2), int(self.height / 2) + 200)
                
        screen.fill((30, 30, 30))
        
        pygame.draw.line(screen, (255, 255, 255), (0, self.height // 2), (25, self.height // 2 - 25))
        pygame.draw.line(screen, (255, 255, 255), (0, self.height // 2), (25, self.height // 2 + 25))
        pygame.draw.line(screen, (255, 255, 255), (self.width, self.height // 2), (self.width - 25, self.height // 2 - 25))
        pygame.draw.line(screen, (255, 255, 255), (self.width, self.height // 2), (self.width - 25, self.height // 2 + 25))
        
        pygame.draw.line(screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2 - 25, 25))
        pygame.draw.line(screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2 + 25, 25))
        pygame.draw.line(screen, (255, 255, 255), (self.width // 2, self.height), (self.width // 2 - 25, self.height - 25))
        pygame.draw.line(screen, (255, 255, 255), (self.width // 2, self.height), (self.width // 2 + 25, self.height - 25))
        
        screen.blit(font_surf, font_rect)
        screen.blit(font_surf2, font_rect2)
        screen.blit(font_surf3, font_rect3)
        screen.blit(self.close_surf, self.close_rect)
        
    def checkForClose(self, screen):
        if event.type == pygame.FINGERDOWN and self.close_rect.collidepoint(self.width * event.x, self.height * event.y):
            self.close_surf = self.close_font.render(" Close ", True, (255, 255, 255), (0, 200, 200))
            self.close_rect = self.close_surf.get_rect()
            self.close_rect.center = (int(self.width / 2), int(self.height / 2) + 200)
            
            screen.blit(self.close_surf, self.close_rect)
            pygame.display.update()
            
            pygame.time.wait(100)
            pygame.quit()
                            
    def print(self):
        print(self.string)
        print(f"The current available width is {self.width}px and the current available height is {self.height}px.")
    
    def debug(self, screen, x=10, y=10):
        info = (0, 0)
        for event in pygame.event.get(FINGERMOTION):
            if event.type == FINGERMOTION:
                info = (event.x, event.y)
        
        #screen = pygame.display.get_surface()
        debug_surf = self.font.render(str(info), True, (255, 255, 255))
        debug_rect = debug_surf.get_rect(topleft=(x, y))
        screen.blit(debug_surf, debug_rect)
        
if __name__ == '__main__':
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
    import pygame
    from pygame.locals import *

    pygame.init()

    SCREEN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    FPS = 30

    screensize = GetScreenSize()

    running = True
    while running:
        for event in pygame.event.get():
            screensize.checkForClose(SCREEN)
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            if event.type == QUIT:
                running = False
            if event.type == VIDEORESIZE:
                SCREEN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    
        screensize.draw(SCREEN)
    
        pygame.display.update()
        CLOCK.tick(FPS)

    pygame.quit()