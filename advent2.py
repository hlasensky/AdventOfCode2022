count = 0
me = 0
opponent = 0

# A = X - Rock lose
# B = Y - Paper draw
# C = Z - scissors win

def ifs(opponent, outCome):
    if (opponent == 1 and outCome == 1):
        return 3

    if (opponent == 2 and outCome == 1):
        return 1

    if (opponent == 3 and outCome == 1):
        return 2

    if (opponent == 1 and outCome == 3):
        return 2

    if (opponent == 2 and outCome == 3):
        return 3

    if (opponent == 3 and outCome == 3):
        return 1


with open("data.txt", "r") as f:
    nm = f.read()
    nm = nm.split("\n")
    for n in nm:
        switch={"A":1,"B": 2,"C": 3}
        opponent = switch.get(n[0])
        switch2={"X":1,"Y": 2,"Z": 3}
        me = switch2.get(n[2])

        # if (opponent == me):
        #     count += (3 + me)

        # if (opponent == 1 and me == 2):
        #     count += (6 + me)

        # if (opponent == 2 and me == 1):
        #     count += (0 + me)

        # if (opponent == 1 and me == 3):
        #     count += (0 + me)

        # if (opponent == 3 and me == 1):
        #     count += (6 + me)

        # if (opponent == 3 and me == 2):
        #     count += (0 + me)

        # if (opponent == 2 and me == 3):
        #     count += (6 + me)

        if (me == 2):
            count += (3 + opponent)

        if (me == 1):
            count += (0 + ifs(opponent, me))
        if (me == 3):
            count += (6 + ifs(opponent, me))
        
print(count)