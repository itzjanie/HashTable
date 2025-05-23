from hashtable import HashTable

if __name__ == "__main__":
    ht = HashTable(30)
    with open('student_data.csv', 'r') as fhand:
        fhand.readline()
        for line in fhand:
            line = line.strip().split(',')
            ht.setitem(line[1], line)
    print(ht)
    print(ht.getitem('s0039e'))
    ht.delitem('s0040f')
    print(ht)
    """
    1. Extract the records from the student_data file
    and add them one at a time, as a Python dict, 
    containing the name, class and their associated
    data as key-value dict pairs, to the hashtable
    
    2. You can use the id as the hash table key for 
    each of the above records.
    """
    
    # Test your hashtable using appropriate methods
    # from your implementation
    
    