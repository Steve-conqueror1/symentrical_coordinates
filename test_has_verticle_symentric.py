import unittest

from main import has_vertical_symentric_line, get_max_and_min_value

class TestVerticalSymetric(unittest.TestCase):

  symentrical_coordinates =  [(-2, 5), (2, 5), (4, 3), (-4, 3)] 
  non_symentrical_coordinates =  [(2, 5), (2, 5), (4, 3), (-4, 3)] 

  def test_has_vertical_symentric_line(self):
      answer = has_vertical_symentric_line(self.symentrical_coordinates)
      self.assertEqual(answer, 'Yes')

  def test_has_no_vertical_symentric_line(self):
      answer = has_vertical_symentric_line(self.non_symentrical_coordinates)
      self.assertEqual(answer, 'No')

  def test_get_max_and_min_value(self):
      min, max = get_max_and_min_value(self.symentrical_coordinates, self.symentrical_coordinates[0][0], self.symentrical_coordinates[0][0], 0)
      self.assertEqual(min, -4)
      self.assertEqual(max, 4)


if __name__ == '__main__':
  unittest.main()