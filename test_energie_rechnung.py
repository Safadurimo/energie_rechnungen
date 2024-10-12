import unittest
from datetime import datetime
from energie_rechnung import calculate_energy_bill

class TestCalculateEnergyBill(unittest.TestCase):
    def test_calculate_energy_bill(self):
        rechnung = calculate_energy_bill(
            2, 
            2, 
            datetime.fromisoformat('2024-01-01'),
            datetime.fromisoformat('2024-12-31')
            )
        self.assertEqual(rechnung.rechnungssumme, 4)


if __name__ == '__main__':
    unittest.main()

