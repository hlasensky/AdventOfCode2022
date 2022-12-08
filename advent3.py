import string
count = 0

with open("data.txt", "r") as f:
    file = f.read()
    lines = file.split("\n")
    for lineIndex in range(2, len(lines), 3):
        # ln = int(len(line)/2)
        # fHalf = line[:ln]
        # sHalf = line[ln:]
        # for letter in fHalf:
        #     findedLetter = sHalf.find(letter)
        #     if findedLetter != -1:
        #         lt = (sHalf[findedLetter])
        #         break 
        for letter in lines[lineIndex]:
            lt2 = lines[lineIndex - 1].find(letter)
            lt3 = lines[lineIndex - 2].find(letter)
            if lt2 != -1 and lt3 != -1:
                lt = lines[lineIndex - 1][lt2]

        ltNum = string.ascii_lowercase.find(lt)
        if ltNum  != -1:
            count += ltNum +1
        else:
            ltNum = (string.ascii_uppercase).find(lt)
            if ltNum != -1:
                count += (27 + ltNum)
        
    print(count)