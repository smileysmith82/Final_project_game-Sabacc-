import pygame
from deck_and_hand import Card, Deck, Hand, Dice, Player_Actions

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sabacc")

IMAGE_WIDTH, IMAGE_HEIGHT = 100, 133 # resolution of card images

BG = pygame.transform.scale(pygame.image.load("Green_background.jpg"), (WIDTH, HEIGHT)) # Load background image

pygame.init()

round_counter = 0

def load_image(card):
    if card.rank == 12:
        image_path = "up_backside"
    elif card.rank == 11:
        image_path = "down_backside"
    elif card.rank == 0:
        image_path = "sylops"
    elif card.rank > 0:
        image_path = f"g_{card.rank}_{card.suit.lower()[0]}"
    elif card.rank < 0:
        image_path = f"r_{abs(card.rank)}_{card.suit.lower()[0]}"

    image_path += ".png"
    image = pygame.image.load(image_path)
    if card.rank == 0:
        return pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT * 2))
    else:
        return pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

    image_path += ".png"  # Include the file extension for all other cards
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

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

def display_deck(front_of_card):
    main_deck_back_image = load_image(front_of_card)
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
    
def end_game(player1_hand, player2_hand):
    player1_total = self.Hand.player1_hand()
    player2_total = self.Hand.player2_hand()
    
    winner_text = ""
    if player1_total < player2_total:
        winner_text = "You Win!"
    elif player1_total > player2_total:
        winner_text = "You Lose!"
    else:
        winner_text = "It's a tie!"

    total_text_player1 = f"Your total: {player1_total}"
    total_text_player2 = f"Dealer's total: {player2_total}"

    return winner_text, total_text_player1, total_text_player2

def quit_function():
    print("Quitting")
    pygame.quit()
    
def stand_function():
    print("stand")

def draw_function():
    print("Draw")

def switch_function(selected_card_index, hand):
    global discard_pile, player1_hand
    if selected_card_index is not None and len(hand.discard_pile) > 0 and 0 <= selected_card_index < len(hand.player1_hand):
        selected_card = hand.player1_hand[selected_card_index]
        hand.player1_hand[selected_card_index] = hand.discard_pile.pop()
        hand.discard_pile.append(selected_card)
        turn = "player2"

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
            if card.rank == 0:
                return "Sylops (0)"
            else:
                card_value = ""
                if card.rank < 0:
                    card_value = "-"
                elif card.rank > 0:
                    card_value = "+"
                card_value += str(abs(card.rank))
                return card_value
    
    # Check if the mouse is over the discard pile
    if discard_rect.collidepoint(mouse_pos):
        if discard_pile:
            if discard_pile[-1].rank == 0:
                return "Sylops (0)"
            else:
                top_card_value = ""
                if discard_pile[-1].rank < 0:
                    top_card_value = "-"
                elif discard_pile[-1].rank > 0:
                    top_card_value = "+"
                top_card_value += str(abs(discard_pile[-1].rank))
                return top_card_value
        else:
            return "Empty discard pile"
    
    return None

def main():
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck.shuffled_deck)
    hand.starting_deal(2)
    player1 = hand.player1_hand
    player2 = hand.player2_hand
    turn = "Player1"
    discard_pile = hand.discard_pile
    back_of_card = Card('11', '_')
    front_of_card = Card('12', '_')
    dealer_back_hand = [back_of_card, back_of_card]
    
    global card_images
    card_images = {card: load_image(card) for card in hand.discard_pile + hand.player1_hand + dealer_back_hand} # Load card images

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
                for i in range(5):
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
                        elif i == 4:
                            stand_function()

                new_button_rect = pygame.Rect(WIDTH - 120, 20, 100, 40)
                if new_button_rect.collidepoint(event.pos) and not quit_button_clicked:
                    quit_function()
                    quit_button_clicked = True

                if switch_button_clicked:  # Check if switch button is clicked
                    card_spacing = 20
                    card_width, card_height = IMAGE_WIDTH, IMAGE_HEIGHT
                    hand_width = len(hand.player1_hand) * card_width + (len(hand.player1_hand) - 1) * card_spacing
                    x_offset = (WIDTH - hand_width) // 2
                    y_offset = HEIGHT - 300
                    for i in range(len(hand.player1_hand)):
                        card_rect = pygame.Rect(x_offset + i * (card_width + card_spacing), y_offset, card_width, card_height)
                        if card_rect.collidepoint(event.pos):
                            selected_card_index = i
                            switch_function(selected_card_index, hand)  # Call switch function with selected card index
                            switch_button_clicked = False  # Reset switch button clicked flag
                        else:
                            selected_card_index = None

        WIN.blit(BG, (0, 0))

        quit_button(WIN, font, 'Quit', WIDTH - 120, 20, (255, 0, 0), (200, 0, 0))
        
        round_text = font.render(f"Round: {round_counter}", True, color)
        WIN.blit(round_text, (20, 20))

        draw_button(WIN, font, 'Start', color, button_x, button_y, color_light_blue, color_dark_blue)
        for i, label in enumerate(["Draw", "Switch", "Fold", "Stand"], start=1):
            draw_button(WIN, font, label, color, button_x - i * (140 + button_spacing), button_y, color_light_blue, color_dark_blue)

        display_hand(hand.player1_hand)
        display_dealer_hand(dealer_back_hand)
        display_deck(front_of_card)
        display_discard(discard_pile)

        hovered_card_player = detect_hover(mouse_pos, hand.player1_hand, (WIDTH - len(hand.player1_hand) * IMAGE_WIDTH - (len(hand.player1_hand) - 1) * 20) // 2, HEIGHT - 300, discard_rect, hand.discard_pile)
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
        if round_counter >= 4:
            winner_text, total_text_player1, total_text_player2 = end_game(player1_hand, player2_hand)
            winner_render = font.render(winner_text, True, (255, 0, 0))
            total_render_player1 = font.render(total_text_player1, True, (255, 0, 0))
            total_render_player2 = font.render(total_text_player2, True, (255, 0, 0))

            # Display winner and totals on the screen
            WIN.blit(winner_render, (WIDTH // 2 - winner_render.get_width() // 2, HEIGHT // 2 - 60))
            WIN.blit(total_render_player1, (WIDTH // 2 - total_render_player1.get_width() // 2, HEIGHT // 2))
            WIN.blit(total_render_player2, (WIDTH // 2 - total_render_player2.get_width() // 2, HEIGHT // 2 + 60))

            pygame.display.flip()

            # Wait for the player to quit the game
            while True:
                mouse_pos = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Check if the quit button is clicked
                        if WIDTH - 120 < event.pos[0] < WIDTH - 20 and 20 < event.pos[1] < 60:
                            print("quitting")
                            run = False
                            break

                # Check if the quit button is hovered over
                quit_button_rect = pygame.Rect(WIDTH - 120, 20, 100, 40)
                if quit_button_rect.collidepoint(mouse_pos):
                    quit_button(WIN, font, 'Quit', WIDTH - 120, 20, (255, 0, 0), (255, 100, 100))  # Change color if hovered
                else:
                    quit_button(WIN, font, 'Quit', WIDTH - 120, 20, (255, 0, 0), (200, 0, 0))  # Reset to default color

                pygame.display.flip()
                
                if not run:
                    break

            if not run:
                break

    pygame.quit()

if __name__ == "__main__":
    main()

