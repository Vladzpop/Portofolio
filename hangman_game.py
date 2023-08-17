import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.guessed_letters = set()
        self.remaining_guesses = 6
        self.current_player = ""
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)

    def select_word(self):
        self.word = random.choice(self.word_list).lower()

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(display)

    def guess_letter(self, player_name, letter):
        if letter in self.guessed_letters:
            print("Ai ghicit deja această literă")
        else:
            self.guessed_letters.add(letter)
            if letter in self.word:
                print("Ai ghicit!")
                if self.check_win():
                    print("Felicitări!, {}! Ai câștigat!".format(player_name))
                    return
            else:
                print("Nu ai ghicit!")
                self.remaining_guesses -= 1
                if self.remaining_guesses == 0:
                    print("Finalul jocului! Ai rămas fără încercări. Cuvântul era:", self.word)
                    return
        self.display_word()

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True


# Word list for the game
words = ["dinozaur", "calculator", "farfurie", "tatuaj", "jocuri", "scaun", "televizor", "scrumieră", "pizza", "hanorac"]

# Create a Hangman game instance
game = HangmanGame(words)

print("Bine ați venit la Spânzurătoarea!")

# Add players
num_players = int(input("Câți jucători sunt?: "))
for i in range(1, num_players + 1):
    player_name = input("Cum te cheama, jucător {}?: ".format(i))
    game.add_player(player_name)

# Select a word
game.select_word()

game.display_word()

# Game loop
while True:
    for player in game.players:
        print("Este rândul lui \n{}".format(player))
        letter = input("Ghicește:").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Comandă invalidă.Te rog să scrii o singură literă.")
            continue

        game.guess_letter(player, letter)
