def bsearch(n_list,num):
    low = 0
    high = len(n_list) - 1
    while low!=high-1:
        mid = (low+high)//2
        if n_list[mid] == num:
            return 'Found'
        elif n_list[mid] > num:
            high = mid
        elif n_list[mid] < num:
            low = mid
    else:
        if n_list[low] == num or n_list[high]==num:
            return 'Found'
        else:
            return 'Not Found'
n_list = []
n = int(input('num'))
for i in range(n):
    temp_list = []
    for j in range(5):
        if j == 3:
            accession_num = int(input('int'))
            n_list.append(accession_num)
        else:
            temp_list.append(input('integer').rstrip())
num_search = int(input('int1'))
n_list.sort()
print(bsearch(n_list,num_search))
