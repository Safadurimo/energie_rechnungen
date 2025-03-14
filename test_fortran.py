import unittest
from fortran import sgerg88, sgerg1

class TestSgerg88(unittest.TestCase):
    def test_sgerg88_valid_parameters(self):
        try:
            sgerg88(1.0, 1.0, 1.0, 1.0, 1.0, 50.0, 20.0, 0.9, 0.8)
        except Exception as e:
            self.fail(f"sgerg88 raised {e} unexpectedly!")

    def test_sgerg88_pressure_out_of_range(self):
        with self.assertRaises(ValueError) as context:
            sgerg88(1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 20.0, 0.9, 0.8)
        self.assertEqual(str(context.exception), 'PRESSURE OUT OF RANGE')

        with self.assertRaises(ValueError) as context:
            sgerg88(1.0, 1.0, 1.0, 1.0, 1.0, 121.0, 20.0, 0.9, 0.8)
        self.assertEqual(str(context.exception), 'PRESSURE OUT OF RANGE')

    def test_sgerg88_temperature_out_of_range(self):
        with self.assertRaises(ValueError) as context:
            sgerg88(1.0, 1.0, 1.0, 1.0, 1.0, 50.0, -24.0, 0.9, 0.8)
        self.assertEqual(str(context.exception), 'TEMPERATURE OUT OF RANGE')

        with self.assertRaises(ValueError) as context:
            sgerg88(1.0, 1.0, 1.0, 1.0, 1.0, 50.0, 66.0, 0.9, 0.8)
        self.assertEqual(str(context.exception), 'TEMPERATURE OUT OF RANGE')

if __name__ == '__main__':
    unittest.main()