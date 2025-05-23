class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None] * self.size

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """
        Return a hashed location using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - The largest value to be returned will be less than size.   
        Remember to compress the return value to fit the table size.
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """
        p = 31
        m = 10^9 + 9
        hashvalue = 0
        i = 1
        while i < len(key):
            charvalue = ord(key[i]) - ord('a') + 1
            hashvalue = hashvalue + (charvalue * (p^i))
            i += 1
        hashvalue = hashvalue % m
        return hashvalue % self.size


    def setitem(self, key: str, value: dict) -> None:
        """
        adds or updates an item and displays an appropriate message
        """
        hashvalue = self._hash(key)
        if self.values[hashvalue] == None:
            self.values[hashvalue] = value
            print('Data successfully added.')
        else:
            self.values[hashvalue] = value
            print('Data successfully updated.')

    def getitem(self, key: str) -> 'dict | None':
        """
        returns an item in the hashtable, prints an error message if destination is empty and return None
        """
        hashvalue = self._hash(key)
        if self.values[hashvalue] == None:
            print('Destionation is empty')
            return None
        else:
            return self.values[hashvalue]
        
    def delitem(self, key: str) -> None:
        """
        removes the item from the destination, prints error message if destination is empty or otherwise
        """
        hashvalue = self._hash(key)
        if self.values[hashvalue] == None:
            print('Unable to remove. Destination is empty.')
        else:
            self.values[hashvalue] = None
            print('Data successfully removed.')