import random

stages = [
    '''
     ------
     |    |
     |    
     |   
     |   
     |   
     |   
    ------
    ''',

    '''
     ------
     |    |
     |    O
     |   
     |   
     |   
     |   
    ------
    ''',

    '''
     ------
     |    |
     |    O
     |    |
     |   
     |   
     |   
    ------
    ''',

    '''
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ------
    ''',

    '''
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |   
    ------
    ''',

    '''
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
     |   
    ------
    ''',

    '''
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ------
    '''
]


fruits = ["Apple", "Watermelon", "Cherry", "Banana", "Grapes", "Pineapple", "Strawberry",
         "Orange", "Blueberry", "Mango", "Peach", "Pear", "Kiwi", "Papaya", "Pomegranate",
         "Avocado", "Lemon", "Lime", "Coconut", "Raspberry", "Blackberry", "Cantaloupe",
         "Honeydew", "Tangerine", "Guava", "Passionfruit", "Dragonfruit", "Lychee",
         "Fig", "Apricot", "Plum", "Cranberry"]
animals = ["Elephant", "Giraffe", "Kangaroo", "Crocodile", "Alligator", "Hippopotamus",
           "Rhinoceros", "Squirrel", "Chipmunk", "Porcupine", "Ostrich", "Penguin",
           "Flamingo", "Peacock", "Platypus", "Koala", "Panda", "Armadillo", "Wombat",
           "Antelope", "Chameleon", "Cheetah", "Jaguar", "Panther", "Leopard", "Lion",
           "Tiger", "Zebra", "Otter", "Ocelot", "Meerkat", "Walrus", "Narwhal", "Dolphin"]

category = input("Do you want to play with fruits or animals? ").lower()
if category == "fruits":
    chosen_word = random.choice(fruits).lower()
elif category == "animals":
    chosen_word = random.choice(animals).lower()
else:
    print("Invalid choice. Starting with fruits by default.")
    chosen_word = random.choice(fruits).lower()

print(f"Your word has {len(chosen_word)} letters")
numbers_of_letters = len(chosen_word)
the_word = "_" * numbers_of_letters
print(the_word)

game_over = False
corrects_words = []
lives = 0

while not game_over:
    print(stages[lives])
    choice = input("Guess a letter of the word\n").lower()

    if choice in chosen_word:
        if choice not in corrects_words:
            corrects_words.append(choice)
    else:
        lives += 1
        print("Wrong choice!")
        if lives == 6:
            game_over = True
            print("\nYou lose!")
            print("The correct word was", chosen_word)
            print(stages[6])
            break
    display = ""
    for letter in chosen_word:
        if letter in corrects_words:
            display += letter
        else:
            display += "_"

    print(display)

    if display == chosen_word:
        game_over = True
        print("You win")
