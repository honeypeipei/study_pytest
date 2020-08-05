# @File  : inventory0506.py
# @Author: leipei
# @Date  :  2020/08/05

allThing = {'rope':1,'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(parm):
    num = 0
    for k, v in parm.items():
        print (v,k)
        num += parm.get(k)
    print('Total number of items: ',num)

displayInventory(allThing)