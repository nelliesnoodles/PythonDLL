class DLLNode(object):
   
    def __init__(self, prev, value, nxt):
        # the first node will have no next or previous
        self.value = value
        self.next = nxt       
        self.prev = prev

    def __repr__(self):  #     [ <--- prev ,  DATA  , next ---> ]
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        ##  previous node,  assigned value, link to next node in list ##
        return f"[{repr(pval)}, {self.value}, {repr(nval)}]"

class DLList(object):


    def __init__(self):
        self.end = None
        self.begin = None
        self._length = 0


#--    push    --#
    def push(self, obj):


        # if there is an empty list create first node with no next or prev.

        if self.end == None and self.begin == None:

           newnode = DLLNode(None, obj, None)
           self.begin = newnode
           self._length += 1
         


       ## if the list has contents,
       ## I don't want the end node and begin node to ever be at the same address.
        elif self.end == None and self.begin != None:
            # get the address of the original node
            node = self.begin
            # create address for new node
            newnode = DLLNode(node, obj, None)
            self.end = newnode
            self.begin.next = self.end
            self._length += 1

        else:
            #[ <--- , DATA, (/)]
            node = self.end
            #[<-node---, DATA,  (/) ] [self.end, obj, None]
            newnode = DLLNode(node, obj, None)
           
            self.end.next = newnode
            # Now I set the end = to the newnode that is pushed on
            # self.end = [ <--- old self.end,   DATA,  (/)  ] (newnode)
            self.end = newnode
            self._length += 1

        assert self.end != self.begin



#--     For pushing a node onto the list, and not just a value --#


    def push_node(self, node):

        if self.end == None and self.begin == None:
            self.begin = node
            node.next = None
            node.prev = None
            self._length += 1
        elif self.end == None and self.begin != None:
            # get the address of the original node
            start = self.begin
            # create address for new node
            node.prev = start
            node.next = None
            self.end = node
            self.begin.next = self.end
            self._length += 1

        else:
            #[ <--- , DATA, (/)]
            end = self.end
            #[<-node---, DATA,  (/) ] [self.end, obj, None]
            node.prev = end
            node.next = None
           
            self.end.next = node
            # Now I set the end = to the newnode that is pushed on
            # self.end = [ <--- old self.end,   DATA,  (/)  ] (newnode)
            self.end = node
            self._length += 1

        assert self.end != self.begin


#################----------------------------------##############
#######                MY PRINT OUT METHODS             #########
             ###( <--- previous, obj , next --->)###

    def graphical(self):
        ##  graphical uses the prev, to go through the list.
        ##  so it's like an invariant check..................
        ## None = (/)
        ## [ link = node in list ]
        ## OBJ =  (data count)DATA?
        ##   [  prev  2 , third data,  next none ]
        ## so, [ <---2 , (3) DATA ,  (/)  ]
        length = self._length
        node = self.begin
        if self.begin == None:
            print(" EMPTY ")
        elif self.begin != None and self.end == None:
            print("\n\n")
            # [(/), (0) DATA, (/)]
            print(f"{node.value}=")
            print(f"[(/), (0) DATA, (/)]")
        else:
            node = self.end
            #I only modify length to keep track
            if node:
                print("\n\n")
            while node:
                
                # example, length is 3
                if node.next == None and node.prev != None:
                    # [ <--2 , (3)DATA , (/) ]
                    print(f"\t\t{node.value}=")
                    print(f"\t [<-- {length -1}, ({length})DATA , (/) ]")
                elif node.next != None and node.prev != None:
                    # [ <--1, (2)DATA , 3-->]
                    print(f"\t\t{node.value}=")
                    print(f"\t [<-- {length -2}, ({length-1})DATA, {length}-->]")
                    length -= 1
                else:
                    # [ (/), (1)DATA , 2-->]
                    print(f"\t\t{node.value}=")
                    print(f"\t [ (/), (1)DATA, 2--> ]")
                node = node.prev
                print("\n")

    ########  <------   prev ---- end
    def what_end(self):

        node = self.end
        if node:
            print(" end = ")
            while node:

                print(node)
                node = node.prev

    ########   begin ----->  next
    def where_begin(self):
        node = self.begin
        print(" front = ")
        chain = f"[ "
        if node:
            while node:
                if node.next != None:
                    chain = chain + (f"{node.value}, ")
                    node = node.next
                else:
                    chain = chain + (f"{node.value}]")
                    node = node.next
            print(chain)

