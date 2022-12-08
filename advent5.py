#                         [Z] [W] [Z]
#         [D] [M]         [L] [P] [G]
#     [S] [N] [R]         [S] [F] [N]
#     [N] [J] [W]     [J] [F] [D] [F]
# [N] [H] [G] [J]     [H] [Q] [H] [P]
# [V] [J] [T] [F] [H] [Z] [R] [L] [M]
# [C] [M] [C] [D] [F] [T] [P] [S] [S]
# [S] [Z] [M] [T] [P] [C] [D] [C] [D]
#  1   2   3   4   5   6   7   8   9
with open("data2.txt", "r") as f:
    file = f.read()
    lines = file.split("\n")
    count = 0
    boxes = ["SCVN",
             "ZMJHNS",
             "MCTGJND",
             "TDFJWRM",
             "PFH",
             "CTZHJ",
             "DPRQFSLZ",
             "CSLHDFPW",
             "DSMPFNGZ"]

    ln = []
    for line in lines:
        line = line.split()
        ln.append([line[1], line[3], line[5]])

    print(boxes)
    for move in ln:
        coont = int(move[0])
        letters = (boxes[int(move[1])-1])[-coont:]
        boxes[int(move[1])-1] = boxes[int(move[1])-1][:-coont]
        boxes[int(move[2])-1] = boxes[int(move[2])-1] + letters
            
        # boxes[int(move[2])-1] = boxes[int(move[2])-1] + boxes[int(move[1])-1][-int(move[0]):-1]
        # boxes[int(move[1])-1] = boxes[int(move[1])-1].replace(boxes[int(move[1])-1][-int(move[0]):-1], "")
    print(boxes)
    for l in boxes:
        print(l[-1], end="")
   

# CNSZFDVLJ