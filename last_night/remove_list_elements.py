def remove_equal_index(list1, list2):
# cecks if a index value in list1 is equal in list2, and, if it is, creates a new list 'remove_list' with the value in list2
    remove_list = []
    aux = 0
    while aux < len(list1):
        print(list1[aux], list2[aux])
        if list1[aux] != list2[aux]:
            remove_list.append(list1[aux])
        aux = aux+1
    print(remove_list)
def remove_equal_values(list1, list2):
#check if a value in list one exist in list 2 and creates a list named non_redundant_list with the values that are in list1 but not in list2'''
    aux = 0
    non_redundant_list = []
    while aux < len(list1):
        if list1[aux] not in list2:
            non_redundant_list.append(list1[aux])
        aux = aux + 1
    print(non_redundant_list)
