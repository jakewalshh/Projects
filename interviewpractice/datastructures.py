

#Lists
"""
languages = [ "a", "b", "c"]


languages.insert(1, "e")
print(languages)


languages.remove(languages[3])
print(languages)


languages.remove("A")
print(languages)

sortedlanguage = languages.sort()
print(sortedlanguage)

languages.sort()
print(languages)

# Alternatively, use sorted() to create a new sorted list
sortedlanguage = sorted(languages)
print(sortedlanguage)

"""

"""
#Reverse a list not using reverse function

def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])

    return reversed_list
        

mylist = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(reverse_list(mylist))
"""
"""
#Tuples         --------- THEY ARE IMMUTABLE

def swap_first_last(myTuple):

    lst = list(myTuple)

    lst[0], lst[-1] = lst[-1], lst[0]

    return tuple(lst)




myTuple = (1,2,3,4,5)

print(swap_first_last(myTuple))

"""

#SETS

"""
numberset1 = {1,2,3,4,7,8,9}
numberset2 = {1,2,5,6}

print(numberset1.union(numberset2))
print(numberset1.intersection(numberset2))
print(numberset1.difference(numberset2))
"""

def remove_duplicates(lst):

    setVersionOfLst = set(lst)
    newLst =list(setVersionOfLst)
    return newLst

lst = [1,2,3,44,5,5,5,66,7,7,8,8,8,8,8,8,8,3,2,1,9]

print(remove_duplicates(lst))


