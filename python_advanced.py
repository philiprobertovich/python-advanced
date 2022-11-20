from faker import Faker

fake = Faker()
color_list = []

for i in range(20):
  color = fake.color_name()
  color_list.append(color)

def remove_dups(color_lst):
  set(color_lst)
  return color_lst

color_dict = {color: len(color) for color in color_list}