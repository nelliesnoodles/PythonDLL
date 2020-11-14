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

        #  end holds the last node, and after the list is greater then 1 the whole list
        # through it's previous links

        self.end = None
        #  begin holds the first node, and the whole list through it's next links
        self.begin = None
        self._length = 0


##########   PUSH (aka : ADD/APPEND)  ################
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
            # at this point the list has at least 2 items... the begin is pointing to the next item
            # which if with 2 items is the end node.  We only need to change the end node. Begin node
            # does not need to be altered.
            #  change end node TO -->
            # change self.end next   [ <--*---, DATA, -- newnode -->  ]
            #  *   it doesn't matter what this link is. IT's set a long time ago.
            self.end.next = newnode
            # Now I set the end = to the newnode that is pushed on
            # self.end = [ <--- old self.end,   DATA,  (/)  ] (newnode)
            self.end = newnode
            self._length += 1

        assert self.end != self.begin

##################  END PUSH ######################

################## PUSH NODE.... ##################

#  pass in data of node into list... useless???############
    def push_node(self, node):
        ### if original node is passed in, it will be altered! ####
        print("activate push node")

        # passing in a node part of a list your using, will alter the original node.
        # must create a new DLLNode to pass in to keep original from being altered.
        # if there is an empty list create first node with no next or prev.

        if self.end == None and self.begin == None:

           node.prev = None
           node.next = None
           self.begin = node

        elif self.end == None and self.begin != None:
            # get the address of the original node
            oldnode = self.begin
            # create address for new node
            node.prev = None
            node.next = self.begin
            self.end = self.begin
            self.end.prev = node
            self.begin = node
            #print(self.end)
            #print(self.begin)

        else:
            print("pushing node")
            #[ <--- , node , (/)]
            node.next = None
            node.prev = self.end
            self.end.next = node
            self.end = node


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

###################      END my print outs    #################################

################################## count ######################################
    def count(self):
        # replaced with self._length, but still used in _invariant
        count = 0
        node = self.begin
        while node:
            count += 1
            node = node.next
        return count
################################  END count ###################################


#####################------------------------------------############
#################     -- GET -- and it's reverse lookup _get   #####
####################-------------------------------------#############

    def get(self, index):
        #print("GET ACTIVATED.... checking hash_key activated.")
        index = int(index)
        length = self._length
        count = 0
        if length == 0:
            # for testing, None works better then "Empty list!"
            return None
        elif index >= (length):
            print(" index out of range! ")

# this should be an error for the real thing
            # pytest for raise error is a pain in the ass....
            #raise IndexError
            return None
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
           
            return None
        elif index >= (length):
            print(" index out of range! ")

            return None
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

   ####################### END GET ##########################

########################### invariant #########################
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

#############    END _invariant    ##########################

################# Remove ########################
# [(/), 1DATA , 2--->][<---1, 2DATA 3--->][<----2, 3DATA, (/)]
# [(/), 1DATA , 3--->][<---1 3DATA, (/)]

    def remove(self, obj):
        #  my original remove had a ton of stuff in it....
        # I should have kept it to show the long way round....
        # removing the entire node is a much better option.  These Nodes as I've learned can
        # grow to contain TONS of stuff...  I had no idea there was a fast way round till now.
        head = self.begin
        #tail = self.end
        while head:
            if head.value == obj:
                result = head.value
                self.detach_node(head)
                self._length -= 1
                return result
                #testing return result
                break
            head = head.next



########################### END remove ######################

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

################## END detach_node ################

####  someone in class, and my sister helped me realize
## that in sorting this list, I need to exchange the entire node
## not just the data.....  #####################


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

    def swap_helper(self, node1, node2):
       
        #[or NONE spam -- n1-->][<---spam---node1--eggs--->][<--n1--eggs or NONE]
        #[or NONE bags -- n2-->][<---bags---node2---nots-->]<---n2--nots or NONE]
        ### make sure they are not next to each other ###
        temp1_next = node1.next 
        temp1_prev = node1.prev 
        temp2_next = node2.next 
        temp2_prev = node2.prev
        print(node1, node2)
       
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
              

        print(node2, node1)

        
        # swap the nieghbors pointers
       
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

        
                
        # neighbors 
        #[<-- prev neighbor -->][<-- node1 -->][<-- next neighbor -->]
        #[<-- prev neighbor -->][<-- node2 -->][<-- next neighbor -->]
        
            

    def printnodes(self):
        length = self._length
        print(length)
        x = self.begin
        for i in range(0, length):
            print(x)
            print(i)
            x = x.next
            



        
        


#################  shift  ##########################
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


##########  unshift is just push() #########

    def unshift(self, obj):
        self.push(obj)

############################################

########  Python cleans up anything that is no longer referenced ######
#### so once you set these to None.... the nodes get garbage collected ####

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
            


 
#######   END dump ###################

########            insert          ##########
#######      like remove in reverse     ####

    def insert(self, obj, index):
        # this isn't required for my class, but I want to be able to do it.
        # I'm thinking inserting at the beginning, is what the unshift should do.
        #[(/), (1)DATA, 2--->][<---1, (2)DATA, 3---->][<---2, (3)DATA, (/)]
        #           1 [<----1, (m)DATA, 2--->] 2
        #[(/), (1), m-->][<--1, (m), 2-->][<--m,(2),3-->][<--2,(3), (/)]


        head = self.begin
        tail = self.end
        length = self.count()
        # check if they are just pushing.
        if index == length:
            print(" pushing: push() ")
            self.push(obj)
        # check if they are prefixing
        # I'm going to make one... prefix
        elif index == 0:
            print( " prefixing data: prefix() ")
            self.prefix(obj)

        # check if they are indexing out of range:
        elif index > length:
            print(" index out of range! ")
            return None

        # Empty list is covered, index too high is covered, end of list
        # is covered
        # [(/), (a)DATA, (b)-->]  [else]  [<---(a)DATA, (/)]
        else:
            #should be just like detach_node:
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
