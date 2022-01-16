with open('day2.txt', 'r') as dat:
    ############
    ## Part I ##
    ############
    commands_orig = dat.read().split('\n')
    commands = [i.split(' ') for i in commands_orig]
    commands = commands[:-1]
    depth = 0
    position = 0
    for i in commands:
        if i[0] == 'down':
            depth += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
        elif i[0] == 'forward':
            position += int(i[1])
    print(depth*position)

    ############
    ## Part I ##
    ############ 
    depth = 0
    position = 0
    aim = 0
    for i in commands:
        if i[0] == 'down':
            aim += int(i[1])
        elif i[0] == 'up':
            aim -= int(i[1])
        elif i[0] == 'forward':
            position += int(i[1])
            depth += aim*int(i[1])
    print(depth*position)