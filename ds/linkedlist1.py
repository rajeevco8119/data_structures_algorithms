class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteListBeginning(head):
    if not head:
        return None
    temp = head
    head = head.next
    temp = None
    return head


def deleteListmiddle(self, prev_node):
    temp = self.head
    while temp.next.data is not prev_node.data:
        temp = temp.next
    temp.next = temp.next.next


def deleteListEnd(self):
    current = self.head
    while current is not None:
        prev = current.next
        del current.data
        current = prev


def deleteList(self):
    node = self.head
    while node is not None:
        temp = node.next
        del node.data
        node = temp


# FLoyd's loop detection
def detectCycle(head):
    one = head.next
    two = head.next.next
    while one is not None and two is not None and two.next is not None:
        if one.data == two.data:
            print("Cycle detected")
            return
        one = one.next
        two = two.next.next
    print('Cycle not detected')


# Get Count
def getCountRecr(head):
    if head is None:
        return 0
    else:
        return 1 + getCountRecr(head.next)


def printmiddle(head):
    one = head
    l = getCountRecr(head)
    n = int(l // 2)
    while n:
        one = one.next
        n -= 1
    return one.data


def printmiddle2(head):
    one = head.next
    two = head.next.next
    while one is not None and two is not None and two.next is not None:
        one = one.next
        two = two.next.next
    print(one.data)
    return


def printlist(head):
    while head is not None:
        print(head.data)
        head = head.next


def push(head, data):
    if not head:
        return Node(data)
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head


def removeFirstNode(head):
    if not head:
        return None
    temp = head

    # Move the head pointer to the next node
    head = head.next
    temp = None
    return head


def remove_duplicates(head):
    pass


def reverseLL(head):
    curr = head
    prev = None
    while curr is not None:
        nextPtr = curr.next
        curr.next = prev
        prev = curr
        curr = nextPtr
    head = prev
    printlist(head)
    return


# head = None
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# head.next.next.next.next.next = Node(60)
# head.next.next.next.next.next.next = Node(50)
# head.next.next.next.next.next.next.next = Node(80)
# head.next.next.next.next.next.next.next.next = Node(90)
# head.next.next.next.next.next.next.next.next.next = Node(100)
# print(getCountRecr(head))
# print(printmiddle2(head))
# temp = head
# while temp.next != None:
#     temp = temp.next
# temp.next = head
# detectCycle(head)
# printlist(head)
# print('-----')
# removeFirstNode(head)
# printlist(head)


head = None
head = push(head, 12)
head = push(head, 29)
head = push(head, 11)
head = push(head, 12)
head = push(head, 12)
head = push(head, 23)
head = push(head, 8)
# printlist(head)
# removeFirstNode(head)
# remove_duplicates(head)
# reverseLL(head)
