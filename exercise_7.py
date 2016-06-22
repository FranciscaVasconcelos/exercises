# Pet Names - use a dictionary to store pet names and types

pet_dict = {"billie":"dog","roger":"bird","wilfred":"monkey"}

for name, animal in pet_dict.items(): 
    print("%s is a %s." % (name.title(), animal))
