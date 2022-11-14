    """
    Docstring: this module contain binary search implementation
    """

def binary_search(l, key):
    """_summary_

    Binary search : input a list and key
    return True if key exist else return False
    """
    
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2
        
        if l[mid] == key:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid], key)
        else:
            return binary_search(l[mid+1:], key)
        
