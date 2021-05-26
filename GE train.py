#This script calculates some values related to physical properties of a moving train
#It is supposed to be practice in defining functions and calling functions

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  temp = (f_temp - 32) * 5/9
  return temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  temp = c_temp * (9/5) + 32
  return temp

c0_in_fahrentheit = c_to_f(0)
print(c0_in_fahrentheit)

#Use the force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies %i Newtons of force" %(train_force))

def get_energy(mass, c = 3*10**8):
  return mass * (c ** 2)

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies %i Joules." %(bomb_energy))

#Do the Work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does %i Joules of work over %i meters." %(train_work, train_distance))
