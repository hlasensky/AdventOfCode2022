with open("data2.txt", "r") as f:
    file = f.read()
    lines = file.split("\n")
    lsDups = []

    for idx in range(1, len(lines)-1):
        highL1 = int(lines[idx][0])
        highL2 = int(lines[idx][-1])
        highR1 = int(lines[0][idx])
        highR2 = int(lines[-1][idx])

        for nmIndex in range(1, len(lines[idx])-1):
            if int(lines[idx][nmIndex]) > int(lines[idx][nmIndex - 1]) and int(lines[idx][nmIndex]) > int(highL1):
                lsDups.append([idx, nmIndex])
                highL1 = int(lines[idx][nmIndex])

            if int(lines[nmIndex][idx]) > int(lines[nmIndex-1][idx]) and int(lines[nmIndex][idx]) > int(highR1):
                lsDups.append([nmIndex, idx])
                highR1 = int(lines[nmIndex][idx])

        for nmIndex in range(2, len(lines[idx])-1):
            if int(lines[idx][-nmIndex]) > int(lines[idx][-nmIndex + 1]) and int(lines[idx][-nmIndex]) > int(highL2):
                lsDups.append([idx, len(lines[0]) - nmIndex])
                highL2 = int(lines[idx][-nmIndex])

            if int(lines[-nmIndex][idx]) > int(lines[-nmIndex + 1][idx]) and int(lines[-nmIndex][idx]) > int(highR2):
                lsDups.append([len(lines[0]) - nmIndex, idx])
                highR2 = int(lines[-nmIndex][idx])

    for i in lsDups:
        if lsDups.count(i) > 1:
            lsDups.remove(i)
    for i in lsDups:
        if lsDups.count(i) > 1:
            lsDups.remove(i)
    for i in lsDups:
        if lsDups.count(i) > 1:
            lsDups.remove(i)
            
    print(len(lsDups) + (2 * len(lines) + 2 * len(lines[0]) - 4))
    # print(lsDups)
    
    maxView = 0
    for treeCoordinates in lsDups:
        tree = lines[treeCoordinates[0]][treeCoordinates[1]]
