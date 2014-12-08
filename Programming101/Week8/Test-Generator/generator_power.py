boilerplate = """import unittest
{imports}


class {class_name}(unittest.TestCase):
    {ClassDescription}
{test_cases}
if __name__ == '__main__':
    unittest.main()
"""

testcase_boilerplate = """    def TestCase{x}(self):
        self.assert{bool}({method}, {ErrorMessage})
"""
