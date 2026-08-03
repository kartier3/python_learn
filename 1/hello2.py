
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

data = (1, 2, 3, 4, 5)
# data[0] = 10  # This would cause an error since tuples are immutable
print(data[1:4])

nums = [1, 2, 3, 4, 5]
new_nums = tuple(nums)
print(new_nums)

count = {'code' : 'IE', 'name' : 'Irelandd', 'population' : 5000000} 
print(count['code'])
print(count['name'])
print(count['population'])

for key, value in count.items():
    print(key, ' - ', value)


person = {
    'user_1' : {
        'first_name' : 'John',
        'last_name' : 'Doe',
        'age' : 30
    },
    'user_2' : {
        'first_name' : 'Jane',
        'last_name' : 'Smith',
        'age' : 25
    }
}

print(person['user_1']['last_name'])

