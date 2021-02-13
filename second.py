# #Shart operatorlari
# #1
# number = int(input('son:'))
# if number > 0:
#     print(number+1)
# else:
#     print(number)
#
# #2
# number = int(input('son'))
# if number > 0:
#     print(number+1)
# elif number < 0:
#     print(number-2)
# elif number == 0:
#     print(number + 10)
#
# #4-5
# number_1 = int(input('son'))
# number_2 = int(input('son'))
# number_3 = int(input('son'))
# print("3 sonimiz:" , number_1, number_2, number_3, end="")
#
# x = 0
# if number_1 > 0:
#     x+=1
# if number_2 > 0:
#     x+=1
# if number_3 > 0:
#     x +=1
#
# y = 0
# if number_1 < 0:
#     x+=1
# if number_2 < 0:
#     x+=1
# if number_3 < 0
#     x+=1
# print("3 ta son orasida:",x,"ta musbat son bor")
# print("3 ta son orasida:",y,"ta manfiy son bor")

# import random
# a = random.randrange(-2, 20)
# b = random.randrange(-2, 20)
# print("a,b",a,b)
# if a > b:
#     _max = a
# else:
#     _max = b
# print("2 sonimiz o'rtasidagi eng katta son:",_max)

# import random
# a = random.randrange(-2, 10)
# b = random.randrange(-2, 10)
# print ("a,b", a,b)
# if a < b:
#     _min = a
# else:
#     _min = b
# print("2 sonimiz o'rtasidagi eng kichkina son:",_min)

# import random
# a = random.randrange(-1, 10)
# b = random.randrange(-1, 9)
# print ("a,b", a,b)
# if a > b:
#     print(a,b)
# else:
#     print(b,a)

# import random
# a = random.randrange(-10, 8)
# b = random.randrange(-10, 5)
# print("a,b",a,b)
# if a > b:
#     a,b = b,a
# print(a,b)

#10

# import random
# a = random.randrange(-10,10)
# b = random.randrange(-10, 10)
# print("a,b",a,b)
# if a!=b:
#     a = b = a+b
# else:
#     a = b = 0
# print(a,":",b)

# import random
# a = random.randrange(-10, 8)
# b =random.randrange(-10, 9)
# print("a,b", a,b)
# if a != b:
#     a =b = max(a,b)
# else:
#     a= b = 0
# print("a:",a,"b",b)


# import random
# a = random.randrange(-19 ,10)
# b = random.randrange(-12, 6)
# c = random.randrange(-4, 8)
# print("a,b,c", a,b,c)
# if a < b:
#     n = a
# else:
#     n = b
#
# if n > c:
#     n = c
# print("min:", n)
# print(min(a,b,c))

# import random
# a = random.randrange(-19, 10)
# b = random.randrange(6, 13)
# c = random.randrange(5, 25)
# print(a,b,c)
# if (a <= b and b <= c) or (c <= b and b <= a):
#     n = b
# elif (b <= a and a <= c) or (c <= b and a <= b):
#     n = a
# elif (a <= c and c <= b) or (b <= c and c <= a):
#     n = c
# print("O'rtacha son:", n)


# import random
# a = random.randrange(-19, 10)
# b = random.randrange(6, 13)
# c = random.randrange(5, 25)
# x = 0
# if a < b:
#     x = a
# else:
#     x = b
# y = 0
# if a > b:
#     x = b
# else:
#     x = a
#
# print("3ta son ichidagi eng kichkin son:",x,"ga teng")
# print("3ta son ichidagi eng katta son:",y,"ga teng")

# import random
# a = random.randrange(-11, 10)
# b = random.randrange(6, 19)
# c = random.randrange(1, 15)
# print("a,b,c",a,b,c)
# if (a >= b and a <= c):
#     n = a
# elif (b >= a and b <= c):
#     n = b
# elif (c >= b and c <= a):
#     n = c
# else:
#     n = a = b = c
#
# print(min(a,b,c),max(a,b,c))





