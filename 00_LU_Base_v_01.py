#function goes here
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

#main routine goes here
played_before = yes_no('have you played the game before? ')
print('You chose {}'.format(played_before))
print()
having_fun = yes_no('are you having fun? ')
print('you said {} to having fun'.format(having_fun))

if played_before == 'no':
    print('display instructions')
else:
    print('program continues')
def instructions() :
    print('**** How To Play ****')
    print()
    print('The Rules Of The Game Go Here')
    print()
    return ''
if played_before =='no':
    instructions()
    print('Program Continues')
error = 'please enter a whole number between 1 and 10\n'
valid = False
while not valid:
    try:
        #ask the question
        response = int(input('how much would you like to play with? '))
        #if the amount is too low / too high give
        if 0 < response <= 10:
            print('you have asked to play with ${}'.format(response))
        #output an error
        else:
            print(error)
    except ValueError:
        print(error)
#functions go here
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
#main routine goes here
how_much = num_check('how much would you like to play with? ', 0, 10)
print ('you will be spending ${}'.format(how_much))
#print the