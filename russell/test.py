dna_map_including_history = {}
dna_map = {}
with open('main_results.csv') as f:
  for line in f:
    parts = line.split(',')
    query, dna = parts[0], parts[2]
    dna_map[dna] = query
    if dna not in dna_map_including_history:
      dna_map_including_history[dna] = set()
    dna_map_including_history[dna].add(query)

with open('dna_map_with_duplicates.txt', 'w') as f:
  for k,v in dna_map_including_history.items():
    f.write(k + ' -> ' + ' '.join(v) + '\n') #left is DNA and right is the proteins. 

with open('lasso_features.csv') as f:
  for line in f:
    parts = line.split(',')
    dna = parts[0]
    if dna in dna_map:
      print(dna_map[dna])
    else:
      print('xxxx')