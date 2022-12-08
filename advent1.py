ls = []
ls2 = []
count = 0
cnt = 0
with open("data.txt", "r") as f:
    nm = f.read()
    nm = nm.split("\n")
    for number in nm:
        if number == "":
            ls.append(count)
            count = 0
        else:
            count += int(number)
print(max(ls))

max1 = max(ls)
ls.remove(max1)
max2 = max(ls)
ls.remove(max2)
max3 = max(ls)

print(max1+max2+max3)