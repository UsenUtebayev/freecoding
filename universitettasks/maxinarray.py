

def sort_max(listofint):
    for j in range(len(listofint)):
        for i in range(len(listofint) - 1):
            if i == len(listofint):
                continue
            else:
                if listofint[i] < listofint[i + 1]:
                    temp = listofint[i]
                    listofint[i] = listofint[i + 1]
                    listofint[i + 1] = temp


x = [55, 66, 99, 66, 41, 54, 36, 54, 11, 1066]
sort_max(x)
print(x)
