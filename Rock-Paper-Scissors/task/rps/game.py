

class RockPaperScissors:

    def __init__(self, option):
        self.option = option

    def determine_option(self):
        computer_option = ''
        if self.option == 'scissors':
            computer_option = 'rock'
        elif self.option == 'paper':
            computer_option = 'scissors'
        elif self.option == 'rock':
            computer_option = 'paper'
        print('Sorry, but computer chose {comp_choice}'.format(comp_choice=computer_option))

    def play(self):
        self.determine_option()


rps = RockPaperScissors(input())
rps.play()
