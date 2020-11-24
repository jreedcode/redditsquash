#!/usr/bin/python

FILE = 'weight.sorted'

weight_list = []

with open(FILE) as weight_file:
  for line in weight_file:
    kg, num = line.split()
    kg = int(kg)
    num = int(num)
    weight_list.append((kg, num))

stop_here = len(weight_list) - 1

counter = 0
for item in weight_list:
  if counter < 1:
    counter += 1
    continue
  if counter == stop_here:
    counter += 1
    continue
  
  val_less_one = weight_list[counter - 1][1]
  mean_val = weight_list[counter][1]
  mean_kg_point = weight_list[counter][0]
  val_plus_one = weight_list[counter + 1][1]
  avg_kg = (val_less_one + mean_val + val_plus_one) / 3
  print mean_kg_point, avg_kg

  counter += 1
