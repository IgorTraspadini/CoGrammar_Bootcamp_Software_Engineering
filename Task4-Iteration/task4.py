# Created by IgorCT - Dez_2024

# Objective: Write a program to find and print the sum of numbers from 1 to 100 that are divisible by 3.

# using While loop
count = 1
sum_ = 0
while count <= 100:
  if count % 3 == 0:
    sum_ += count
  count += 1
print("Sum of numbers from 1 to 100 that are divisible by 3.")
print(sum_)

# using For loop
sum_ = 0
for i in range(1, 101):
  if i % 3 == 0:
    sum_ += i
print("Sum of numbers from 1 to 100 that are divisible by 3.")
print(sum_)

