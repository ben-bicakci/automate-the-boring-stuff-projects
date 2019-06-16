# fantasy-game-inventory.py
# By Ben Bicakci
# Source: Automate the Boring Stuff with Pythong by Al Sweigart

stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def display_inventory(inventory):
    
    total_items = 0

    print("Inventory: ")
    
    for k, v in inventory.items():
        print(v, k)
        total_items = total_items + v
    
    print('Total number of items: ' + str(total_items))

display_inventory(stuff)


inv = {'gold coin': 42, 'rope': 1}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def update_inventory(inventory, loot):

    updated_inv = dict(inventory)

    for item in loot:
        updated_inv.setdefault(item, 0)
        updated_inv[item] += 1
    
    return updated_inv


inv = update_inventory(inv, dragon_loot)
display_inventory(inv)