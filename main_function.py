import pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sabacc")

BG = pygame.transform.scale(pygame.image.load("Green_background.jpg"), (WIDTH, HEIGHT))
pygame.init()

def draw_button(screen, font, text, color, color_light, color_dark, x, y):
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

def draw_function():
    print("Draw")
    # Add draw logic here

def switch_function():
    print("Switch")
    # Add switch logic here

def discard_function():
    print("Discard")
    # Add discard logic here

def main():
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Corbel', 35)
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)

    button_x = WIDTH - 140 - 20
    button_y = HEIGHT - 60 
    button_spacing = 20 

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
                            print("Quitting")
                            run = False  # Quit the game when the quit button is clicked
                        elif i == 1:
                            draw_function()
                        elif i == 2:
                            switch_function()
                        elif i == 3:
                            discard_function()

        # Fill the screen with background
        WIN.blit(BG, (0, 0))

        # Draw the buttons
        draw_button(WIN, font, 'Quit', color, color_light, color_dark, button_x, button_y)
        for i, label in enumerate(["Draw", "Switch", "Discard"], start=1):
            draw_button(WIN, font, label, color, color_light, color_dark, button_x - i * (140 + button_spacing), button_y)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

