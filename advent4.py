with open("data2.txt", "r") as f:
    file = f.read()
    lines = file.split("\n")
    count = 0
    for line in lines:
        line = line.split(",")
        line1 = line[0].split("-")
        line2 = line[1].split("-")
        x1, y1 = int(line1[0]), int(line1[1])
        x2, y2 = int(line2[0]), int(line2[1])
        
        # if ((x1 <= x2 and y1 >= y2) or (x1 >= x2 and y1 <= y2)):
        #     count += 1
        
        if ( (x1 <= x2 and x1 >= y2) or (x2 <= x1 and x2 >= y1) or (y1 >= x2 and y1 <= y2) or (y2 >= x1 and y2 <= y1)):
            count += 1
    print(count)