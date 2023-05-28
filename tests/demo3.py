from transitions import Machine


class Matter(object):
    pass


lump = Matter()

machine = Machine(model=lump, states=['solid', 'liquid', 'gas', 'plasma'], initial='solid')

# Lump now has state!
print(lump.get)
