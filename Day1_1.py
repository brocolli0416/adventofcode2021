with open('1-1.txt', 'r') as dat:
    ############
    ## Part I ##
    ############
    contents = dat.read().split('\n')
    contents = contents[:-1]
    contents = [int(i) for i in contents]
    print(len(contents))
    increase = 0
    for c, x in enumerate(contents[0:-1]):
        if x < contents[c+1]:
            increase += 1

    print(increase)
    
    #############
    ## Part II ##
    #############
    increase_list = []
    for i in range(2,len(contents)):
        print(i)
        sum = contents[i-2] + contents[i-1] + contents[i-0]
        increase_list.append(sum)
        
    print(len(increase_list))

    sum_increase = 0
    for c, x in enumerate(increase_list[0:-1]):
        if x < increase_list[c+1]:
            sum_increase += 1

    print(sum_increase)
    print(contents[:15])
    print(increase_list[:10])


        

