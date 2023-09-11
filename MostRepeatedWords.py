import sys


l = []
count = k = 0

for line in sys.stdin:
    word = ""
    for c in line:
        if c ==  '=':
            k = count
        if  65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 :
            word += c
        else:
            word.replace(',', '').replace(':', '').replace("'", "")
            if word != '':
                l.append(word.lower())
                count += 1
                word = ""
            else:
                word = ""

our_strings = l[:(k-1)]

our_query = l[k:]


def my_hash(s):
    h = 0
    for c in s:
        h = (h * 1_000_003 + ord(c)) % (2 ** 32)
    return h 

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        self.a = [None] * 5  
        self.count = 0

    def get(self, key):
        index = my_hash(key) % len(self.a)
        p = self.a[index]
        while p != None:
            if p.key == key:
                return p.value
            p = p.next
        return None

    def set(self, key, value):
        # Here we are checking the load factor (this is the part I have problems)
        if (self.count//len(self.a)) >= 4 and self.get(key) == None:   # the fixed-size array is full
            b = [None] * (len(self.a)*2)
            print(f'resizing to {len(b)} buckets')
            counter = 0
            # Here we are trying to realocate the nodes from our self.a to b 
            # depending of the mod(len b) example index-3 in mod 5 might be index-8 in mod 10
            for i in range(len(self.a)):
                y = self.a[i]
                while y != None:
                    index = my_hash(y.key) % len(b)
                    # print(y.key)
                    node = Node(y.key, y.value)
                    node.next = b[index]
                    b[index] = node
                    y = y.next
            self.a = b

        node = Node(key, value)
        index = my_hash(key) % len(self.a)
        if self.get(key) == None:
            node.next = self.a[index]
            self.a[index] = node
            self.count += 1
        else:
            n = self.a[index]
            while n != None:
                if n.key ==  key:
                    n.value = value
                    return
                n = n.next

    def remove(self, key):
        index = my_hash(key) % len(self.a)
        n = self.a[index]
        prev = n
        if self.get(key) is not None:
            # print(key)
            if n.key == key:
                if n.next == None:
                    # print(f'first position of index {index}')
                    self.a[index] = None  
                    return
                else:
                    # print(f'in the loop of the index {index}')
                    n = n.next
                    self.a[index] = n
                    return
            while n.key != key:
                prev = n
                n = n.next
            else:
                if n.next == None:
                    prev.next = n.next
                    return
                else: 
                    n = n.next
                    # print(f'comparison of {key} and his previous {n.key} and the next {prev.key}')
                    prev.next = n
                    return


m = HashMap()
for i in range(len(our_strings)):
    q = m.get(our_strings[i])
    if q == None:
        m.set(our_strings[i], 1)
    else:
        m.set(our_strings[i], q + 1)

print(f'unique words = {m.count}')

for i in range(len(our_query)):
    e = m.get(our_query[i])
    # print(f'We are removing {our_query[i]} with value = {e}')
    if e != None:
        print(f'{our_query[i]} {e}')
        m.remove(our_query[i])
    else:
        print(f'{our_query[i]} None')



