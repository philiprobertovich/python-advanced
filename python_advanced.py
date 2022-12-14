from faker import Faker
import json


fake = Faker()
color_list = []

for i in range(20):
  color = fake.color_name()
  color_list.append(color)

def remove_dups(color_lst):
  if type(color_lst) == str:
    return color_lst
  var_storage = None
  counter = 0
  for color in color_lst:
    var_storage = color
    for other_color in color_lst:
      if var_storage == other_color and counter > 1:
        color_lst.remove(other_color)
      counter += 1
  return color_lst

  # set(color_lst)
  # return color_lst

color_dict = {color: len(color) for color in color_list}

with open("./data/color.json", 'w') as json_file:
  json.dump(color_dict, json_file, indent=2)

with open("./data/color.json", "r") as json_file:
  json_color_dict = json.load(json_file)
  for color, color_len in json_color_dict.items():
    if color_len > 4:
      print(f"{color}: {color_len}")