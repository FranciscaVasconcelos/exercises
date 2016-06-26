# Mountain Heights 4

# 5 tallest mountains in the world and their heights
mountains = {'Everest':{'elevation': 8456,'range':'Himalayas'},
            'K2':{'elevation': 8364,'range': 'Himalayas'},
            'Kangchenjunga':{'elevation': 8295,'range': 'Himalayas'},
            'Lhotse':{'elevation': 8235,'range': 'Himalayas'},
            'Makalu':{'elevation': 8178,'range': 'Himalayas'}}

print('Mountain names:')
for name in mountains:
    print(name)
print('\n')

print('Mountain elevations:')

for name, d in mountains.items():
    elev = []    
    for i, j in d.items():
        elev.append(j)        
    print(elev[1])
print('\n')

print('Mountain range:')
for name,d in mountains.items():
    rang = []    
    for i, j in d.items():
        rang.append(j)        
    print(rang[0])
print('\n')

for name, d in mountains.items():
    val = []    
    for i, j in d.items():
        val.append(j)        
    print(name+' is an '+ val[1] +' meters tall mountain in the '+
        str(val[0]) +' range.')
