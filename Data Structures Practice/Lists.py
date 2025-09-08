my_list = [5, 2, 46, 59, 91, 2, 32, 62, 76, 24]
print(my_list[0])
print(my_list[-1])
print(my_list[int(len(my_list))//2])
my_list.append(93)
my_list[2] = 99

for i in my_list:
    if i % 2 == 0:
        print(i)