import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((810, 1000))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BROWN = (222, 184, 135)
LIGHT_GREEN = (144, 238, 144)
LIGHT_GRAY = (211, 211, 211)
LIGHT_PINK = (255, 182, 193)
DARK_BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)
DARK_GRAY = (169, 169, 169)
DARK_PINK = (255, 105, 180)

# Define font
font = pygame.font.Font(None, 36)

# Define button positions and sizes
# x, y, width, height
button_rects = {
    "1vs1": pygame.Rect(295, 300, 200, 50),
    "3vs3": pygame.Rect(295, 400, 200, 50),
    "6vs6": pygame.Rect(295, 500, 200, 50),
    "exit": pygame.Rect(295, 600, 200, 50),
    "music": pygame.Rect(650, 10, 150, 50)
}

# Load image for display menu
menu_image = pygame.image.load("/home/mete/Desktop/arena.jpeg")  # Replace "menu_image.jpg" with the path to your downloaded image

# Load music
pygame.mixer.music.load("/home/mete/Desktop/menu.mp3")  # Replace "your_music_file.mp3" with the path to your music file
pygame.mixer.music.play(-1)

# Music button state
music_playing = True

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if any button is clicked
            for button_name, rect in button_rects.items():
                if rect.collidepoint(event.pos):
                    if button_name == "exit":
                        running = False
                    elif button_name == "music":
                        if music_playing:
                            pygame.mixer.music.pause()
                            music_playing = False
                        else:
                            pygame.mixer.music.unpause()
                            music_playing = True
                    elif button_name in ["1vs1", "3vs3", "6vs6"]:


                        # Scene for 1vs1, 3vs3, and 6vs6 buttons clicked
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    if button_rects["music"].collidepoint(event.pos):
                                        if music_playing:
                                            pygame.mixer.music.pause()
                                            music_playing = False
                                        else:
                                            pygame.mixer.music.unpause()
                                            music_playing = True
                                    elif exit_button_rect.collidepoint(event.pos):  # Check if exit button is clicked
                                        running = False  # Exit the scene
                                        break  # Exit the scene loop
                                    elif "vs" not in button_name:
                                        print(f"Clicked on {button_name}")

                            if not running:  # Check if the scene should exit
                                break  # Exit the main scene loop

                            screen.fill((255, 255, 255))
                            screen.blit(menu_image, (0, 0))

                            # Draw exit button
                            exit_button_rect = button_rects["exit"].copy()
                            exit_button_rect.topleft = (10, 10)  # Set the position of the exit button rectangle
                            pygame.draw.rect(screen, DARK_PINK, exit_button_rect)
                            pygame.draw.rect(screen, LIGHT_PINK, exit_button_rect.inflate(-5, -5))
                            # Draw "Exit" text
                            text_surface = font.render("Exit", True, WHITE)
                            text_rect = text_surface.get_rect(topleft=(20, 20))  # Position the "Exit" text
                            screen.blit(text_surface, text_rect)

                            # Draw music button
                            pygame.draw.rect(screen, DARK_BROWN, button_rects["music"])
                            pygame.draw.rect(screen, LIGHT_BROWN, button_rects["music"].inflate(-5, -5))
                            if music_playing:
                                text_surface = font.render("Music", True, BLACK)
                            else:
                                text_surface = font.render("Music", True, WHITE)
                            text_rect = text_surface.get_rect(center=button_rects["music"].center)
                            screen.blit(text_surface, text_rect)

                            pygame.display.flip()






                    else:
                        print(f"Clicked on {button_name}")

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw menu image first
    screen.blit(menu_image, (0, 0))

    # Draw buttons on top of the menu image with 3D effect
    for button_name, rect in button_rects.items():
        if button_name in ["1vs1", "3vs3", "6vs6"]:
            pygame.draw.rect(screen, DARK_BROWN, rect)
            pygame.draw.rect(screen,LIGHT_BROWN, rect.inflate(-5, -5))
        elif button_name == "exit":
            pygame.draw.rect(screen, DARK_PINK, rect)
            pygame.draw.rect(screen, LIGHT_PINK, rect.inflate(-5, -5))
        else:
            pygame.draw.rect(screen, GRAY, rect)

        # Draw text on buttons
        text_surface = font.render(button_name, True, WHITE)  # Change text color to WHITE
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    # Draw music button text
    if music_playing:
        text_surface = font.render("Music", True, BLACK)
    else:
        text_surface = font.render("Music", True, WHITE)
    text_rect = text_surface.get_rect(center=button_rects["music"].center)
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
