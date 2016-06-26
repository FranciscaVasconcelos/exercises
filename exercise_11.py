# Greeter

def greeter(name):
    # A function to greet the people
    print('Hello %s!\nI hope you are well, %s.\nIt is a great day, %s.\n' % (name, name, name))

# The people to be greeted
nombres = ['Steve','Alicia','Roger']
for i in nombres:
    greeter(i)
