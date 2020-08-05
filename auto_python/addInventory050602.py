# @File  : addInventory050602.py
# @Author: leipei
# @Date  :  2020/08/05

def displayInventory(parm):
    num = 0
    for k, v in parm.items():
        print (v,k)
        num += parm.get(k)
    print('Total number of items: ',num)

# 更新字典，将物品清单中的物品整合到原来字典中
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] += 1
        else:
            inventory.setdefault(addedItems[i],1)
    return inventory

# 初始字典
inv = {'gold coin':42, 'rope':1}
# 新清单
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# 更新后的字典
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)