import unittest
import json
from test import costOfTrip

class TestCostOfTrip(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('interchanges.json', 'r') as f:
            cls.data = json.load(f)

    def test_cost_of_trip_same_locations(self):
        with self.assertRaises(ValueError):
            costOfTrip('QEW', 'QEW')

    def test_cost_of_trip_invalid_locations(self):
        with self.assertRaises(ValueError):
            costOfTrip('Invalid Location', 'Highway 400')

    def test_cost_of_trip_valid_locations(self):
        costOfTrip('Salem Road', 'QEW')
        costOfTrip('QEW', 'Salem Road')
        costOfTrip('QEW', 'Highway 400')
        costOfTrip('Highway 27', 'Dufferin Street')


if __name__ == '__main__':
    unittest.main()