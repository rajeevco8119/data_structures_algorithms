def sortLL(head):
    curr = head
    index = None
    while curr is not None:
        index = curr.next
        while index is not None:
            if curr.data > index.data:
                curr.data, index.data = index.data, curr.data
            index = index.next
        curr = curr.next
    printlist(head)
    return
  
  
  
head = None
head = push(head, 29)
head = push(head, 11)
head = push(head, 12)
head = push(head, 23)
head = push(head, 8)
# sortLL(head)
