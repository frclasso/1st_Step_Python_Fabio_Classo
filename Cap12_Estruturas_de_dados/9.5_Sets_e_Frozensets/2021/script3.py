# unificando listas com valores repetidos usando set()

nums_1 = [1,2,3,4,5,6]
nums_2  =[4,5,6,7,8,9,10]
nums_3 = [6,8,8,10,11,12]

def unifying_lists(*args):

    return list(set().union(*args))

print(unifying_lists(nums_1, nums_2, nums_3))
