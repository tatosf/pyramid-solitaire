import random

# O(1) - Constant runtime 
f= open ('asciiArt.txt','r')

#Creating Player Class
# Time Complexity O(1)

class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0

# Make Cards Algorithm 
# Creating the hash map using inbuilt python dict
# Time Complexity - O(n^2) -> since there are 2 nested for loops, its O(n^2 + m^2) which can be simplified to O(n^2)
    
def make_cards(cards, special_cards):
    hash_map = {}
    for card in cards:
        for num in range(2,11):
            hash_map[(str(num) + card)] = num
          
    for special_card in special_cards:
      for card in cards:
        hash_map[special_card + card] = special_cards[special_card]
    # print(card_lst)
    return hash_map

  
# Creating the card deck -> Starting deck and stock deck

# Time complexity -> O(n*m) - n because it's a Linear runtime since we are only looping through all the keys in the hashmap once and appending it to the list)
# m  because the python random.shuffle() function has an average linear complexity as its the Fisher-Yates algorithm)

def create_deck(deck):
  all_cards = []
  for c in full_deck:
    all_cards.append(c)
  random.shuffle(all_cards)
  starting_deck = all_cards[:28]
  stock_deck = all_cards[28:]
  
  return starting_deck, stock_deck


# Function to compare the cards chosen by the user
  
#Time complexity - O(n) since we are mostly conducting constant operations which are O(1) since we are directly accessing the hash map values by the index. However, the for loop has to iterate through the deck items and the worst case and average case is O(n).
  
def comparisn(card1, card2, full_deck, rows, decks, deck, stock_deck, score):
  if full_deck[card1] + full_deck[card2] == 13:
    score += 10
    full_deck[card1] = "**"
    full_deck[card2] = "**"

    for i in range(len(deck)):
      if card1 in deck[i]:
          deck[i] = '**'
      if card2 in deck[i]:
          deck[i] = '**'
    if card1 in stock_deck:
      current = random.shuffle(deck)
    if card2 in stock_deck:
      current = random.shuffle(deck)
    rows = [deck[0],deck[1:3],deck[3:6],deck[6:10],deck[10:15],
    deck[15:21],deck[21:28]] 

  else:
    return 0
    
  return rows, score

# Function to get user input
  
# Time Complexity - O(n^2) since we are continously in a while loop and have a nested for loop. Nested linear loops here result in the time complexity being O(n^2)
  
def get_user_input(deck, stack_last_element, full_deck):
  score = 0
  rows = [deck[0],deck[1:3],deck[3:6],deck[6:10],deck[10:15],\
    deck[15:21],deck[21:28]] 
  flag = False
  
  while not flag:
    card1 = input("Please select the first card: ").upper()
    if full_deck[card1] == 13:
      score += 10
      game.score = score
      
     #compare_king(card1, full_deck, rows, decks, deck, decks[1])
      full_deck[card1] = "**"
      for i in range(len(deck)):
        if card1 in deck[i]:
            deck[i] = '**'
        #if card1 in stock_deck:
        #  current = random.shuffle(deck)
      rows = [deck[0],deck[1:3],deck[3:6],deck[6:10],deck[10:15],
        deck[15:21],deck[21:28]] 
      print_pyramid(rows,stack_last_element)
     
      flag = True
      return card1
    else:
      card2 = input("Please select the second card: ").upper()
    
    if card1 in rows[6] or card1 in stack_last_element and card2 in rows[6] or card2 in stack_last_element:
      compared = comparisn(card1, card2, full_deck, rows, decks, deck, decks[1], score)
      game.score += compared[1]
      print_pyramid(compared[0],stack_last_element)
      flag = True
    else:
      print('Please enter values only from the last row')
      print(rows[6])
  return card1, card2 

  
  # Time complexity O(n+1): eache time it is returning 1 card more to make the pyramid
