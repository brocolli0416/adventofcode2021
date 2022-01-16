import numpy as np
with open('day15.txt', 'r') as dat:
    ############
    ## Part I ##
    ############
    report_o = dat.read().split('\n')
    report_o = report_o[:-1]
    report_o = [int(i) for i in report_o]
    report_o = [[int(i) for i in str(row)] for row in report_o]
    report = np.array(report_o)
    #print(report[0][5])
    x_length = len(report_o[0])
    y_length = len(report_o)
    print(x_length)
    print(y_length)
    right = x_length-1
    down = y_length-1
    risk = 0
    while right > 0 or down > 0:
        try:
            nextx = report[down+0][right-1]
            nexty = report[down-1][right+0]
            if nextx < nexty:
                risk += nextx
                right -= 1
                down += 0
            else:
                risk += nexty
                right += 0
                down -= 1
            print(right, down)
        except:
            if right == 0:
                down -= 1
                right += 0
                risk += report[down][right]
            elif down == 0:
                down += 0
                right -= 1
                risk += report[down][right]
            print(right, down)
    print(risk)

