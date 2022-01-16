import re
import numpy as np
with open('day5.txt', 'r') as dat:
    report_orig = dat.read().split('\n')
    report = [re.split(' -> |,', i) for i in report_orig]
    report = report[:-1]
    report = [[int(i) for i in line] for line in report]
    ground = np.array([[0]*2000]*2000)
    ############
    ## Part I ##
    ############
    for line in report:
        #print(line)
        x1 = line[0]
        x2 = line[2]
        y1 = line[1]
        y2 = line[3]
        if x1 == x2:
            y1 = min(line[1], line[3])
            y2 = max(line[1], line[3])
            for y in range(y1, y2+1):
                ground[x1][y] += 1
        elif y1 == y2:
            x1 = min(line[0], line[2])
            x2 = max(line[0], line[2])
            for x in range(x1, x2+1):
                ground[x][y1] += 1
        else:
            print(line)
            if y1 > y2:
                ymove = -1
            else:
                ymove = 1
            if x1 > x2:
                for x in range(x2, x1+1):
                    ground[x][y2] += 1
                    y2 -= ymove
                    #print(y2)
            else:
                for x in range(x1, x2+1):
                    ground[x][y1] += 1
                    y1 += ymove
            
    #print(ground[851][373])        
    print((ground > 1).sum())

        

