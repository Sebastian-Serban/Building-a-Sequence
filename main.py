import unittest


def proc_seq(*args):
    res = [int(i) for i in recursive_combine(args) if i[0] != "0"]
    res_clean = list(set(res))
    return sorted(list(set([len(res_clean), min(res_clean), max(res_clean), sum(res_clean)])))


def recursive_combine(args, prefix='', res=None):
    if res is None:
        res = []
        args = [str(i) for i in args]
    if not args:
        res.append(prefix)
        return res
    for char in args[0]:
        recursive_combine(args[1:], prefix + char, res)
    return res


class TestProcSeq(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(proc_seq(23, 17, 89), [8, 218, 379, 2388])

        self.assertEqual(proc_seq(22, 22, 22, 22), [1, 2222])

        self.assertEqual(proc_seq(230, 15, 8), [4, 218, 358, 1152])


if __name__ == "__main__":
    unittest.main()
