def getHealth(currentHealth, potion):
    currentHealth += potion
    if currentHealth > 20:
        currentHealth = 20
    return currentHealth

def getWeapon(power, currentWeapon):
    currentWeapon = power
    return currentWeapon

def getSlain(slain, monster):
    if slain == '':
        slain += monster
    else:
        slain += ', ' + monster
    return slain

def roomHand(deck, hand, handSize):
        if hand == []:
            if len(deck) < handSize:
                handSize = len(deck)
            for n in range(handSize):
                hand += [deck[0]]
                deck.pop(0) 
        else:
            if len(deck) < handSize-1:
                handSize = len(deck)+1
            for n in range(handSize-1):
                hand += [deck[0]]
                deck.pop(0)
        return hand

def roomWeapons(hand):
    weapons = ''
    for item in hand:
        if str(item)[0] == 'w':
            if weapons != '':
                weapons += ', '
            weapons += str(item)[1:3] + '(' + str(hand.index(item)+1) + ')'
    if weapons != '':
        print('Weapons:', weapons)

def roomMonsters(hand):
    monsters = ''
    for item in hand:
        if str(item)[0] == 'm' or str(item)[0] == 'n':
            if monsters != '':
                monsters += ', '
            monsters += str(item)[1:3] + '(' + str(hand.index(item)+1) + ')'
    if monsters != '':
        print('Monsters:', monsters)

def roomHealth(hand):
    health = ''
    for item in hand:
        if str(item)[0] == 'h':
            if health != '':
                health += ', '
            health += str(item)[1:3] + '(' + str(hand.index(item)+1) + ')'
    if health != '':
        print('Health:', health)

def roomChoice(hand, handSize, deck, ran):
    choice = input('What will you do: ')

    if choice.isdigit():
        ran = False
        index = int(choice) - 1
        if 0 <= index < len(hand):
            card = hand[index]
            handSize -= 1
        else:
            input("Invalid Choice")
            return '0', handSize, hand, deck, ran
        
    elif choice == 'r' or choice == 'run':
        if handSize == 4 and ran == False and len(deck) != 0:
            deck.extend(hand)
            hand = []
            handSize = 1
            card = '0'
            ran = True
        elif handSize < 4:
            input('You can only run from a full room!')
            return '0', handSize, hand, deck, ran
        elif len(deck) == 0:
            input('There are no rooms left to run to!')
            return '0', handSize, hand, deck, ran
        else:
            input("You can't run two rooms in a row!")
            return '0', handSize, hand, deck, ran
    else:
        input('Invalid Choice')
        return '0', handSize, hand, deck, ran
    return card, handSize, hand, deck, ran

def combat(card, lowestSlain, currentHealth, currentWeapon):
    monster = int(card[1:])
    usedWeapon = False
    if monster < lowestSlain and currentWeapon != '':
        while True:
            method = input('Fight barehanded(1) or with weapon(2): ')
            if method == '1':
                currentHealth -= monster
                break
            elif method == '2':
                if currentWeapon < int(card[1:]):
                    damage = int(card[1:])-currentWeapon
                else:
                    damage = 0
                currentHealth -= damage
                usedWeapon = True
                break
            else:
                print('Invalid input. Try again.')
    else:
        currentHealth -= monster
    return currentHealth, usedWeapon