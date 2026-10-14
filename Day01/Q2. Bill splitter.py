# 1. Count how many names were passed (len of names).
# 2. If no names, return an empty dict.
# 3. share = total / count.
# 4. Create a dict by looping over names, with each name getting share.
# 5. Return the dict. Call it with 2 names, then with 4.


def split_bill(total, *names):
    """split_bill(total, *names) that returns a dict of {name: share} with the bill divided equally."""
    count = len(names)
    
    if count == 0:
        return{}

    share = total/ count
    result = {}
    
    for name in names:
        
        result[name] = share
    
    return result
        

if __name__ == "__main__":
    print(split_bill(1000, "Amit", "Riya"))