s = set()

def permutate(titles, tmp):
    if titles == "":
        if tmp != "":
            s.add(tmp)
    else:
        for i in range(len(titles)):
            permutate(titles[:i]+titles[i+1:], tmp+titles[i])    
            permutate(titles[:i]+titles[i+1:], tmp)




def numTilePossibilities(tiles):
    """
    :type tiles: str
    :rtype: int
    """
    permutate(tiles, "")
    return s


print(numTilePossibilities("AAB"))