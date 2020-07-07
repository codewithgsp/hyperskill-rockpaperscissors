from random import choice


class RockPaperScissors:

    result_to_display_mapping = {'win': 'Well done. Computer chose {} and failed',
                                 'draw': 'There is a draw ({})',
                                 'lose': 'Sorry, but computer chose {}'}

    computer_options = ['rock', 'paper', 'scissors']
    game_valid_words = set(computer_options + ['!exit'])

    win_scenario = {'rock': 'scissors',
                    'paper': 'rock',
                    'scissors': 'paper'}

    def __init__(self, option):
        self.option = option
        self.computer_option = ''

    def display_result(self, result):
        print(self.result_to_display_mapping.get(result).replace('{}', self.computer_option))

    def determine_option(self):
        self.computer_option = choice(self.computer_options)
        if self.option == self.computer_option:
            return 'draw'
        elif self.win_scenario.get(self.option) == self.computer_option:
            return 'win'
        else:
            return 'lose'

    def determine_valid_words(self):
        if self.option not in self.game_valid_words:
            print('Invalid input')
            return False
        if self.option == '!exit':
            print('Bye!')
            exit(0)
        return True

    def play(self):
        if self.determine_valid_words():
            result = self.determine_option()
            self.display_result(result)


while True:
    user_choice = input()
    rps = RockPaperScissors(user_choice)
    rps.play()
