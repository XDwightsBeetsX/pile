"""
Cool ways to print data
"""

def show_by_key(dictionary, indent=2, symbol="", separation=True):
    """
    Displays like bullet-points
    """
    if isinstance(dictionary, dict):
        def maxValue(d):
            l_maxK = 0
            for k in d.keys():
                l_new = len(str(d[k]))
                if l_new > l_maxK:
                    l_maxK = l_new
            return l_maxK
        
        sep = ""
        for k, vals in dictionary.items():
            if separation:
                l = indent + len(symbol) + maxValue(dictionary)
                sep = "=" * l
                print(sep)
            print(f"{symbol}{k}")
            for v in vals:
                prefix = " " * indent
                print(f"{prefix}{symbol}{v}")
        print(sep)
    else:
        raise Exception("[INVALID ARGUMENT] show_by_key requires a dict")


def show_linked_list(llist, doubly=False):
    """
    Requires .size/.next/.prev/.data capable list
    """
    sep = "->"
    if doubly:
        sep = "<=>"
    try:
        s = llist.size
        curr = llist.head
        if s > 0:
            curr = curr.next
        for _ in range(s-1):
            print(f"{curr.data}", end=sep)
            curr = curr.next
        print(f"{curr.data}")
    
    except Exception:
        raise Exception("[INVALID ARGUMENT] show_linked_list requires .size/.next/.prev/.data capable list")


def make_square(side_length, char="X"):
    """
    Prints a solid square of size side_length with char='X'
    """
    for _ in range(side_length):
        row = [char for _ in range(side_length)]
        for c in row[:-1]:
            print(f"{c}", end=" ")
        print(f"{row[-1]}")


def make_tree(branch_factor, depth, char="X", gaps=True):
    """
    Prints a tree-like triangle
    """
    c_len = len(char)
    max_w = (c_len) * branch_factor**(depth-1)
    for d in range(0, depth):
        c_count = branch_factor**d
        spaces = round((max_w - (c_count * c_len)) / c_count) + 1
        spacing = " " * spaces
        elements = branch_factor**d
        for i in range(elements):
            if i == 0:
                print("", end=spacing)
            print(f"{spacing}{char}", end=spacing)
            if i == elements-1:
                print(f"{spacing}\n")
        if gaps and d != depth-1:
            print("\n")
