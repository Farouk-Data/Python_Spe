# Min FUnction
def min(values) :
    min = None
    for i in values :
        if min is None or i < min :
            min = i
    return min
