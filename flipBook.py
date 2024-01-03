import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flip Book Example")

# Load images
image_folder = "images"  # Folder containing your images
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])

images = [pygame.image.load(os.path.join(image_folder, img)) for img in image_files]
current_frame = 0

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the current frame
    screen.blit(images[current_frame], (0, 0))
    current_frame = (current_frame + 1) % len(images)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
