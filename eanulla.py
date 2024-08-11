import pygame

# Initialize Pygame
pygame.init()

# Set up display settings
W, H = 800, 600  # Example width and height
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Example player state
player_state = "Playing"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update FPS and set window caption
    fps = clock.get_fps()
    pygame.display.set_caption(f"fps: {fps:.2f}  res:{W}x{H}  {player_state}")
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Here you would update and draw your game objects
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
