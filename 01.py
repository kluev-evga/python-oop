class Block:
    color = 'red'
    radius = 2

    def __init__(self, color):
        self.color = color


bl = Block('orange')
# print(bl.__dict__)
delattr(Block, 'color')
print(hasattr(bl, 'color'))