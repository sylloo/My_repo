"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
h_size = 1280
v_size = 720
size = (h_size, v_size)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("-- Pomme poursuite --")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
rect_x = 50
rect_y = 50
vector_x = 5
vector_y = 5

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    if rect_x > (h_size-50) or rect_x<0:
        vector_x *= -1
    if rect_y > (v_size - 50) or rect_y<0:
        vector_y *= -1
		
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y , 40, 40])
    pygame.draw.rect(screen, RED, [ rect_x +10, rect_y +10, 20, 20])
    rect_x += vector_x
    rect_y += vector_y
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()