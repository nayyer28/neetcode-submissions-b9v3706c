class Node:

    def __init__(self, val: [int,int] = (0,0), nxt: Optional[Node] = None, prv: Optional[Node] = None ):
        self.val = val # (key , val)
        self.nxt = nxt
        self.prv = prv

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node() # lru head
        self.tail = Node() # lru tail
        self.head.nxt = self.tail
        self.tail.prv = self.head

        self.cache = {} # key -> node
        self.cap = capacity
    
    def remove_node(self, node):
        node.prv.nxt = node.nxt # node-1 -> node+1
        node.nxt.prv = node.prv # node-1 <- node+1
    
    def add_node(self, node):
        node.nxt = self.tail # node -> tail
        node.prv = self.tail.prv # node-1 <- node
        self.tail.prv.nxt = node # node-1 -> node
        self.tail.prv = node    # node <- tail

    def get(self, key: int) -> int:
        # if key in hmap return but change lru sequence
        if key not in self.cache:
            return - 1
        
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)
        return node.val[1]


    def put(self, key: int, value: int) -> None:
        node = Node((key, value))
        
        if key in self.cache: # remove
            self.remove_node(self.cache[key])
        
        # now add
        self.add_node(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            # remove head.nxt
            lru = self.head.nxt
            self.remove_node(lru)
            del self.cache[lru.val[0]]
        
        
                    
        
