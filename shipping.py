#This script checks for the cheapest cost to ship a certain weight through some
#invented costs 

weight = 1.5

#Ground Shipping
if weight <= 2:
  ground_shipping_cost = 20 + 1.5 * weight  
elif weight <= 6:
  ground_shipping_cost = 20 + 3.0 * weight
elif weight <= 10:
  ground_shipping_cost = 20 + 4.0 * weight  
else:
  ground_shipping_cost = 20 + 4.75 * weight    
print("Ground Shipping Price: $% .2f" %(ground_shipping_cost))

#Premium Ground Shipping
premium_ground_shipping_cost = 125

print("Premium Ground Shipping Price: $% .2f" %(premium_ground_shipping_cost))

#Drone Shipping
if weight <= 2:
  drone_shipping_cost = weight * 4.5
elif weight <= 6:
  drone_shipping_cost = weight * 9
elif weight <= 10:
  drone_shipping_cost = weight * 12
else:
  drone_shipping_cost = weight * 14.25

print("Drone Shipping Price: $% .2f" %(drone_shipping_cost))

print("The Cheapest method is $% .2f" %(min(drone_shipping_cost, premium_ground_shipping_cost, ground_shipping_cost)))
