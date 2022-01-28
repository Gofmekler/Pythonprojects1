#Black Jack


import random
import sys
Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)
Backside = "Backside"


def main():
    print("RULES...")
    money = 5000
    while True:
        if money <= 0:
            print("You're broke")
            sys.exit()
        print("Money: ", money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        print("bet: ", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)
            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(" bet increased to {}".format(bet))
                print("Bet", bet)
            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}".format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ("S", "D"):
                break
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("DEALER HITS")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                input("press enter to continue")
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print("dealer busts, you win ${}".format(bet))
            money += (bet * 2)
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost")
            money -= bet
        elif playerValue > dealerValue:
            print("you won ${}".format(bet))
            money += (bet * 2)
        elif playerValue == dealerValue:
            print("Tie, bet is returned")
            print('\n\n')


def getBet(maxBet):
    while True:
        print("How much do you bet? (1-{}, or type \'Quit\')".format(maxBet))
        bet = input('> ').upper().strip()
        if bet == "Quit":
            print("Thanks for playing")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (Hearts, Diamonds, Spades, Clubs):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("Dealer: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("Dealer: ???")
        displayCards([Backside] + dealerHand[1:])

    print("Player: ", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == Backside:
            rows[1] += ' |## | '
            rows[2] += ' |###| '
            rows[3] += ' |_##|'
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, ' '))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble Down')
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


if __name__ == '__main__':
    main()
