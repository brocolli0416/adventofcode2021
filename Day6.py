with open('day6.txt', 'r') as dat:
    fish_orig = list(dat.read().split(','))
    fish_orig[-1] = 1
    fish = [int(i) for i in fish_orig]
    #print(fish)

    day = 1
    while day <= 256:
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] = 6
                fish.append(8)
        day += 1
    print(len(fish))
