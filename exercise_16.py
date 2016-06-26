# Mountain Heights 3

def m2f(meters):
    return meters * 3.28

# 5 tallest mountains in the world and their heights
mountains = {'Everest':['8848',m2f(8848)],'K2':['8611',m2f(8611)],
            'Kangchenjunga':['8586',m2f(8586)],
            'Lhotse':['8586',m2f(8586)],'Makalu':['8485',m2f(8485)]}

print('Mountain names:')
for name in mountains:
    print(name)
print('\n')

print('Mountain elevations (meters):')
for i in mountains.values():
    print(i[0])
print('\n')

print('Mountain elevations (feet):')
for i in mountains.values():
    print(i[1])
print('\n')

for name, height in mountains.items():
    print(name+' is '+ height[0]+' meters, or '+
        str(height[1]) +' feet tall.')
