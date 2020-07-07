from random import choice


class RockPaperScissors:

    result_to_display_mapping = {'win': 'Well done. Computer chose {} and failed',
                                 'draw': 'There is a draw ({})',
                                 'lose': 'Sorry, but computer chose {}'}

    options = ['rock', 'paper', 'scissors']

    win_scenario = {'rock': 'scissors',
                    'paper': 'rock',
                    'scissors': 'paper'}

    def __init__(self, option):
        self.option = option
        self.computer_option = ''

    def display_result(self, result):
        print(self.result_to_display_mapping.get(result).replace('{}', self.computer_option))

    def determine_option(self):
        self.computer_option = choice(self.options)
        if self.option == self.computer_option:
            return 'draw'
        elif self.win_scenario.get(self.option) == self.computer_option:
            return 'win'
        else:
            return 'lose'

    def play(self):
        result = self.determine_option()
        self.display_result(result)


rps = RockPaperScissors(input())
rps.play()
