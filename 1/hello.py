print("Hello",7,6,2, sep=" ");
  


input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

print("The power of input 1 raise to input 2 is:", int(input1) ** int(input2));
print("hello input 1 is:", str(input1));5


if input2 > 4:
    print("input 2 is bigger than 4");

del input2;

happy = True
if happy:
    print("I am happy");
elif input1 == 0:
    print("I am neutral");
else:
    print("I am sad");

if happy & input1 > 0:
    print("I am happy and input 1 is positive");


data = input("Enter a string Five: ")

number = 5 if data == "Five" else 0
print("the number is:",number);
count = 0
word ="Hello World"
char = input("Enter a character to check if it is in the string:")
for i in word:
    if i == char:
        print("Yes")
        count += 1
    elif i != " ":
        print("No")

print(count)


i = 16

while i > 0:
    print(i)
    i -= 1
    if i ==1:
        break
    if i % 2 == 0:
        continue


print("The loop has ended.")