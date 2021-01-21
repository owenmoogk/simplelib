import singly_linked_list

mylist = singly_linked_list.singlyLinkedList()

mylist.display()
mylist.append(1)
mylist.append(6)
mylist.display()
print(mylist.size())
mylist.append("boiiiii smd")
print(mylist.size())
mylist.display()
print(mylist.get(1))
mylist.erase(1)
mylist.display()

mylist.insertAtIndex("hello",1)
mylist.display()

mylist.insertBefore(545,"hello")
mylist.insertAfter(545,"hello")
mylist.insertAfter(545,"boiiiii smd")
mylist.display()
print(mylist.size())
mylist.insertAtIndex("hello",5)
mylist.display()

mylist.eraseItem(545)
mylist.eraseItem(545)
mylist.eraseItem(545)
mylist.display()

print(mylist.inList(1))
print(mylist.inList(3))

print(mylist.getItemIndex("boiiiii smd"))
print(mylist.getItemIndex("hello"))
print(mylist.getItemIndex(545))

mylist.display()
mylist.deleteList()
mylist.display()