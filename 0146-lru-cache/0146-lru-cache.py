class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    #need to definitely create a linked list and use hashmap to store address of each node, greedyly can do, but full baddhakam :(

    def __init__(self, n: int):
        self.len = n
        self.dic = {}
        self.head, self.tail = None, None

    def get(self, key: int) -> int:
        if key in self.dic:
            s = self.dic[key].val
            arr = s.split('-')
            ans = int(arr[1])

            node = self.dic[key]

            if node.prev == None:
                return ans
            node.prev.next = node.next

            if node.next == None:
                self.tail = node.prev
            else:
                node.next.prev = node.prev
            
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node

            return ans
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.dic:
            s = self.dic[key].val
            arr = s.split('-')
            arr[1] = str(val)
            s = arr[0] + '-' + arr[1]

            node = self.dic[key]
            self.dic[key].val = s

            if len(self.dic) == 1:
                return 

            if node.prev == None:
                return 
            node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
            return
        
        s = str(key) + '-' + str(val)
        new_node = Node(s)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        self.dic[key] = new_node

        if len(self.dic) == 1:
            return 
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        if len(self.dic) > self.len:
            s = self.tail.val
            arr = s.split('-')
            a = int(arr[0])
            
            del self.dic[a]
            
            node = self.tail    
            node.prev.next = None
            self.tail = node.prev
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)