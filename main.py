import random
import os
import functions as fun

deck = ['w2','w3','w4','w5','w6','w7','w8','w9','w10','n2','n3','n4','n5','n6','n7','n8','n9','n10','n11','n12','n13','n14','m2','m3','m4','m5','m6','m7','m8','m9','m10','m11','m12','m13','m14','h2','h3','h4','h5','h6','h7','h8','h9','h10']
room = 0
game = 1
currentWeapon = ''
slain = ''
currentHealth = 20
potion = 0
handSize = 1
lowestSlain = 15
hand = []
card = '0'
ran = False
healedThisRoom = False

random.shuffle(deck)

while game == 1:
    os.system('cls')

    if handSize == 1 and len(deck) > 0:
        room += 1
        handSize = 4
        healedThisRoom = False
        hand = fun.roomHand(deck, hand, handSize)
    
    currentHealth = fun.getHealth(currentHealth, potion)
    currentWeapon = fun.getWeapon(currentWeapon, slain)

    print('Current Health:', currentHealth)
    print("Current Weapon:", currentWeapon)
    print("Enemies Slain:", slain)
    print()

    if currentHealth <= 0:
        input('Game Over...')
        game = 0
        break

    print("Room:", room)
    fun.roomMonsters(hand)
    fun.roomWeapons(hand)
    fun.roomHealth(hand)

    print()
    card, handSize, hand, deck, ran = fun.roomChoice(hand, handSize, deck, ran)

    if card[0] == 'h':
        if healedThisRoom == False:
            currentHealth = fun.getHealth(currentHealth, int(card[1:]))
            healedThisRoom = True
        else:
            input('You can only heal once per room! Discarding...')
    elif card[0] == 'w':
        currentWeapon = fun.getWeapon(int(card[1:]), currentWeapon)
        slain = ''
        lowestSlain = 15
    elif card[0] == 'n' or card[0] == 'm':
        currentHealth, usedWeapon = fun.combat(card, lowestSlain, currentHealth, currentWeapon)
        if usedWeapon == True:
            slain = fun.getSlain(slain, card[1:])
            lowestSlain = int(card[1:])

    if card != '0':
        hand.remove(card)

    if len(hand) == 0 and len(deck) == 0:
        input('You Win!')
        game = 0
        break