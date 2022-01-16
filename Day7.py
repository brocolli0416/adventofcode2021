from statistics import mean, mode, median
with open('day7.txt', 'r') as dat:
    position_orig = list(dat.read().split(','))
    position_orig[-1] = '1392'
    position = [int(i) for i in position_orig]
    #print(position)
    ############
    ## Part I ##
    ############
    #position = [16,1,2,0,4,2,7,1,2,14]
    distances = {}
    for i in position:
        dis = abs(i - mean(position))
        distances[i] = dis 
    #center = min(distances, key = distances.get)
    center = int((mean(position)))
    def get_sum(n):
        return n*(n+1)//2
    sumlist = []
    for center in range(1900):
        sumlist.append(sum([get_sum(abs(i - center)) for i in position]))
    print(min(sumlist))
