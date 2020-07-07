from random import choice


class RockPaperScissors:

    result_to_display_score_mapping = {
                                 'win': {'display': 'Well done. Computer chose {} and failed', 'score': 100},
                                 'draw': {'display': 'There is a draw ({})', 'score': 50},
                                 'lose': {'display': 'Sorry, but computer chose {}', 'score': 0}
                                 }

    player_commands = ['!exit', '!rating']

    # win_scenario = {'rock': 'scissors',
    #                 'paper': 'rock',
    #                 'scissors': 'paper'}

    def __init__(self):
        self.option = ''
        self.computer_option = ''
        self.player_rating = 0
        self.player_name = ''
        self.winner_index = []
        self.computer_options = ['rock', 'paper', 'scissors']
        self.game_valid_words = set(self.computer_options + self.player_commands)

    def display_result(self, result):
        print(self.result_to_display_score_mapping.get(result)['display'].replace('{}', self.computer_option))

    def win_scenario(self):
        option_index = self.computer_options.index(self.option)
        count_of_winner = int((len(self.computer_options) - 1) / 2)
        return [option_index - i if option_index - i >= 0
                else option_index - i + len(self.computer_options)
                for i in range(1, count_of_winner + 1)]

    def determine_option(self):
        self.computer_option = choice(self.computer_options)
        if self.option == self.computer_option:
            self.player_rating += self.result_to_display_score_mapping.get('draw')['score']
            return 'draw'
        elif self.computer_options.index(self.computer_option) in self.win_scenario():
            self.player_rating += self.result_to_display_score_mapping.get('win')['score']
            return 'win'
        else:
            return 'lose'

    def display_player_rating(self):
        print('Your rating: {}'.format(self.player_rating))

    def determine_valid_words(self):
        if self.option not in self.game_valid_words:
            print('Invalid input')
            return False
        if self.option == '!exit':
            print('Bye!')
            exit(0)
        if self.option == '!rating':
            self.display_player_rating()
            return False
        return True

    def greet_player(self):
        self.player_name = input('Enter your name:')
        print('Hello, {}'.format(self.player_name))

    def set_player_rating(self):
        file = open('rating.txt', 'r')
        ratings_if_available = [line.split()[1] for line in file if line.split()[0] == self.player_name]
        file.close()
        return 0 if not ratings_if_available else int(ratings_if_available[0])

    def fetch_player_options(self):
        player_options = input()
        if player_options:
            self.computer_options = player_options.split(',')
        print("Okay, let's start")

    def play(self):
        self.greet_player()
        self.player_rating = self.set_player_rating()
        self.fetch_player_options()
        while True:
            self.option = input()
            if self.determine_valid_words():
                result = self.determine_option()
                self.display_result(result)


rps = RockPaperScissors()
rps.play()
