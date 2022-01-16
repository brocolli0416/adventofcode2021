with open('day8.txt', 'r') as dat:
    ############
    ## Part I ##
    ############
    lines_orig = dat.read().split('\n')
    lines = [i.split(' ') for i in lines_orig]
    lines = lines[:-1]
    outputs = [i[-4:] for i in lines]
    count = 0
    #print('max', len(outputs)*4)
    for line in outputs:
        #count += sum(map(lambda x: len(x) == 3 or len(x) == 4 or len(x) == 2 or len(x) == 8, line))
        count += sum(1 for x in line if len(x) == 3 or len(x) == 4 or len(x) == 2 or len(x) == 7)
    #print(count)

    #############
    ## Part II ##
    #############
    for i in lines:
        i.remove('|')
    one = []
    four = []
    seven = []
    eight = []
    twothreefive = []
    zerosixnine = []
    for line in lines:
        for i in line:
            if len(i) == 2:
                one.append(i)
            elif len(i) == 3:
                seven.append(i)
            elif len(i) == 4:
                four.append(i)
            elif len(i) == 7:
                eight.append(i)
            elif len(i) == 5:
                twothreefive.append(i)
            else:
                zerosixnine.append(i)
        


