import bisect

def solve(value):
    return bisect.bisect_right(value["items"], value["target"])
