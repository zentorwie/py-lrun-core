
def judge_same(path_a, path_b):
    '''
    Judge two files is the same or not, path_a and path_b are pathnames of both files
    path_a: pathname of file A
    path_b: pathname of file B
    return two variables
    absolute: if two files are absolutely the same
    approximate: if two files are approximately the same
    '''
    fa = open(path_a, 'r')
    fb = open(path_b, 'r')

    try:
        absolute = True
        approximate = True
        while True:
            if not approximate:
                break
            lines_a = fa.readline()
            lines_b = fb.readline()
            if not lines_a and not lines_b:
                break
            if not lines_a or not lines_b:
                absolute = False
                approximate = False
                break

            if lines_a != lines_b:
                absolute = False

            lines_a = lines_a.strip()
            lines_b = lines_b.strip()

            if lines_a != lines_b:
                approximate = False

        return absolute, approximate

    except:
        pass
    finally:
        fa.close()
        fb.close()