#--            count                --#

    def count(self):
        # replaced with self._length, but still used in _invariant
        count = 0
        node = self.begin
        while node:
            count += 1
            node = node.next
        return count

    #--             get             --#

    def get(self, index):
        
        index = int(index)
        length = self._length
        count = 0
        if length == 0:
            print(" Empty list ")
            raise ValueError
        elif index >= (length):
            print(" index out of range! ")
            raise IndexError

            
        else:
            count = 0
            node = self.begin
            while node:
                #print(f"while loop.{count}")
                if count == index:
                    #print('get return value:')
                    #print(node.value)
                    return node.value


                node = node.next
                count += 1

#-- NEW  GET NODE ---
    def get_node(self, index):
       
        index = int(index)
        length = self._length
        count = 0
        if length == 0:
            print("This list is empty")
            raise ValueError
        elif index >= (length):
            print(" index out of range! ")
            raise IndexError
            
        else:
            count = 0
            node = self.begin
            while node:
                
                if count == index:
                   
                    return node


                node = node.next
                count += 1




    def _get(self, index):
        length = self.count()

        if length == 0:
            print(" ***** Empty list ***** ")
            return(None)

        elif index >= (length):
            print(" index out of range! ")
            return None

        elif length == 1:
            # when there are 0, or 1 item's on the list, else loop won't work.
            if index == 0:
                node = self.begin
                return(node.value)


        else:
            node = self.end
            #  [(/)(0)DATA -->][<---(1)DATA--->][<---(2)DATA--->][<---(3)DATA (/) ]
            # length    1              2               3                4
            while node:

                if length == index + 1:
                    return(node.value)
                else:
                    node = node.prev

                length -= 1


#--          invariant             --#
# the things that need to hold true on every change to the list

    def _invariant(self):
        node = self.begin
        length = self.count()
        if node == None:
            assert length == self._length
            assert self.end == None
        elif length == 1:
            assert length == self._length
            assert node.next == None
            assert node.prev == None
            assert self.end == None
        else:
            assert length == self._length
            assert self.end != self.begin
            assert self.end.next == None
            assert self.begin.prev == None

#--         remove       --#
# [(/), 1DATA , 2--->][<---1, 2DATA 3--->][<----2, 3DATA, (/)]
# [(/), 1DATA , 3--->][<---1 3DATA, (/)]

    def remove(self, obj):
        #  my original remove had a ton of stuff in it....
        # I should have kept it to show the long way round....
        # removing the entire node is a much better option.  These Nodes as I've learned can
        # grow to contain TONS of stuff...  I had no idea there was a fast way round till now.
        head = self.begin
        #tail = self.end
        result = None
        while head:
            if head.value == obj:
                result = head.value
                self.detach_node(head)
                self._length -= 1
                return result
                #testing return result
                break
            head = head.next
        if not result:
            print(f" Value not found. ")
            raise ValueError

        



