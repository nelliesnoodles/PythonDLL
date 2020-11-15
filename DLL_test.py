
from DLL import*
import pytest

def test_push():
    #colors is a placeholder for the instance DLList Double linked list
    # I'm totally coping the test from single linked list and modifing it.

    colors = DLList()
    #Use colors placeholder get the DLL instance assigned to it
    # and use it's push(function) ... The arg , obj, being "Pthalo Blue"
    colors.push("Pthalo Blue")
    colors._invariant()
    # assert that the instances, count function returns a 1
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    colors._invariant()
    assert colors.count() == 2
    colors.push("Yellow")
    colors._invariant()
    assert colors.count() == 3

### deciding how Zed wants this _invariant thing done.... ####

def test_pop():
    ##  remove the last item in the linked list
    colors = DLList()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors.push("yellow")

    assert colors.pop() == "yellow"
    colors._invariant()
    assert colors.get(3) == None
    colors._invariant()
    assert colors.get(2) == None
    assert colors.get(0) == "Magenta"
    colors._invariant()
    assert colors.get(1) == "Alizarin"
    assert colors.pop() == "Alizarin"
    colors._invariant()
    assert colors.get(2) == None
    assert colors.get(0) == "Magenta"
    assert colors.pop() == "Magenta"
    colors._invariant()
    assert colors.pop() == None
    assert colors.get(0) == None
    colors._invariant()
    #print(zero)

def test_inv_get():
    # I think this is what he means by an invariant....
    colors = DLList()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors.push("yellow")

    assert colors.pop() == "yellow"
    colors._invariant()
    # get doesn't change anything... I don't think I need to do invariant check...
    assert colors._get(3) == None
    assert colors._get(2) == None
    assert colors._get(0) == "Magenta"
    assert colors._get(1) == "Alizarin"
    assert colors.pop() == "Alizarin"
    assert colors._get(2) == None
    assert colors._get(0) == "Magenta"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None
    assert colors._get(0) == None

def test_remove():
    colors = DLList()
    colors.push("blue")
    colors.push("yellow")
    colors.remove('yellow')
    colors._invariant()
    colors.push("green")
    colors.push("orange")
    colors.push("Trillium")
    colors.remove("green")
    assert colors.count() == 3
    assert colors.get(1) == "orange"
    with pytest.raises(ValueError):
        colors.remove(9)
    assert colors.remove('blue') == 'blue'
    colors._invariant()
    assert colors.count() == 2
    assert colors.get(0) == "orange"
    assert colors.get(1) == "Trillium"
    with pytest.raises(IndexError):       
        colors.get(2)
    
    colors.remove('orange')
    assert colors.count() == 1

def test_prefix():
    colors = DLList()
    #Use colors placeholder get the DLL instance assigned to it
    # and use it's push(function) ... The arg , obj, being "Pthalo Blue"
    colors.prefix("Pthalo Blue")
    colors._invariant()
    # assert that the instances, count function returns a 1
    assert colors.count() == 1
    colors.prefix("Ultramarine Blue")
    colors._invariant()
    assert colors.count() == 2
    colors.prefix("Yellow")
    colors._invariant()
    assert colors.count() == 3

def test_shift():
    # shift, reverse pop()
    # remove first item of list
    colors = DLList()
    colors.push("Pthalo Blue")
    colors.push("Ultramarine Blue")
    colors.push("Yellow")
    colors.shift()
    colors._invariant()
    assert colors.get(0) == "Ultramarine Blue"
    assert colors.get(1) == "Yellow"
    colors.shift()
    colors._invariant()
    assert colors.get(0) == "Yellow"
    colors.shift()
    colors._invariant()
    with pytest.raises(ValueError):
        colors.get(0)

def test_prefix():
    # add to the front of the list
    colors = DLList()
    colors.prefix("Pthalo Blue")
    colors._invariant()
    colors.prefix("Ultramarine Blue")
    colors._invariant()
    colors.prefix("Yellow")
    colors._invariant()
    assert colors.get(0) == "Yellow"
    assert colors.get(1) == "Ultramarine Blue"
    assert colors.get(2) == "Pthalo Blue"


