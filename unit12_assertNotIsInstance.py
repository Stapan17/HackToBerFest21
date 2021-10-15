import unittest

# Method assertNotIsInstance()
# UnitTestBy Hathaipach I.


class Empclass:
    Name = "Maria"
    Birthday = "10-Dec-1997"
    Garden = "Male"


class TestClass(unittest.TestCase):
    # test function to test whether obj is instance of class
    def test_positive(self):
        objectName = "Bangkok"
        # error message in case if test case got failed
        message = "An object is instance of Empclass."
        self.assertNotIsInstance(objectName, Empclass, message)


if __name__ == "__main__":
    unittest.main()
