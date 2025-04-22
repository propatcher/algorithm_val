import math
import random
def FindLargest(array1):
    largest = array1[0] # O(1)
    for i in range(len(array1)): #O(n)
        if array1[i] > largest:
            largest = array1[i]
    return largest #O(1)
    # in sum O(1 + n + 1) = O(2+n)
    
def ContainsDuplicates(array2):
    for i in range(len(array2)):
        for j in range(i + 1, len(array2)):
            if array2[i] == array2[j]:
                return True
    return False # O(n^2)

def DividingPoint(array3):
    number1 = array3[0]
    number2 = array3[-1]
    number3 = array3[5]
    
    if number1 > number2 and number1 < number3:
        return number1
    elif number2 > number1 and number2 < number3:
        return number2
    else:
        return number3
    
def GCD(a,b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a    

def FindFactors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    i = 3
    max_factor = math.isqrt(number)
    while i <= max_factor:
        while number % i == 0:
            factors.append(i)
            number //= i
            max_factor = math.isqrt(number)
        i += 2
    if number > 1:
        factors.append(number)
    return factors

def deal_cards(players, cards_per_player=5):
    deck = shuffle_deck(generate_deck()) #????не работает generate_deck нужно задать изначально O(n) или O(2**n)????
    hands = [[] for _ in range(players)] # перебор игроков в виде пустоты см. _
    
    for card_num in range(cards_per_player):
        for player in range(players):
            if not deck:
                raise ValueError("Мало карт")
            hands[player].append(deck.pop())
    
    return hands
"""
def deal_cards(players, cards_per_player=5):
    deck = shuffle_deck(generate_deck())
    hands = []
    
    for player in range(players):                                                        #Идёт раздача по 5 карт сразу на человека
        hand = deck[player * cards_per_player : (player + 1) * cards_per_player]
        hands.append(hand)
    
    return hands
"""
def MonteCarlo(target, num_rolls): #соответственно чем больше бросков тем точнее результат
    successes = 0
    for _ in range(num_rolls): #Перебор в количество бросков
        roll = random.randint(1, 6) #cлучайное значение между 1 и 6
        if roll == target: #если бросок который нам нужен к успешным добавляется один соответственно 
            successes += 1
    return successes / num_rolls #успешные броски делятся на сумму всех бросков и получается вероятность по методике Монте Карло