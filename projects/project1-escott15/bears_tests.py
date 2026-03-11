import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_40(self):
        self.assertFalse(bears(40))
    
    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    def test_bears_84(self):
        self.assertTrue(bears(84))

    def test_bears_41(self):
        self.assertFalse(bears(41))  

    def test_bears_250(self):
        self.assertTrue(bears(250))
        
    def test_bears_40(self):
        self.assertFalse(bears(40))

    # Base / below-base behavior
    def test_bears_41(self):
        self.assertFalse(bears(41))

  
    def test_bears_168(self):
        self.assertTrue(bears(168)) 

    
    def test_bears_210(self):
        self.assertTrue(bears(210)) 


    def test_bears_96(self):
        self.assertTrue(bears(96))

    def test_bears_52(self):
        self.assertTrue(bears(52))   

    def test_bears_100(self):
        self.assertFalse(bears(100))  


if __name__ == "__main__":
    unittest.main()
