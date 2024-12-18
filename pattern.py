# Created by IgorCT - Dez_2024

# variable
count_rev = 5

for i in range(1,10):
  if i < 6:
    print(i*"*")
  else:
    count_rev -= 1
    print(count_rev*"*")
