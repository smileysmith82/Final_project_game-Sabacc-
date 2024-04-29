import pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sabacc")

# Define the desired resolution for the images
IMAGE_WIDTH, IMAGE_HEIGHT = 100, 133

# Load background image
BG = pygame.transform.scale(pygame.image.load("Green_background.jpg"), (WIDTH, HEIGHT))

pygame.init()

round_counter = 1
discard_pile = ['r_10_t.png', 'g_2_s.png']
player_hand = ['r_10_s.png', 'sylops.png']
dealer_hand = ['up_backside.png', 'up_backside.png']

# Function to load images with desired resolution
def load_image(image_path):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

# Load card images with desired resolution
card_images = {card: load_image(card) for card in discard_pile + player_hand + dealer_hand}

def display_dealer_hand(hand):
    card_spacing = 20
    hand_width = len(hand) * IMAGE_WIDTH + (len(hand) - 1) * card_spacing
    x_offset = (WIDTH - hand_width) // 2
    y_offset = 50
    for i, card in enumerate(hand):
        WIN.blit(card_images[card], (x_offset + i * (IMAGE_WIDTH + card_spacing), y_offset))

def display_hand(hand):
    card_spacing = 20
    hand_width = len(hand) * IMAGE_WIDTH + (len(hand) - 1) * card_spacing
    x_offset = (WIDTH - hand_width) // 2
    y_offset = HEIGHT - 300
    for i, card in enumerate(hand):
        WIN.blit(card_images[card], (x_offset + i * (IMAGE_WIDTH + card_spacing), y_offset))

def display_deck():
    main_deck_back_image = load_image("up_backside.png")
    deck_width = IMAGE_WIDTH * 2 + 20
    x_deck_offset = (WIDTH - deck_width) // 2
    WIN.blit(main_deck_back_image, (x_deck_offset, 250))

def display_discard(discard_pile):
    if discard_pile:
        top_card = card_images[discard_pile[-1]]
        x_deck_offset = (WIDTH - IMAGE_WIDTH * 2 - 20) // 2
        WIN.blit(top_card, (x_deck_offset + 120, 250))

def draw_button(screen, font, text, color, x, y, color_light=None, color_dark=None):
    button_width, button_height = 140, 40
    button_rect = pygame.Rect(x, y, button_width, button_height)
    text_render = font.render(text, True, color)

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_light, button_rect)
    else:
        pygame.draw.rect(screen, color_dark, button_rect)

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

def switch_function(selected_card_index):
    print("Switch")
    global discard_pile, player_hand
    if selected_card_index is not None and len(discard_pile) > 0 and 0 <= selected_card_index < len(player_hand):
        selected_card = player_hand[selected_card_index]
        player_hand[selected_card_index] = discard_pile.pop()
        discard_pile.append(selected_card)

    print(player_hand)
    print(discard_pile)

def fold_function():
    global round_counter
    print("Fold")
    round_counter += 1

def start_function():
    global round_counter
    print("Starting Game")
    round_counter = 1

def quit_button(screen, font, text, x, y, color_light=None, color_dark=None):
    button_width, button_height = 100, 40
    button_rect = pygame.Rect(x, y, button_width, button_height)

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_light, button_rect)
    else:
        pygame.draw.rect(screen, color_dark, button_rect)

    text_render = font.render(text, True, (0, 0, 0))
    text_rect = text_render.get_rect(center=button_rect.center)
    screen.blit(text_render, text_rect)

