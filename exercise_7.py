# Pet Names - use a dictionary to store pet names and types

# dictionary of pet names
pet_dict = {"billie":"dog","roger":"bird","wilfred":"monkey"}

# iteration through dict to print name and animal type
for name, animal in pet_dict.items(): 
    print("%s is a %s." % (name.title(), animal))
