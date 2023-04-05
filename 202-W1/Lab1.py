def indexOf(text, str, index=0):
    if index > len(text) - len(str):
        return -1 # substring not found
    if text[index:index+len(str)] == str:
        return index # substring found
    return indexOf(text, str, index+1) # recursive call

def sqrt(x, g=100):
    if x < 0:
        raise ValueError("Input cannot be negative")
    if abs(x-g**2) < 0.0000001:
        return g
    return sqrt(x,(g + x/g)/ 2)

