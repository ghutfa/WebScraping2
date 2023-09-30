a=[10, 90, 67, 15, 6, 77]

# for i in a:
#     if i%3 ==0:
#         a = i**2
#         print(a)

abc = [i**2 for i in a if i%3 ==0]
print(abc)