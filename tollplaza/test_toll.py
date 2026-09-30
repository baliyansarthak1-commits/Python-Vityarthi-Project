# Unit tests for the Toll Booth Management System
# Run with:  python -m unittest test_toll -v
import unittest

import booth
import records
from pricing import get_toll, rates
from rules import is_exempt
from reports import cash_alert, CASH_LIMIT, ALERT_MSG, SAFE_MSG


class TestPricing(unittest.TestCase):
    def test_single_rates(self):
        self.assertEqual(get_toll("Car", "Single"), 100)
        self.assertEqual(get_toll("Bus", "Single"), 200)
        self.assertEqual(get_toll("Truck", "Single"), 300)

    def test_return_rates(self):
        self.assertEqual(get_toll("Car", "Return"), 150)
        self.assertEqual(get_toll("Truck", "Return"), 350)

    def test_unknown_vehicle_is_zero(self):
        self.assertEqual(get_toll("AutoRickshaw", "Single"), 0)


class TestExemption(unittest.TestCase):
    def test_ambulance_plate(self):
        self.assertTrue(is_exempt("KA01AMB99"))

    def test_vip_plate(self):
        self.assertTrue(is_exempt("DL1VIP001"))

    def test_lowercase_plate(self):
        self.assertTrue(is_exempt("ka01amb99"))

    def test_normal_plate(self):
        self.assertFalse(is_exempt("MH12AB1234"))


class TestCountsAndRecords(unittest.TestCase):
    def setUp(self):
        # counts and receipts are shared, so reset them before every test
        for v in booth.counts:
            booth.counts[v] = 0
        records.receipts.clear()

    def test_update_count(self):
        booth.update_count("Car")
        booth.update_count("Car")
        booth.update_count("Bus")
        self.assertEqual(booth.counts, {"Car": 2, "Bus": 1, "Truck": 0})

    def test_invalid_type_not_counted(self):
        booth.update_count("Tractor")
        self.assertNotIn("Tractor", booth.counts)

    def test_total_cash_empty(self):
        self.assertEqual(records.get_total_cash(), 0)

    def test_total_cash_with_receipts(self):
        records.add_receipt("MH12AB1234", "Car", 150)
        records.add_receipt("KA01AMB99", "Exempt", 0)
        records.add_receipt("MH09CD5678", "Bus", 200)
        self.assertEqual(records.get_total_cash(), 350)
        self.assertEqual(len(records.receipts), 3)


class TestCashAlert(unittest.TestCase):
    def test_safe_below_limit(self):
        self.assertEqual(cash_alert(350), SAFE_MSG)

    def test_alert_at_limit(self):
        self.assertEqual(cash_alert(CASH_LIMIT), ALERT_MSG)

    def test_alert_above_limit(self):
        self.assertEqual(cash_alert(2100), ALERT_MSG)


if __name__ == "__main__":
    unittest.main()
