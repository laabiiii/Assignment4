import pygame

# Initialize pygame
pygame.init()

# Constants
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 40  # Match cell size for cleaner erasing

# Colors
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (225, 182, 193)

# Setup screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Canva-like Eraser")

# Create grid of rectangles
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Eraser rect
eraser = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)

clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position and update eraser
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.center = (mouse_x, mouse_y)

    # Check if mouse is clicked for erasing
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  # Left click
        grid = [rect for rect in grid if not eraser.colliderect(rect)]

    # Draw grid
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Draw eraser
    pygame.draw.rect(screen, PINK, eraser, 2)  # Draw border for visibility

    # Update display and control frame rate
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()
