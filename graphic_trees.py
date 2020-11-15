from DLL import * 

# create list
mytrees = DLList()
mytrees.push('pine')
mytrees.push('maple')
mytrees.push('palm')
mytrees.push('redwood')
mytrees.push('baobab')

noodles = DLList() 
node1 = DLLNode(None, 'ramen', None)
node2 = DLLNode(None, 'egg', None)
node3 = DLLNode(None, 'speghetti', None)
noodles.push_node(node1)
noodles.push_node(node2)
noodles.push_node(node3)
#print(noodles.get_node(1))

noodles.dump()