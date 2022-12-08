with open("data.txt", "r") as f:

    splitLS = []
    lineBuffer = []
    parsedInfo = []
    file = f.read()

    lines = file.split("$ cd")

    count = lines.count(' ..\n')
    for line in range(count):
        lines.remove(' ..\n')

    for line in lines:
        line = line.split("$ ls\n")
        for part in line:
            pt = part.split("\n")
            for p in pt:
                if p == "":
                    pt.remove(p)
                if p != "":
                    idx = pt.index(p)
                    pt[idx] = p.split()
            lineBuffer.append(pt)
        splitLS.append(lineBuffer)
        lineBuffer = []

    for line in splitLS:
        obj = {
            "fileName": None,
            "ls": None
        }
        if len(line) > 1:
            obj["fileName"] = line[0][0]
            obj["ls"] = line[1]
            parsedInfo.append(obj)

    lsFileAndSize = []
    for obj in parsedInfo:
        fileAndSize = {
            "fileName": None,
            "size": 0,
            "dir": []
        }

        fileAndSize["fileName"] = obj["fileName"][0]
        for fileOrDir in obj["ls"]:
            if fileOrDir[0] != "dir":
                fileAndSize["size"] += int(fileOrDir[0])
            else:
                fileAndSize["dir"].append(fileOrDir[1])

        lsFileAndSize.append(fileAndSize)

    # for line in lsFileAndSize:
    #     print(line)

    lsFileAndSize2 = lsFileAndSize[:]

    count = 0
    ct = 0
    while True:
        if 175 != ct:
            print(ct)
            for obj in lsFileAndSize:
                if (len(obj["dir"]) == 0):
                    # if obj["size"] <= 100000:
                    count += obj["size"]
                    # else:
                    #     continue
                    # lsFileAndSize.remove(obj)
                    for ob in lsFileAndSize:
                        # print(ob["dir"])
                        # print(ob["dir"].count(obj["fileName"]))
                        if ob["dir"].count(obj["fileName"]):
                            ct += 1
                            id = lsFileAndSize.index(ob)
                            lsFileAndSize[id]["dir"].remove(obj["fileName"])
                            lsFileAndSize[id]["size"] += obj["size"]
        else:
            break
    
    print(count)

    count = 0
    lsNums = []
    for obj in lsFileAndSize:
        lsNums.append(int(obj["size"]))

    # print(lsNums)
    print(sum(lsNums))

    for num in range(len(lsNums)):
        nmMin = min(lsNums)
        count = + nmMin
        if nmMin >= 268_565:
            break
        lsNums.remove(nmMin)

    for line in lsFileAndSize:
        print(line)
    print(count)

    # 249919  18509
