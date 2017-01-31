
def judge_same(path_a, path_b):
    "Judge two files is the same or not, path_a and path_b are pathnames of both files"
    fa = open(path_a, 'r')
    fb = open(path_b, 'r')

    try:
        lines_a = fa.readlines()
        lines_b = fb.readlines()
        length = len(lines_a)
        if length != len(lines_b):
            return False
        for i in range(length):
            if lines_a[i] != lines_b[i]:
                return False
        return True
    finally:
        fa.close()
        fb.close()