def test_insert():
    colors = DLList()
    colors.push("blue")
    assert colors.get(0) == "blue"
    colors.insert("new color", 0)
    colors._invariant()
    assert colors.get(0) == "new color"
    assert colors.get(1) == "blue"
    colors.push("yellow")
    assert colors.count() == 3
    assert colors.get(2) == "yellow"
    colors.insert("orange", 2)
    colors._invariant()
    assert colors.get(2) == "orange"
    assert colors.get(3) == "yellow"
    assert colors.count() == 4
    colors.insert("green", 2)
    colors._invariant()
    with pytest.raises(IndexError):
        colors.insert('gray', 22)

def test_length():
    spam = DLList()
    spam.push("jello")
    assert spam._length == 1
    spam.push("lions")
    assert spam._length == 2
    spam.push("metabolism")
    assert spam._length == 3
    for i in range(0, 100):
        spam.push(i)
    assert spam._length == 103
    spam.prefix("hush")
    assert spam._length == 104
    for i in range(0, 100):
        spam.remove(i)
    assert spam._length == 4 

def test_pop():
    names = DLList() 
    names.push('John')
    names.push('Darian')
    names.push('Harold')
    names.push('Maude')
    names.push('Carol')
    x = names.pop() 
    assert x == 'Carol'
    assert names._length == 4 
    y = names.pop() 
    assert y == 'Maude'
    assert names._length == 3 
    a = names.pop() 
    assert a == 'Harold'
    assert names._length == 2 
    b = names.pop() 
    assert b == 'Darian'
    assert names._length == 1 
    c = names.pop() 
    assert c == 'John'
    assert names._length == 0 
    d = names.pop() 
    assert d == None 
    assert names._length == 0

def test_swap():
    mytrees = DLList()
    mytrees.push('pine')
    mytrees.push('maple')
    mytrees.push('palm')
    mytrees.push('redwood')
    mytrees.push('baobab')

    StartList = mytrees.dump_list()
    test1 = ['pine', 'maple', 'palm', 'redwood', 'baobab']
    assert test1 == StartList
    mytrees.swap(0, 4)
    test2 = ['baobab', 'maple', 'palm', 'redwood', 'pine']
    test2List = mytrees.dump_list() 
    assert test2 == test2List
    test3 = ['baobab', 'palm', 'maple', 'redwood', 'pine']
    mytrees.swap(1, 2)
    test3List = mytrees.dump_list()
    assert test3 == test3List
    test4 = ['palm', 'baobab', 'maple', 'redwood', 'pine']
    mytrees.swap(1, 0)
    test4List = mytrees.dump_list()
    assert test4 == test4List
    test5 = ['palm', 'baobab', 'maple', 'pine', 'redwood']
    mytrees.swap(4, 3)
    test5List = mytrees.dump_list() 
    assert test5 == test5List
    with pytest.raises(IndexError):
        mytrees.swap(1, 99)


def test_get():
    mylist = DLList() 
    mylist.push('pup')
    mylist.push('kit')
    mylist.push('doggo')
    mylist.push('cat-o')
    pup = mylist.get(0)
    assert pup == 'pup'
    kit = mylist.get(1)
    assert kit == 'kit'
    doggo = mylist.get(2)
    assert doggo == 'doggo'
    cato = mylist.get(3)
    assert cato == 'cat-o'

    with pytest.raises(IndexError):
        mylist.get(5)


def test_getnode():
    noodles = DLList() 
    node1 = DLLNode(None, 'ramen', None)
    node2 = DLLNode(None, 'egg', None)
    node3 = DLLNode(None, 'speghetti', None)
    noodles.push_node(node1)
    noodles.push_node(node2)
    noodles.push_node(node3)
    ramen = noodles.get_node(0)
    assert ramen.value == 'ramen'
    egg = noodles.get_node(1)
    assert egg.value == 'egg'
    speghetti = noodles.get_node(2)
    assert speghetti.value == 'speghetti'