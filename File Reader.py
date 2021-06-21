# sum_all = 0
# result = open("number.txt")
# for nums in result:
#     sum_all += int(nums)
# print(sum_all)

print(sum([int(el) for el in open("number.txt")]))