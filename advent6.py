with open("data3.txt", "r") as f:
    file = f.read()
    
    koef = 14
    for i in range(len(file)):
        strPar = file[i : i + koef]
        # print(strPar)
        # print(set(strPar))
        
        if (len(set(strPar)) == len(strPar)):
            print(i+koef)
            break