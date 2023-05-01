
str1 = "aaaaa"
str2 = "bbbbb"

str1_list = list(str1)
str2_list = list(str2)

answer = ""

for i in range(0,len(str1)):
  answer += str1_list[i] + str2_list[i]


print(answer)