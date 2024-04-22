# flatten list function
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]

def flattenList(l):
    flatten = []
    for i in l:
        if isinstance(i, type([])):
            flatten.extend(flattenList(i))
        else:
            flatten.append(i)  
    return flatten

inputList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(f'Flatten list : \n{flattenList(inputList)}\n')


# reverse list function
#input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

def reverseList(l):
    newList = []
    l.reverse()
    for item in l:
        if isinstance(item, type([])):
            item.reverse()
            newList.append(item)
        else:
           newList.append(item)
    return newList

willReverse = [[1, 2], [3, 4], [5, 6, 7]]
print(f'Reversed list: \n{reverseList(willReverse)}')
