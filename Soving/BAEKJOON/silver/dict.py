import string
dic = dict()

alphabet = list(string.ascii_uppercase)
# for i in range(1, 27):
# #     dic[chr(i+64)] = i
# #
# # print(dic["Z"])

for a, b in enumerate(alphabet, start=1):
    dic[b] = a
print(dic)

# print(dic["창민이"])
print(list(i[1] for i in dic.items()))