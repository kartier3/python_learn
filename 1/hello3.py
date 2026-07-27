data = set('Hello')
print(data)

data1 = {1, 2, 3, 4, 5, 6}
data1.add(32)

print(data1)

nums=[1, 2, 3, 4, 5, 5]
nums=set(nums)
new_data= frozenset(nums)

print(nums)

def test_fun(word):
    print("This is a test function" , end="")
    print(word)

test_fun(4)

def min(L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min

nums1=[ 5,2,3,7,123]

min_value = min(nums1)
print("The minimum number is: ", min_value)

func = lambda x: x * 2
result = func(5)
print(result)