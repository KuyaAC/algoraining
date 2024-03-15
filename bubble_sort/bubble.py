
list = [3,1,25,23,28,4,5]

def bubble(list):
    indexing_lenth = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range (0, indexing_lenth):
            if list[i] >  list[i+1]:
                sorted =  False
                list[i], list[i+1] = list[i+1], list[i]
    return list;

print(bubble(list))

