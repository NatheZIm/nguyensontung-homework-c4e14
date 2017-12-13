def get_even_list(ds):
    lists=[]
    even=[]
    for i in range(len(ds)):
        lists.append(ds[i])
        if lists[i] % 2 == 0:
            even.append(lists[i])
    return even

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
