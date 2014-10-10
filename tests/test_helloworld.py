import unittest

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        pass

    def test_HelloWorld(self):
        try:
            print HelloWorld
        except:
            pass       
if __name__ == '__main__':
    unittest.main()
