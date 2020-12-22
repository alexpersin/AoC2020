game_counter = 0

LOG = False
p = print
if not LOG:
    def print(*a):
        pass

def deal_game():
    with open("inputs/22", "r") as f:
        p1,p2 = f.read().split("\n\n")

    p1 = list(reversed([int(x.strip()) for x in p1.split('\n')[1:] if x]))
    p2 = list(reversed([int(x.strip()) for x in p2.split('\n')[1:] if x]))

    return p1, p2

def play_game(p1, p2, game_counter):
    previous_rounds = set()
    roundn = 1
    print(f"=== Game {game_counter} ===")
    while p1 and p2:
        print(f"-- Round {roundn} (Game {game_counter}) --")
        print(f"Player 1's deck: {list(reversed(p1))}")
        print(f"Player 2's deck: {list(reversed(p2))}")

        h = tuple(p1 + ["|"] + p2)
        if h in previous_rounds:
            return '1'
        previous_rounds.add(h)

        a, b = p1.pop(), p2.pop()
        print(f"Player 1 plays: {a}")
        print(f"Player 2 plays: {b}")

        if len(p1) >= a and len(p2) >= b:
            print("Playing a sub game to determine the winner...")
            winner = play_game(p1[len(p1)-a:], p2[len(p2)-b:], game_counter+1)
            print(f"...anyway, back to game {game_counter}.")
        else:
            winner = '1' if a > b else '2'
        print(f"Player {winner} wins round {roundn} game {game_counter}")
        winner_card, loser_card = (a, b) if winner == '1' else (b, a)

        if winner == '1':
            p1.insert(0, winner_card)
            p1.insert(0, loser_card)
        else:
            p2.insert(0, winner_card)
            p2.insert(0, loser_card)
        roundn += 1
    winner = '1' if p1 else '2'
    print(f"The winner of game {game_counter} is player {winner}!")
    return winner

p1, p2 = deal_game()
play_game(p1, p2, 1)

p(f"=== Post-game results ===")
p(f"Player 1's deck: {list(reversed(p1))}")
p(f"Player 2's deck: {list(reversed(p2))}")

winning_deck = p1 or p2
score = 0
for i, card in enumerate(winning_deck):
    score += (i+1) * card
p(f"Part 2: {score}")