def detect_hover(mouse_pos, hand, x_offset, y_offset, discard_rect, discard_pile):
    card_spacing = 20
    card_width, card_height = IMAGE_WIDTH, IMAGE_HEIGHT
    
    # Check if the mouse is over any card in the player's hand
    for i, card in enumerate(hand):
        card_rect = pygame.Rect(x_offset + i * (card_width + card_spacing), y_offset, card_width, card_height)
        if card_rect.collidepoint(mouse_pos):
            # Handle sylops card separately
            if card == "sylops.png":
                return "Sylops (0)"
            else:
                card_value = ""
                if card[0] == "r":
                    card_value = "-"
                elif card[0] == "g":
                    card_value = "+"
                card_value += card.split("_")[1]
                return card_value
    
    # Check if the mouse is over the discard pile
    if discard_rect.collidepoint(mouse_pos):
        if discard_pile:
            # Check if the top card in the discard pile is "sylops"
            if discard_pile[-1] == "sylops.png":
                return "Sylops (0)"
            else:
                top_card_value = ""
                if discard_pile[-1][0] == "r":
                    top_card_value = "-"
                elif discard_pile[-1][0] == "g":
                    top_card_value = "+"
                top_card_value += discard_pile[-1].split("_")[1]
                return top_card_value
        else:
            return "Empty discard pile"
    
    return None


def main():
    global round_counter
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('ITC Serif Gothic', 35)
    color = (255, 255, 255)
    color_light_blue = (100, 149, 237)
    color_dark_blue = (0, 0, 128)
    color_black = (0, 0, 0)

    button_x = WIDTH - 140 - 20
    button_y = HEIGHT - 60
    button_spacing = 20

    quit_button_clicked = False
    discard_rect = pygame.Rect((WIDTH - IMAGE_WIDTH * 2 - 20) // 2 + 120, 250, IMAGE_WIDTH, IMAGE_HEIGHT)
    selected_card_index = None
    switch_button_clicked = False  # Flag to track switch button click

    while run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    button_rect = pygame.Rect(button_x - i * (140 + button_spacing), button_y, 140, 40)
                    if button_rect.collidepoint(event.pos):
                        if i == 0:
                            start_function()
                        elif i == 1:
                            draw_function()
                        elif i == 2:
                            switch_button_clicked = True  # Flag to track switch button click
                        elif i == 3:
                            fold_function()

                new_button_rect = pygame.Rect(WIDTH - 120, 20, 100, 40)
                if new_button_rect.collidepoint(event.pos) and not quit_button_clicked:
                    quit_function()
                    quit_button_clicked = True

                if switch_button_clicked:  # Check if switch button is clicked
                    card_spacing = 20
                    card_width, card_height = IMAGE_WIDTH, IMAGE_HEIGHT
                    hand_width = len(player_hand) * card_width + (len(player_hand) - 1) * card_spacing
                    x_offset = (WIDTH - hand_width) // 2
                    y_offset = HEIGHT - 300
                    for i in range(len(player_hand)):
                        card_rect = pygame.Rect(x_offset + i * (card_width + card_spacing), y_offset, card_width, card_height)
                        if card_rect.collidepoint(event.pos):
                            selected_card_index = i
                            switch_function(selected_card_index)  # Call switch function with selected card index
                            switch_button_clicked = False  # Reset switch button clicked flag
                        else:
                            selected_card_index = None

        WIN.blit(BG, (0, 0))

        quit_button(WIN, font, 'Quit', WIDTH - 120, 20, (255, 0, 0), (200, 0, 0))

        round_text = font.render("Round: " + str(round_counter), True, color)
        WIN.blit(round_text, (20, 20))

        draw_button(WIN, font, 'Start', color, button_x, button_y, color_light_blue, color_dark_blue)
        for i, label in enumerate(["Draw", "Switch", "Fold"], start=1):
            draw_button(WIN, font, label, color, button_x - i * (140 + button_spacing), button_y, color_light_blue, color_dark_blue)

        display_hand(player_hand)
        display_dealer_hand(dealer_hand)
        display_deck()
        display_discard(discard_pile)

        hovered_card_player = detect_hover(mouse_pos, player_hand, (WIDTH - len(player_hand) * IMAGE_WIDTH - (len(player_hand) - 1) * 20) // 2, HEIGHT - 300, discard_rect, discard_pile)
        if hovered_card_player:
            if hovered_card_player == "discard_pile":
                if discard_pile:
                    text_render = font.render("Discard Pile: " + discard_pile[-1], True, color_black)
                else:
                    text_render = font.render("Empty discard pile", True, color_black)
            else:
                text_render = font.render(hovered_card_player, True, color_black)
            WIN.blit(text_render, (mouse_pos[0], mouse_pos[1] - 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

