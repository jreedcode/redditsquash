#!/usr/bin/python

FILE = 'all_weights_kg'

kg_playercount_dict = {}
with open(FILE) as w_file:
  for line in w_file:
    if line:
      kg = line.strip()
      if kg in kg_playercount_dict.keys():
        count_sum = kg_playercount_dict[kg]
        new_sum = count_sum + 1
        kg_playercount_dict[kg] = new_sum
      else:
        kg_playercount_dict[kg] = 1

for k, v in kg_playercount_dict.iteritems():
  print k, v
