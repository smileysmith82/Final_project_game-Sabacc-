import pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sabacc")

BG = pygame.transform.scale(pygame.image.load("Green_background.jpg"), (WIDTH, HEIGHT))
pygame.init()

round_counter = 1

def draw_button(screen, font, text, color, x, y, color_light=None, color_dark=None):
    # Calculate button coordinates and dimensions
    button_width, button_height = 140, 40
    button_rect = pygame.Rect(x, y, button_width, button_height)
    text_render = font.render(text, True, color)

    # Check if mouse is over the button
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_light, button_rect)
    else:
        pygame.draw.rect(screen, color_dark, button_rect)

    # Center the text on the button
    text_rect = text_render.get_rect(center=button_rect.center)
    screen.blit(text_render, text_rect) 

def round_count():  
    global round_counter
    round_counter += 1
    
def quit_function():
    print("Quitting")
    pygame.quit()

def draw_function():
    print("Draw")
    # Add draw logic here

def switch_function():
    print("Switch")
    # Add switch logic here

def fold_function():
    global round_counter
    print("Fold")
    # Add fold logic here
    round_counter += 1 # placeholder and will be removed
    
def start_function():
    global round_counter
    print("Starting Game")
    # Add starting game logic
    round_counter = 1
    
def quit_button(screen, font, text, x, y, color_light=None, color_dark=None):
    button_width, button_height = 100, 40
    button_rect = pygame.Rect(x, y, button_width, button_height)
    
    # Check if mouse is over the button
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_light, button_rect)
    else:
        pygame.draw.rect(screen, color_dark, button_rect)

    text_render = font.render(text, True, (0, 0, 0))  # Black color for quit button text
    text_rect = text_render.get_rect(center=button_rect.center)
    screen.blit(text_render, text_rect)

def main():
    global round_counter
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('ITC Serif Gothic', 35)
    color = (255, 255, 255)
    color_light_blue = (100, 149, 237)  # Light blue color
    color_dark_blue = (0, 0, 128)  # Dark blue color

    button_x = WIDTH - 140 - 20
    button_y = HEIGHT - 60 
    button_spacing = 20 

    quit_button_clicked = False  # Flag to track if quit button is clicked

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button is clicked
                for i in range(4):
                    button_rect = pygame.Rect(button_x - i * (140 + button_spacing), button_y, 140, 40)
                    if button_rect.collidepoint(event.pos):
                        if i == 0:
                            start_function()
                        elif i == 1:
                            draw_function()
                        elif i == 2:
                            switch_function()
                        elif i == 3:
                            fold_function()

                    # Check if the new button is clicked and it's not already clicked
                    new_button_rect = pygame.Rect(WIDTH - 120, 20, 100, 40)
                    if new_button_rect.collidepoint(event.pos) and not quit_button_clicked:
                        quit_function()  # Attach quit functionality to the new button
                        quit_button_clicked = True  # Set the flag to True

        # Fill the screen with background
        WIN.blit(BG, (0, 0))
        
        # Draw quit button on top right
        quit_button(WIN, font, 'Quit', WIDTH - 120, 20, (255, 0, 0), (200, 0, 0))
        
        # Draw round count
        round_text = font.render("Round: " + str(round_counter), True, color)
        WIN.blit(round_text, (20, 20))  # Adjusted x-coordinate to 20

        # Draw the buttons
        draw_button(WIN, font, 'Start', color, button_x, button_y, color_light_blue, color_dark_blue)
        for i, label in enumerate(["Draw", "Switch", "Fold"], start=1):
            draw_button(WIN, font, label, color, button_x - i * (140 + button_spacing), button_y, color_light_blue, color_dark_blue)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
