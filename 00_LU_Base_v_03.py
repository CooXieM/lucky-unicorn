# Functions go here 

# checks that a respones is yes / no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            response = 'yes'
            return response
        elif response == 'no' or response == 'n':
            response = 'no'
            return response
        else:
            print ('please answer yes / no') 

# checks for numbers between low and high
def num_check(question, low, high):
    error = 'please enter a whole number between 1 and 10\n'
    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))
            #if the amount is too low / too high give
            if low < response <= high:
                return response
            #output an error
            else:
                print(error)
        except ValueError:
            print(error)

# Displays instructions, returns ''
def instructions() :
    print('**** How To Play ****')
    print()
    print('The Rules Of The Game Go Here')
    print()
    return ''

# Main routine goes here

played_before = yes_no('have you played the game before? ')

if played_before =='no':
    instructions()
else:
    print('Program Continues')

how_much = num_check('how much would you like to play with? ', 0, 10)
print ('you will be spending ${}'.format(how_much))