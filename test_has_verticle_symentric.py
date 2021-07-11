import unittest

from main import has_vertical_symentric_line

class TestVerticalSymetric(unittest.TestCase):

  symentrical_coordinates =  [(-2, 5), (2, 5), (4, 3), (-4, 3)] 
  non_symentrical_coordinates =  [(2, 5), (2, 5), (4, 3), (-4, 3)] 

  def test_has_vertical_symentric_line(self):
      answer = has_vertical_symentric_line(self.symentrical_coordinates)
      self.assertEqual(answer, 'Yes')

  def test_has_no_vertical_symentric_line(self):
      answer = has_vertical_symentric_line(self.non_symentrical_coordinates)
      self.assertEqual(answer, 'No')


if __name__ == '__main__':
  unittest.main()