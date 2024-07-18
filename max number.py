numbers = [2,4,65,7]
max_num = numbers[0]

for i in numbers[1:]:
    if i > max_num:
        max_num = i

print ("max number is ",max_num)