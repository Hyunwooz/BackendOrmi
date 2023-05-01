
my_strings = ["He11oWor1d","Program29b8UYP"]
overwrite_strings = ["lloWorl","merS123"]
ss = [2,7]

n = 0

for str in range(0,2):
  
  my_string = my_strings[n]
  overwrite_string = overwrite_strings[n]
  s = ss[n] 
  
  str = list(my_string)

  for i in overwrite_string :
    str[s] = i
    s += 1

  answer = "".join(str)

  print(answer)
  n +=1