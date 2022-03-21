import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
   def test_is_five_prime(self):    
      self.assertTrue(is_prime(5)) 
   def test_is_nine_prime(self):
      self.assertFalse(is_prime(9))
   def test_is_negative_prime(self):
      self.assertFalse(is_prime(-1))
   def test_is_zero_prime(self):
      self.assertFalse(is_prime(0))
   def test_is_one_prime(self):
      self.assertFalse(is_prime(1))
   def test_is_two_prime(self):
      self.assertTrue(is_prime(2))
   def test_is_decimal_treated(self):
      self.assertFalse(is_prime(5.2))
   def test_is_decimal_treated(self):
     self.assertFalse(is_prime("5"))

if __name__ == '__main__':
	unittest.main()
