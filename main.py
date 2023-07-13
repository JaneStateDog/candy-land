import random
from enum import Enum

class T(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    ORANGE = 5
    PURPLE = 6

    GINGER_BREAD = 7
    CANDY_CANE = 8
    GUMDROP = 9
    PEANUT = 10
    LOLIPOP = 11
    ICE_CREAM = 12

BOARD = [
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE, # skip 1
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.GINGER_BREAD,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.CANDY_CANE,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW, # skip 2
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.GUMDROP,
    T.BLUE,
    T.ORANGE,
    T.GREEN, # skip 2 leave
    T.RED, # licorice
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE, # skip 1 leave
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.PEANUT,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE, # licorice
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.LOLIPOP,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.ICE_CREAM,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW, # licorice
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
    T.PURPLE,
    T.YELLOW,
    T.BLUE,
    T.ORANGE,
    T.GREEN,
    T.RED,
]

SKIPS = [
    (4, 57),
    (33, 43),
]

LICORICE = [
    44,
    84,
    115,
]

class C(Enum):
    BLUE = 1
    BLUE_DOUBLE = 2
    RED = 3
    RED_DOUBLE = 4
    PURPLE = 5
    PURPLE_DOUBLE = 6
    YELLOW = 7
    YELLOW_DOUBLE = 8
    ORANGE = 9
    ORANGE_DOUBLE = 10
    GREEN = 11
    GREEN_DOUBLE = 12

    GINGER_BREAD = 13
    CANDY_CANE = 14
    GUMDROP = 15
    PEANUT = 16
    LOLIPOP = 17
    ICE_CREAM = 18

DECK_TEMPLATE = {
    C.BLUE: 8,
    C.BLUE_DOUBLE: 2,
    C.RED: 8,
    C.RED_DOUBLE: 2,
    C.PURPLE: 8,
    C.PURPLE_DOUBLE: 2,
    C.YELLOW: 8,
    C.YELLOW_DOUBLE: 2,
    C.ORANGE: 8,
    C.ORANGE_DOUBLE: 2,
    C.GREEN: 8,
    C.GREEN_DOUBLE: 2,

    C.GINGER_BREAD: 1,
    C.CANDY_CANE: 1,
    C.GUMDROP: 1,
    C.PEANUT: 1,
    C.LOLIPOP: 1,
    C.ICE_CREAM: 1,
}

UNSHUFFLED_DECK = []
for key, value in DECK_TEMPLATE.items():
    for _ in range(value):
        UNSHUFFLED_DECK.append(key)

def shuffle(unshuffled_deck):
    deck = []
    for card in unshuffled_deck:
        deck.append(card)

    random.shuffle(deck)

    return deck

def m_print(text):
    if False:
        print(text)

GAMES_TO_RUN = 100
games_data = []

PLAYER_COUNT = 4

def strat_1(position):
    return list(T)[random.randint(0, len(list(T)) - 1)]

def strat_2(position):
    results = {}
    for tile in list(T):
        end_position = 0
        for pos in range(position, len(BOARD)):
            if BOARD[pos] == tile:
                end_position = pos

                for skip in SKIPS:
                    if pos == skip[0]:
                        end_position = skip[1]
                        break
                
                if pos in LICORICE:
                    end_position = 0
                    
                break

        results[tile] = end_position

    best = T.BLUE # BLUE for default as always, poggies
    for key, value in results.items():
        if value > results[best]:
            best = key

    return best

for game_number in range(GAMES_TO_RUN):
    players = [ -1 for _ in range(PLAYER_COUNT) ] # All players start at position -1 (off the board)

    deck = shuffle(UNSHUFFLED_DECK)

    lost_turn = {}

    turn = 0
    is_game_running = True
    while is_game_running:
        turn += 1

        for player_number in range(len(players)):
            if player_number in lost_turn:
                if lost_turn[player_number]:
                    lost_turn[player_number] = False
                    continue

            player_guess = strat_2(players[player_number])
            m_print(f"Player {player_number} is guessing it will be a {player_guess.name} card")

            if len(deck) == 0:
                deck = shuffle(UNSHUFFLED_DECK)
            card = deck.pop(0)
            m_print(f"Player {player_number} drew a {card.name} card")

            amount = 2
            if card == C.BLUE_DOUBLE: card = C.BLUE
            elif card == C.RED_DOUBLE: card = C.RED
            elif card == C.PURPLE_DOUBLE: card = C.PURPLE
            elif card == C.YELLOW_DOUBLE: card = C.YELLOW
            elif card == C.ORANGE_DOUBLE: card = C.ORANGE
            elif card == C.GREEN_DOUBLE: card = C.GREEN
            else:
                amount = 1

            space_to_find = T.BLUE # I guess BLUE will be the default
            for tile_type in list(T):
                if card.name == tile_type.name:
                    space_to_find = tile_type

            if player_guess != space_to_find:
                m_print(f"Player {player_number} guessed wrong")
                continue
            else:
                m_print(f"Player {player_number} guessed right!")

            for i in range(amount):
                found_space = False
                for position in range(players[player_number] + 1, len(BOARD)):
                    if BOARD[position] == space_to_find:
                        m_print(f"Player {player_number} moved to the {space_to_find.name} space at position {position}")
                        players[player_number] = position

                        for skip in SKIPS:
                            if position == skip[0]:
                                m_print(f"Player {player_number} got to skip to position {skip[1]}!")
                                players[player_number] = skip[1]

                                break
                        
                        if position in LICORICE:
                            m_print(f"Player {player_number} got stuck in licorice for a turn")
                            lost_turn[player_number] = True

                        found_space = True
                        break

                if not found_space and (
                    space_to_find != T.GINGER_BREAD and
                    space_to_find != T.CANDY_CANE and
                    space_to_find != T.GUMDROP and
                    space_to_find != T.PEANUT and
                    space_to_find != T.LOLIPOP and
                    space_to_find != T.ICE_CREAM
                ):
                    m_print(f"Player {player_number} won the game at turn {turn}!")
                    games_data.append(turn)

                    is_game_running = False
                    break

            if not is_game_running:
                break

average = 0
for turns in games_data:
    average += turns
average /= GAMES_TO_RUN
print(f"The average amount of turns per game is {average}!")