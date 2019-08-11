def filter_if(l, f):
    # The one-liner: see
    # https://docs.python.org/2.7/tutorial/datastructures.html#list-comprehensions
    #
    #     return [x for x in l if f(x)]
    #
    # Or, as a maybe-simpler loop:
    result = []
    for x in l:
        if f(x):
            result.append(x)
    return result
