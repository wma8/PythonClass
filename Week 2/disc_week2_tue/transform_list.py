def transform_list(l, f):
    return [f(x) for x in l]

# You can often transform a comprehension like the one above into a
# simple for loop:
#
#     result = []
#     for x in l:
#         result.append(f(x))
#     return result
#
# Likewise, if the loop is simple enough, it's easy to convert to a
# comprehension.  If the code's more complex, the loop syntax may be
# more clear than a super-dense comprehension.