def print_pyramid(deck,current1):
  for n in range(1):
      
      print()
  print()
  print("       ",decks[0][0])
  print("     ",decks[0][1],decks[0][2])
  print("    ",decks[0][3],decks[0][4],decks[0][5])
  print("   ",decks[0][6],decks[0][7],decks[0][8],decks[0][9])
  print("  ",decks[0][10],decks[0][11],decks[0][12],decks[0][13],decks[0][14])
  print(" ",decks[0][15],decks[0][16],decks[0][17],decks[0][18],decks[0][19],decks[0][20])
  print("",decks[0][21],decks[0][22],decks[0][23],decks[0][24],decks[0][25],decks[0][26],\
  decks[0][27],"     ","Stock/Waste - ", current1)
  

  return current1


# Simple function to give user the menu options
# Time Complexity - O(1) since its just printing a statement at constant time. 
  
def menu():
    print('\n\nSelect 1 to Compare 2 cards.\nSelect 2 to shuffle the stock deck. \nSelect 3 to end the game.\n')


# Function to add the user scores to the score.txt file.
  
# Time Complexity - O(1) since we are just opening a file which is a constant operation and appending values to the file, which is also a constant operation. 
  
def add_score(name, score):
  # Open a file with access mode 'a'
  with open("score.txt", "a") as file_object:
      # Append 'hello' at the end of file
      file_object.write(f"{name} {score}\n")


# Sorting algorithm Function
# Time Complexity Analysis - 
# For loop 1 - O(n) since we visit each line and split by space
# For loop 2 - O(m) since we visit each value and remove \n characters
# For loop 3 - O(k^2) since for each value in sorted values, we loop k times
# For loop 4 - O(p) since we are visiting each element in the dictionary hence linear. 

    
def sorting_algo():
  # we make this to order the all time rankings of players based on their scores
# Initially used mergesort algorithm to do the sorting along with the data extraction from score.txt, which has average and best case complexity of O(nlogn), but python's sorted function uses the TimSort algorithm which has best case O(n) and average case O(nlogn) hence we used the python sorted() function 
  
  lines = []
  scoring_sys = {}
  with open('score.txt') as f:
    lines += f.readlines()
    #print(lines)
    for i in lines:
      i = i.split(' ')
      scoring_sys[i[0]] = i[1]
    #print(scoring_sys)
    for i in scoring_sys:
      scoring_sys[i] = scoring_sys[i].rstrip('\n')
    #print(scoring_sys)
    sorted_values = sorted(scoring_sys.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in scoring_sys.keys():
            if scoring_sys[k] == i:
                sorted_dict[k] = scoring_sys[k]
    print("The all time rankings are as follows:")
    for i in sorted_dict:
      print(i, sorted_dict[i])
      # i = i[1].rstrip('/n')

# Choices function
# Time Complexity: O(n) -> Linear runtime complexity as we keep asking continously for the choices as long as the game is on. 
      
def choices(choice,print1):
  flag = False
  while not flag:
    flag = True
    if choice == 1:
      get_user_input(decks[0],print1, full_deck)
      return print1
      #flag = True
    elif choice == 2:
      # shuffle stock deck
      print('Shuffling stock deck')
      current = decks[1].pop()
      return current
      
      # have to make the function
      #flag = True
    elif choice == 3:
      print(f" The game has ended, your score is {game.score}")
      add_score(game.name, game.score)
      sorting_algo()
      exit() 
      #flag = True
    else:
      print('Please enter options only from 1-3')
      flag = False
  return 0
  

cards = ["C","S","D","H"]
special_cards = {"A":1,"J":11,"Q":12,"K":13}

full_deck = make_cards(cards, special_cards)  

decks = create_deck(full_deck)

current = decks[1].pop()


print(''.join([line for line in f]))
name = input('Please enter your name: ')
game = Player(name)
print(f" Your current score is {game.score} ")



while True:
  print_pyramid(decks,current)
  menu()
  choice = int(input())
  current= choices(choice,print_pyramid(decks,current))

