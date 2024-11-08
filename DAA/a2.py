# huffman coding

import heapq


class Node:
    def __init__(self, freq, sym, code='') -> None:
        self.freq = freq
        self.code = code
        self.sym = sym
        self.left = None
        self.right = None

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def traverse(node: Node, code: str, table):
    if node == None:
        return table
    if node.left == None and node.right == None:
        table[node.sym] = code
        return table
    table = traverse(node=node.left, code=code+'0', table=table)
    table = traverse(node=node.right, code=code+'1', table=table)
    return table


def huffman_encode(msg):
    # count
    cnt = dict()
    for i in msg:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    # build tree
    count_arr = []

    for k in cnt:
        heapq.heappush(count_arr, Node(cnt[k], k))

    while len(count_arr) > 1:

        a = heapq.heappop(count_arr)
        b = heapq.heappop(count_arr)

        newNode = Node(freq=a.freq + b.freq, sym=None)
        newNode.left = a
        newNode.right = b

        heapq.heappush(count_arr, newNode)

    # traverse and assign codes to leaf
    table = traverse(node=count_arr[0], code='', table={})

    print(table)

    original_size = 0
    compressed_size = sum([8+len(table[k]) for k in table])

    for k in cnt:
        original_size += cnt[k] * 8
        compressed_size += cnt[k] * len(table[k])

    print('Size before compression = ', original_size)
    print('Size after compression = ', compressed_size)
    print('%Compression = ' +
          str((abs(original_size-compressed_size)/original_size) * 100) + "%")

    sent_msg = ''
    for i in msg:
        sent_msg += table[i]

    return sent_msg, count_arr[0]


def huffman_decode(msg, root: Node):
    decoded_msg = ''
    current_node = root

    for bit in msg:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_msg += current_node.sym
            current_node = root

    return decoded_msg


msg, rt = huffman_encode('hello world')
print('Message sent = ', msg)

decoded_msg = huffman_decode(msg=msg, root=rt)
print('Decoded message = ', decoded_msg)
