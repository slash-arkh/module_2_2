c = 0
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while my_list[c] >= 0:
   if my_list[c] == 0:
      c += 1
      continue
   print(my_list[c])
   c += 1
