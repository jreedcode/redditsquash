#!/usr/bin/python

sum_dict = {}
FILE = 'weight.txt'

with open(FILE) as r_file:
  for line in r_file:
    if line:
      sponsor = line.split('>')[1].split('<')[0].strip('\n')
      sponsor = sponsor.lower().strip()
      if sponsor.startswith('none'):
        continue
      if sponsor.startswith('pakistan'):
        continue
      if sponsor == 'bk':
        actual_sponsor = 'black knight'
      elif sponsor.startswith('knight black'):
        actual_sponsor = 'black knight'
      elif sponsor.startswith('black knight'):
        actual_sponsor = 'black knight'
      elif sponsor.startswith('blackknight'):
        actual_sponsor = 'black knight'
      elif sponsor.startswith('c2c black knight'):
        actual_sponsor = 'black knight'
      elif sponsor.startswith('quarts'):
        actual_sponsor = 'black knight'
      elif sponsor.startswith('mantis'):
        actual_sponsor = 'mantis'
      elif sponsor.startswith('blade'):
        actual_sponsor = 'blade'
      elif sponsor.startswith('ion'):
        actual_sponsor = 'ion'
      elif sponsor.startswith('stellar'):
        actual_sponsor = 'stellar'
      elif sponsor.startswith('victor'):
        actual_sponsor = 'victor'
      elif sponsor.startswith('grays'):
        actual_sponsor = 'grays'
      elif sponsor.startswith('climax'):
        actual_sponsor = 'climax'
      elif sponsor.startswith('wilson'):
        actual_sponsor = 'wilson'
      elif sponsor.startswith('harrow'):
        actual_sponsor = 'harrow'
      elif sponsor.startswith('eye'):
        actual_sponsor = 'eye'
      elif sponsor.startswith('dunlop'):
        actual_sponsor = 'dunlop'
      elif sponsor.startswith('denlop'):
        actual_sponsor = 'dunlop'
      elif sponsor.startswith('head'):
        actual_sponsor = 'head'
      elif sponsor.startswith('tecnifibre'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('tecnifiber'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('technifibre'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('technifiber'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('carboflex'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('tecnifbre'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('suprem'):
        actual_sponsor = 'technifibre'
      elif sponsor.startswith('salming'):
        actual_sponsor = 'salmin'
      elif sponsor.startswith('prince'):
        actual_sponsor = 'prince'
      elif sponsor.startswith('karakal'):
        actual_sponsor = 'karakal'
      elif sponsor.startswith('oliver'):
        actual_sponsor = 'oliver'
      elif sponsor.startswith('pro kennex'):
        actual_sponsor = 'prokennex'
      else:
        actual_sponsor = sponsor



      if actual_sponsor in sum_dict.keys():
        current_sum = sum_dict[actual_sponsor]
        new_sum = current_sum + 1
        sum_dict[actual_sponsor] = new_sum
      else:
        sum_dict[actual_sponsor] = 1

for k, v in sum_dict.iteritems():
  print k,v
#for k, v in sum_dict.iteritems():
#  print k
#for k, v in sum_dict.iteritems():
#  print v
