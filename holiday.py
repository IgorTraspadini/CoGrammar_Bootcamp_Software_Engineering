# Created by IgorCT - Dez_2024

# Calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car rental cost.


# Variables
print("########################################### Holiday Summary ###########################################")
city_flight = input("Please, inform the name of the city you will be flying to: ")
num_nights = int(input("The number of nights you'll staying at a hotel: "))
rental_days = int(input("The number of days for which you'll hiring a car: "))

# hotel_cost() function
def hotel_cost(nights):
  return 90 * nights

# car_rental() function
def car_rental(days):
  return 35 * days

# This function will take city_flight as an argument and return a cost for the flight.
def plane_cost(city_flight):
  # Dictionary with fligh prices by City
  city_flight_price = {"London": 150, 
                      "Roma": 50, 
                      "Netherlands": 30, 
                      "Lisbon": 60}
    
  if city_flight in city_flight_price.keys():
    return city_flight_price[city_flight]
  else:
    return 110

# Calculate the total cost of the holiday
def holiday_cost(city_flight_, num_nights_, rental_days_):
  return plane_cost(num_nights_) + car_rental(rental_days_) + plane_cost(city_flight_)

print(f"#################### Holiday in {city_flight} - cost report #######################")
print("")
print("Flight cost: ",plane_cost(city_flight))
print("Hotel cost: ",hotel_cost(num_nights))
print("Car rental cost: ",car_rental(rental_days))
print("")
print("Total cost: ",holiday_cost(city_flight, num_nights, rental_days))
print("###################################################################################")