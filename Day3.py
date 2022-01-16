with open('day3.txt', 'r') as dat:
    ############
    ## Part I ##
    ############
    report_orig = dat.read().split('\n')
    report = [list(i) for i in report_orig]
    report = report[:-1]
    reportlen = len(report)
    #print(len(report[0]))
    new_report = []
    for i in range(len(report[0])):
        newlist = []
        for j in report:            
            newlist.append(int(j[i]))
        new_report.append(newlist)
    gamma = []
    epsilon = []
    for x in new_report:
        if sum(x) > reportlen/2:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)
    #print(int(gamma,2)*int(epsilon,2))

    ############
    ## Part I ##
    ############
    orig_report = report
    def vertical(report, position): # Creates a vertical report of this position
        vertical_report = []
        for command in report:            
            vertical_report.append(int(command[position]))
        return vertical_report

    def most_common(vertical_report): # Find the most commond digit in this vertical report
        length = len(vertical_report)
        if sum(vertical_report) >= length/2: # If there is more one than zero
            return '1'
        else:
            return '0'
    def least_common(vertical_report): # Find the most commond digit in this vertical report
        length = len(vertical_report)
        if sum(vertical_report) >= length/2: # If there is more one than zero
            return '0'
        else:
            return '1'
    
    report = orig_report
    print(len(report))
    for position in range(len(report[0])): # For this position in each command line:
        vertical_report = vertical(report, position) # Create a vertical report
        print("Vertical", vertical_report)
        digit = most_common(vertical_report)
        print("Digit", digit)
        report = [command for command in report if command[position] == digit]
        print("Position: ", position, " Length: ", len(report))
        if len(report) == 1:
            print(report[0])
            gen_rating = "".join(report[0])
            gen_rating = int(gen_rating, 2)
            break

    report = orig_report
    print(len(report))
    for position in range(len(report[0])): # For this position in each command line:
        vertical_report = vertical(report, position) # Create a vertical report
        digit = least_common(vertical_report)
        report = [command for command in report if command[position] == digit]
        #print(len(report))
        if len(report) == 1:
            print(report[0])
            scrub_rating = "".join(report[0])
            scrub_rating = int(scrub_rating, 2)
            break
    
    print(gen_rating)
    print(scrub_rating)
    print(gen_rating*scrub_rating)