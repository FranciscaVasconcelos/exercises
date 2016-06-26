# Mountain Heights

# 5 tallest mountains in the world and their heights
mountains = {'Everest':'8848','K2':'8611','Kangchenjunga':'8586','Lhotse':'8586','Makalu':'8485'}

print('Mountain names:')
for name in mountains:
    print(name)
print('\n')

print('Mountain elevations:')
for elevation in mountains.values():
    print(elevation)
print('\n')

for name, elevation in mountains.items():
    print(name + ' is ' + elevation + ' meters tall.')
