# Created by IgorCT - Dez_2024

# Objective: You're building a simple checkout system for an e-commerce store. 
# When a customer checks out, they need to enter their age, total order price, and account balance. 
# The system will categorise them into an age group and apply a discount if they qualify. 
# Then it will check if the balance is sufficient to complete the purchase, taking into account any applicable discounts.

#. Steps to Implement:
#  Take User Inputs:
#    a. Get the customer's age, total order price, and account balance.
#  Categorise Age and Apply Discount:
#    a. If the customer is aged 18-25, apply a 10% discount.
#    b. If the customer is aged 26-60, apply a 5% discount.
#    C. If the customer is under 18 or over 60, no discount is applied.
#  Calculate Discounted Price:
#    a. Adjust the total order price based on the applicable discount.
#  Check Balance:
#    a. Compare the customer's account balance with the discounted price.
#    b. If the balance is enough, proceed with the order.
#    c. If the balance is insufficient, calculate the shortfall and inform the user.


print("")
print("####################### Welcome to Checkout System ##############################")
print("")
discount = 1
# input variables
age = int(input("Enter your age?: "))
total_ordering = float(input("Enter your total order price: "))
account_balance = float(input("Enter your account balance: "))

# Categorise Age and Apply Discount:
if age in range(18,26):
  discount = .90
elif age in range(26, 61):
  discount = .95

# Calculate Discounted Price:
total_order_after_discount = total_ordering * discount 

# Check Balance:
if account_balance >= total_order_after_discount:
  print("Your order is complete. Thank you for shopping with us!")
else:
  shortfall = total_order_after_discount - account_balance
  print(f"Insufficient balance! Your shortfall is: -${shortfall}")
  
