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
