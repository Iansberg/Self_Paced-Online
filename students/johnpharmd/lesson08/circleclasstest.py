import circle_class as cc
import unittest
import math


class CircleTest(unittest.TestCase):
    """tests circle attributes"""

    def setUp(self):
        self.test = cc.Circle(5)

    def test_circle_radius(self):
        self.assertEqual(self.test.radius, 5)

    def test_circle_diameter(self):
        self.assertEqual(self.test.diameter, 10)
        self.test.diameter = 8
        self.assertEqual(self.test.diameter, 8)
        self.assertEqual(self.test.radius, 4)

    def test_circle_area(self):
        self.assertEqual(self.test.area, math.pi * self.test.radius ** 2)

    def test_circle_from_diameter(self):
        self.assertEqual(self.test.from_diameter(), 10)
        self.assertTrue(self.test.radius == 5)

    def test_circle_str(self):
        self.assertEqual(self.test.__str__(), 'Circle with radius: ' +
                         str(5))

    def test_circle_repr(self):
        self.assertEqual(self.test.__repr__(), 'Circle(5)')

    def test_circle_num_protocol(self):
        self.new_test = cc.Circle(3)
        self.assertEqual(self.test + self.new_test, 'Circle(8)')
        self.assertEqual(self.test * 3, 'Circle(24)')
        self.assertEqual(3 * self.test, 'Circle(72)')
