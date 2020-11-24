#!/usr/bin/python

sum_dict = {}
FILE = 'racquets'
with open(FILE) as r_file:
  for line in r_file:
    data_list = line.split()
    if len(data_list) > 1:
      sponsor = data_list[1]
      if sponsor in sum_dict.keys():
        current_sum = sum_dict[sponsor]
        new_sum = current_sum + 1
        sum_dict[sponsor] = new_sum
      else:
        sum_dict[sponsor] = 1
print sum_dict
