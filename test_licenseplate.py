import unittest

from licenseplate import LicensePlate

VALID_PLATES = [
    'XX-99-99',
    '99-99-XX',
    '99-XX-99',
    'XX-99-XX',
    'XX-XX-99',
    '99-XX-XX',
    '99-XXX-9',
    '9-XXX-99',
    'XX-999-X',
    'X-999-XX'
]

class TestLicensePlate(unittest.TestCase):
    def test_valid(self):
        plate = LicensePlate('99-XX-99')
        self.assertTrue(plate)

    def test_invalid(self):
        self.assertRaises(ValueError, LicensePlate, 'appeltaart')

    def test_normalized(self):
        plate = LicensePlate('99-XX-99')
        self.assertEqual('99XX99', plate.normalized)

    def test_formatted(self):
        plate = LicensePlate('99XX99')
        self.assertEqual('99-XX-99', plate.formatted)

    def test_str(self):
        plate = LicensePlate('99XX99')
        self.assertEqual('99-XX-99', str(plate))


if __name__ == '__main__':
    unittest.main()
