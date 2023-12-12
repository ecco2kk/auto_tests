from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
import circle

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser

class CircleTest(unittest.TestCase):
    ''' модуль UNITTEST, проверяющий корректность вычислений функции вычисления площади круга'''
    def test_area_1(self):
        res = circle.area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_area_2(self):
        res = circle.area(0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_area_3(self):
        res = circle.area(-2)
        self.assertEqual(res, 'Invalid input')

    def test_area_4(self):
        res = circle.area('qw')
        self.assertEqual(res, 'Invalid input')

    def test_area_5(self):
        res = circle.area(True)
        self.assertEqual(res, 'Invalid input')

    ''' модуль UNITTEST, проверяющий корректность вычислений функции вычисления площади круга'''
    def test_perimeter_1(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_perimeter_2(self):
        res = circle.perimeter(0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_3(self):
        res = circle.perimeter(-2)
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_4(self):
        res = circle.perimeter('qw')
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_5(self):
        res = circle.perimeter(True)
        self.assertEqual(res, 'Invalid input')


if __name__ == '__main__':
    unittest.main()