# Created by IgorCT - Dez_2024

# variables
namely_swimming_time = 0
cycling_time = 0
running_time = 0
total_time = 0
award = ""

print("################ Award calculation #################")
# user input values
namely_swimming_time = int(input("Please, inform your namely Swimming time (minutes): "))
cycling_time = int(input("Please, inform your Cycling time (minutes): "))
running_time = int(input("Please, inform your namely Running time (minutes): "))
total_time = namely_swimming_time + cycling_time + running_time

# display total time
print(f"Your total time: {total_time}")

# award calculation
if total_time in range(0, 101):
  award = "Honorary colours!"
elif total_time in range(101, 106):
  award = "Honorary half colours!"
elif total_time in range(106, 111):
  award = "Honorary scroll."
else:
  award = "No award :("  

print(f"Award: {award}")


