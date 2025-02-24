"""
Implementation of A Hash Table Data Structure

"""

class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.load = 0
        self.skip = 3
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __str__(self):
        table_str = f"index| key | values\n"
        for i in range(self.size):
            table_str += f"{i}| {self.keys[i]} | {self.values[i]}\n"
        return table_str
    
    def __setitem__(self, key,value):
        try:
            self.insert(key, value)
        except Exception as e:
            print(e)
   
    def __getitem__(self,key):
        try:
            return self.get(key)
        except Exception as e:
            print(e)
            return ''

    def insert(self,key,value):
        """
        Inserts a key,value pair into the hash table
        Args:
            key: (str)
            value: (str)
        Returns:
            None
        """
        if self.load+1 > self.size:
            raise Exception(f"Hash table ran out of space. Cannot insert key:'{key}'")
        
        index = self.hash(key)
        while self.keys[index]:
            index = self.rehash(index)

        self.keys[index] = key
        self.values[index] = value
        self.load += 1
    
    def get(self, key):
        index = self.hash(key)
        for i in range(self.size):
            if self.keys[index] == key:
                return self.values[index]
            index = self.rehash(index)
        raise Exception(f"Unable to find key '{key}' in hash table")

    def hash(self,key):
        """
        Generates a hash for a given key, which will be the index the key and value will be stored in.
        Use a mid-square hash.
        Args:
            key: (str)
        Returns:
            (int): hash value 
        """
        key_ord = sum([ord(char) for char in key])
        hash = key_ord % self.size
        return hash
        
    def rehash(self, oldhash):
        rehash = (oldhash+self.skip)% self.size
        return rehash




if __name__ == "__main__":
    h_table = HashTable(11)
    h_table["cat"] = 50
    h_table["dog"] = 100
    h_table["bunny"] = 20
    h_table["hamster"] = 10
    h_table["parakeet"] = 25
    h_table["parrot"] = 300
    print(h_table)
    print(h_table["bunny"])
    print(h_table["lizard"])