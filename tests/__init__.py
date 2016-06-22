import unittest


class CodeWordsTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(CodeWordsTests)
    unittest.TextTestRunner().run(suite)
