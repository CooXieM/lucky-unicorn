#ask if they have they played before
show_instructions = ''
while show_instructions.lower() != 'xxx':
    show_instructions = input('have you played this game before? ').lower()
        #if they say yes, output 'program continues'
    if show_instructions.lower() == 'yes'or show_instructions== 'y':
        print('program continues')   
    elif show_instructions == 'no' or show_instructions == 'n':
        print('display instructions')

        #if they say no, output 'display instructions'
    else:
        print('please answer yes / no')
