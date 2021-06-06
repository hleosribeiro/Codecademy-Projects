# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
#convert damages function
def convert_damages():
  new_damages = []
  for damage in damages:
    if damage[-1] in conversion:
      new_damages.append(float(damage[:-1]) * conversion[damage[-1]])
    else:
      new_damages.append(damage)
  return new_damages

#converted damages
damages = convert_damages()

#create hurricane dict by name
def create_hurr_by_name_dict():
  data_dict = {name:{"Month": month, "Year": year, "Max Sustained Wind": max_wind, "Areas Affected": area_affected, "Deaths": death_n, "Damage": damage} for (name, month, year, max_wind, area_affected, death_n, damage) in zip(names, months, years, max_sustained_winds, areas_affected, deaths, damages)}
  return data_dict

#hurricane by name dictionary
hurr_by_name_dict = create_hurr_by_name_dict()

#create hurricane by year dict
def create_hurr_by_year_dict(hurr_by_name):
  names = []
  months = []
  years = []
  max_winds = []
  area_affected = []
  deaths = []
  damages = []
  for hurr in hurr_by_name:
    names.append(hurr)
    months.append(hurr_by_name[hurr]["Month"])
    years.append(hurr_by_name[hurr]["Year"])
    max_winds.append(hurr_by_name[hurr]["Max Sustained Wind"])
    area_affected.append(hurr_by_name[hurr]["Areas Affected"])
    deaths.append(hurr_by_name[hurr]["Deaths"])
    damages.append(hurr_by_name[hurr]["Damage"])
  return {year: {"Month": month, "Max Sustained Wind": max_wind, "Name": name, "Areas Affected": area, "Deaths": death, "Damage": damage} for (year, month, max_wind, name, area, death, damage) in zip(years, months, max_winds, names, area_affected, deaths, damages)}

#hurricane by year dict
hurr_by_year_dict = create_hurr_by_year_dict(hurr_by_name_dict)

#number of occurrences by area function
def ocurrences_by_area_dict(hurr_dict):
  ocurrences_dict = {}
  for hurr in hurr_dict:
    for area in hurr_dict[hurr]["Areas Affected"]:
      if area not in ocurrences_dict:
        ocurrences_dict[area] = 1
      else:
        ocurrences_dict[area] += 1
  return ocurrences_dict

#number of occurrences by area
number_by_area = ocurrences_by_area_dict(hurr_by_year_dict)

#function highest ocurrences of hurricanes
def highest_ocurrences(number_dict):
  highest = 0
  highest_area = ""
  for each in number_dict:
    if number_dict[each] > highest:
      highest = number_dict[each]
      highest_area = each
  return (highest_area, highest)

#highest occurrence
highest_occ = highest_ocurrences(number_by_area)

#mortality scale
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

#function to calculate highest deaths and name
def highest_deaths(hurr_dict):
  highest = 0
  highest_name = ""
  for hurr in hurr_dict:
    if hurr_dict[hurr]["Deaths"] > highest:
      highest = hurr_dict[hurr]["Deaths"]
      highest_name = hurr
  return (highest_name, highest)

#tuple containing name and deaths of the highest deaths hurricane
highest_death = highest_deaths(hurr_by_name_dict)

#making dictionary classifying hurricanes by mortality scale
hurr_by_mort_scale = {}

for hurr in hurr_by_name_dict:
  for number in sorted(list(range(5)), reverse=True):
    if hurr_by_name_dict[hurr]["Deaths"] >= mortality_scale[number]:
      hurr_by_mort_scale[hurr] = number
      break
#hurr_by_mortscale created

#creating hurricanes by damage scale
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

hurr_by_dmg_scale = {}

for hurr in hurr_by_name_dict:
  for number in sorted(list(range(5)), reverse=True):
    if type(hurr_by_name_dict[hurr]["Damage"]) == float:
      if float(hurr_by_name_dict[hurr]["Damage"]) >= damage_scale[number]:        
        hurr_by_dmg_scale[hurr] = number
        break
