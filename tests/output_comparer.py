"""
Finds differences in ouputs
"""


def compare(string1, string2, report=False):
    same = True
    diff = []
    l = len(string1)

    for i in range(l):
        c1 = string1[i]
        c2 = string2[i]
        if c1 != c2:
            same = False
            if report:
                diff.append(f"[DIFF @ i={i}]: {c1} != {c2}")
    if report:
        print("[REPORT]:")
        print(string1)
        print(string2)
        for err in diff:
            print(err)
    
    return same
