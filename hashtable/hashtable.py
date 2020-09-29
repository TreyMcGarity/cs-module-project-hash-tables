class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        self.buckets = [None] * self.capacity
        # counter to keep track of number of items in table
        self.counter = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        #number of slots is length of capacity
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # length of elements divided by length of capacity
        return self.counter / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381 
        # Just a "magic" number that, in testing,
        # resulted in fewer collisions and better avalanching.
        for i in key:
            hash = (( hash << 5) + hash) + ord(i)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.counter += 1
        index = self.hash_index(key)
        current = self.buckets[index]
        # if nothing is at this index

        # if load_factor >= 0.7
        if self.get_load_factor() >= 0.7:
            # call resize that doubles length of buckets
            self.resize(len(self.buckets) * 2)

        if self.buckets[index] is None:
            # at hashed index insert a node with key, value pair
            self.buckets[index] = HashTableEntry(key, value)

        # loop through index's Linked List
        while current is not None:
            # if key is found
            if current.key == key:
                # set inputed value to node's value
                current.value = value
                break
            # if next node is nothing
            if current.next is None:
                # set current's next to inputed node
                current.next = HashTableEntry(key, value)
                break
            # continue to current's next
            current = current.next



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.buckets[index]

        # loop through index's Linked List
        while current is not None:
            # if key is found
            if current.key == key:
                # nullify/remove value
                current.value = None
                self.counter -= 1
                break
            # no key found, print message
            if current.next is None and current.key != key:
                return print("Key not found.")
            # continue to current's next
            current = current.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.buckets[index]

        # loop through index's Linked List
        while current is not None:
            # if no next node and no 
            if current.next is None and current.key != key:
                return
            # if key is found
            if current.key == key:
                # return value of node
                return current.value
            # continue to current's next
            current = current.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # make a new array of double elements
        old_table = self.buckets
        # traverse each entry of old array and add to new
        self.buckets = [None] * new_capacity

        for item in old_table:
            # if there is a value
            if item is not None:
                # make new index for new table
                new_index = self.hash_index(item.key)
                self.buckets[new_index] = item

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