#--     detach     --#

    def detach_node(self, node):
             ### node ###   [  <---1  , 2DATA , 3--->  ]  ### node ###
       # [(/), 1DATA , ((2--->))][**<---1**, 2DATA** 3--->**](([<----2)))), 3DATA, (/)]
       # [(/), 1DATA , 3--->][<---1 3DATA, (/)]
        if node.prev == None and node.next == None:
            ## working with Dictionary.... detach nodes...
            ## one node on the list
            self.begin = None
            self.end = None

        elif node.prev == None and node.next != None:
            # node is a begin node:
            #[(/) node ---next-->][<----new---->]
            newnode = node.next
            if newnode.next != None:
                # newnode is not the end node
                self.begin = newnode
                self.begin.prev = None
            else:
                # newnode is the end node
                # two items on list
                self.begin = newnode
                self.end = None
                self.begin.prev = None


        elif node.next == None and node.prev != None:
            # node is an end node:
            # [<---new ---node ---->][<--new--- node  (/)]

            newend = node.prev
            if newend.prev == None:
                ## newend is the begin node
                ## two items on list
                self.end = None
                self.begin.next = None
            else:
                ## node is end node
                ## more then two on list
                self.end = newend
                self.end.next = None

        else:
            ## item in the middle of list.
            ## not begin or end node

            prevlink = node.prev # <---1
            #[(**<---1**), 2DATA,  3-->]

            nextlink = node.next # ---> 3
            #[(<---1, 2DATA, (**3--->**))]

            #node.prev.next = 2--->
            #[(/), 1DATA, ((**2--->**))]
            # nextlink == ----> 3
            node.prev.next = nextlink

            #node.next.prev = <----2
            # [**<---2**, DATA3, (/)]
            # prevlink == <-----1
            node.next.prev = prevlink





# ---   Pop() remove and return the last node --- #  

    def pop(self):
        lastnode = self.end 
        if lastnode != None:
            temp = self.end.value
            self.detach_node(self.end)
            # in detach_node, the length is not changed
            self._length -= 1
            return temp

        elif self.end == None and self.begin != None:
            temp = self.begin.value 
            self.detach_node(self.begin)
            self._length -= 1 
            return temp
        else:
            
            message = "The list has no last value: empty list."
            print(message)
            return None

#--       swap       --#

    def swap(self, index1, index2):
        node1 = self.get_node(index1)
        node2 = self.get_node(index2)
        print(f"size = {self._length}")
        if node1 != None and node2 != None:
            #print(f"node1 = {node1.value} , node2 = {node2.value}")
            self.swap_helper(node1, node2)
        else: 
            message = "One or both of the index's are an index Error. \n Could not swap"
            print(message)
            raise IndexError

    def swap_helper(self, node1, node2):
       
        #[or NONE spam -- n1-->][<---spam---node1--eggs--->][<--n1--eggs or NONE]
        #[or NONE bags -- n2-->][<---bags---node2---nots-->]<---n2--nots or NONE]
        ### make sure they are not next to each other ###
        temp1_next = node1.next 
        temp1_prev = node1.prev 
        temp2_next = node2.next 
        temp2_prev = node2.prev
        #print(node1, node2)
       
        #[<--  node1 --->]*CHECK*[<--- node2 -->]
        neighbor = False
        if node1.next != node2 and node1.prev != node2:
            node2.next = temp1_next
            node2.prev = temp1_prev
        else:
            neighbor = True
        
        if node2.next != node1 and node2.prev != node1:
            node1.next = temp2_next
            node1.prev = temp2_prev
        else:
            neighbor = True

        if neighbor:
           if node1.next == node2:
               node1.next = temp2_next 
               node1.prev = node2 
               node2.prev = temp1_prev 
               node2.next = node1 
           elif node1.prev == node2:
               node1.prev = temp2_prev 
               node1.next = node2 
               node2.next = temp1_next 
               node2.prev = node1 
              

        #print(node2, node1)
        # swap the nieghbors pointers               
        # neighbors 
        #[<-- prev neighbor -->][<-- node1 -->][<-- next neighbor -->]
        #[<-- prev neighbor -->][<-- node2 -->][<-- next neighbor -->]
       
        if temp1_next != None:
            if temp1_next != node2:
                temp1_next.prev = node2
        
        else:
            self.end = node2

        if temp1_prev != None:
            if temp1_prev != node2:
                temp1_prev.next = node2 
        else:
            self.begin = node2

        if temp2_next != None:
            if temp2_next != node1:
                temp2_next.prev = node1
        else:
            self.end = node1

        if temp2_prev != None:
            if temp2_prev != node1:
                temp2_prev.next = node1
        else:
            self.begin = node1

        
        
        
            

    def printnodes(self):
        length = self._length
        print(length)
        x = self.begin
        for i in range(0, length):
            print(x)
            print(i)
            x = x.next

