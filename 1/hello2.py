
nums = [1, 2, 3, 4, 5, [1,2]]
for num in nums:
    print(num)

print(nums)
nums[0] = 50
nums[4] = 1
print(nums)
print(nums[-1][1])

nums.append(6)
print(nums)


n = input("enter a lenght of a list: ")
n = int(n)
 
list1=[]
i = 0
for i in range (n):
    element = input("enter an element "+    str(i+1)+ ": ")
    list1.append(element)
    print(list1)


print("The list is: ", list1);