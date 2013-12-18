__author__ = 'b543840'

from Node import Node

counter = 0

n0 = None
n1 = None
n2 = None
n3 = None
n4 = None
n5 = None
n6 = None
n7 = None
n8 = None

node_array = None

combinations = {}

def make_nodes():
    # 0 1 2
    # 3 4 5
    # 6 7 8

    n0 = Node(0, [1, 3, 4, 5, 7], {1:2, 3:6, 4:8})
    n1 = Node(1, [0, 2, 3, 4, 5, 6, 8], {4:7})
    n2 = Node(2, [1, 3, 4, 5, 7], {1:0, 4:6, 5:8})
    n3 = Node(3, [0, 1, 2, 4, 6, 7, 8], {4:5})
    n4 = Node(4, [0, 1, 2, 3, 4, 5, 6, 7, 8], {})
    n5 = Node(5, [0, 1, 2, 4, 6, 7, 8], {4:3})
    n6 = Node(6, [1, 3, 4, 5, 7], {3:0, 4:2, 7:8})
    n7 = Node(7, [0, 2, 3, 4, 5, 6, 8], {4:1})
    n8 = Node(8, [1, 3, 4, 5, 7], {4:0, 5:2, 7:6})
    global node_array
    node_array = [n0, n1, n2, n3, n4, n5, n6, n7, n8]

def compress(array):
    number = ""
    for i in range(0, len(array)):
        number += str(array[i])
    return number

def rf(array, next):
    print array
    global counter
    global combinations
    if next == 9:
        for i in range(0, len(array)):
            if array[i] == 0:
                array[i] = next
        counter += 1
        print "Reached the end : " + str(array)
        combinations[compress(array)] = 1
        return
    new_arrays = make_new_arrays(array, next)
    for i in range(0, len(new_arrays)):
        if next >= 4:
            counter += 1
            combinations[compress(new_arrays[i])] = 1
        rf(new_arrays[i], next + 1)

def make_new_arrays(array, next):
    new_arrays = []
    global node_array
    for i in range(0, len(array)):
        if array[i] == next - 1:
            last_visited_node = node_array[i]
            for relation in last_visited_node.get_direct_rel():
                if array[relation] == 0:
                    new_array = list(array) #copy array, not reference
                    new_array[relation] = next
                    new_arrays.append(new_array)

    return new_arrays

if __name__ == "__main__":
    # global counter
    # global combinations

    for i in range(0, 9):
        i = 0
        make_nodes()
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        arr[i] = 1
        rf(arr, 1 + 1)



    print "Counter: " + str(counter)
    print "Combinations: " + str(len(combinations))