#--       shift       --#

    def shift(self):
        # shift is a reverse pop()
        # check for empty list:
        head = self.begin
        # end and begin node never occupy the same space
        # If a list size is one, we will still be retrieving the first node
       
        if head != None:
            temp = head.value
            self.detach_node(head)
            self._length -= 1 
            return temp 
        else:
            message = "This is an empty list"
            print(message)
            return None


#--   unshift  --#

    def unshift(self, obj):
        self.push(obj)



#  Python cleans up anything that is no longer referenced 
# so once you set these to None.... the nodes get garbage collected 

    def dump(self):
        ## I had this wrong.... dump is supposed to print the contents to screen....##
        print("dump")
        start = self.begin
        
        if start == None:
            print(" [] ")
            
        else:
            x = "["
            while start:
                x = x + f"{start.value},"
                start = start.next

            print (x + " ]")


    def dump_list(self):
       
        start = self.begin
        testlist = []
        if start == None:
            return testlist
            
        else:
            
            while start:
                val = start.value
                testlist.append(val)
                start = start.next
        return testlist
            

   def _dump_list(self, begin=True):
        end = self.end
        testlist = []
        if end == None:
            return testlist 
        else:

            while end:
                val = end.value 
                testlist.append(val)
                end = end.prev
        if begin:
            testlist.reverse()
            
        return testlist
 


#--             insert          --#


    def insert(self, obj, index):
        
        head = self.begin
        tail = self.end
        length = self._length
        # check if they are just pushing.
        if index == length:           
            self.push(obj)

        # check if they are prefixing        
        elif index == 0:            
            self.prefix(obj)

        # check if they are indexing out of range:
        elif index > length:
            # to bypass pytest error, import pytest and in your test use:
            # with pytest.raises(IndexError):
            #    mylist.insert('obj', 99)
            # where obj is the item being pushed, and 99 the index out of range
            print(f"the length of this list is: {length}")
            raise IndexError
            

       
        # [(/), (a)DATA, (b)-->]  [else]  [<---(a)DATA, (/)]
        else:
            
            head = self.begin
            count = 0

            link = None
            plink = None
            nlink = None

            while head:

                if index == count:
                   self.attach_node(head, obj)
                   self._length += 1
                   break
                else:
                    head = head.next
                    count += 1



##############  attach node ########################

    def attach_node(self, node, obj):
        #                    newnode
        ### node ### [<---a ,   x   , b--->] ### node ###

        #    old previous ((a))      index node being replaced((b))
        #  [ ~~ ,  a , --->]   ((x))    [<----, b , ~~ ]

        newnode = DLLNode(None , obj, None)
        #1 [<---a--,  x ,  (/)] set prev of newnode
        newnode.prev = node.prev
        #2 [<---a--, x , --b--->] set next of newnode
        newnode.next = node
        #3 [~~  ,  a  , ---x-->] set next of previous node to newnode
        node.prev.next = newnode
        #4 [<--x---, b , ~~ ] set previous of the index, given node to newnode
        node.prev = newnode
        # doing (3 and 4)   out of order will break your list.

############ END attach node ################



################  prefix #####################################
############  like push, but at the beginning of the list ####

    def prefix(self, obj):

        # insert at the beginning of list.
        head = self.begin
        tail = self.end

        if head == None:
            print(" .... pushing....")
            self.push(obj)
        elif head !=None and tail == None:
            #    [(/), (a)DATA, (/)]     None
            #[(/), (b)newData, a--->][<---(b), (a)DATA, (/)]
            self.end = self.begin
            newnode = DLLNode(None, obj, self.end)
            self.end.prev = newnode
            self.begin = newnode
            self._length += 1


        else:
            #   link begin
            #[(/), (a)DATA, (x)--->][<---(a), DATA(x), (/)--->]
            #           here       link new here
            #[(/), (new), (a)--->][<--(new), (a)DATA, (x)--->]...>
            link = self.begin
            newnode = DLLNode(None, obj, link)
            self.begin.prev = newnode
            self.begin = newnode
            self._length += 1

    def last(self):
        node = self.end
        if node:
            return node.value
        else:
            return None

    def first(self):
        node = self.begin
        if node:
            return node.value
        else:
            return None
