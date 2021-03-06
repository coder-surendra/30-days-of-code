class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    def removeDuplicates(self,head):
        #Write your code here
        if head is None:
            return
        else:
            arr = []
            curr = lastNode = head
            
            while curr is not None:
                #arr.append(curr.data)
                if curr.data not in arr:
                    arr.append(curr.data)
                    oldNode = curr
                    
                else:
                    oldNode.next = curr.next
                    #curr.next = curr.next.next
                #oldNode = curr
                curr = curr.next
                
            return head    
            #print(arr)
  

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 