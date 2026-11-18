
import unittest
from delivery import ExpressCreator, FreeCoupon

class TestDelivery(unittest.TestCase):

    def test_express_fee(self):
        delivery = ExpressCreator().create_delivery()
        self.assertEqual(delivery.get_fee(), 70)

    def test_valid_coupon(self):
        delivery = ExpressCreator().create_delivery()
        delivery.set_strategy(FreeCoupon())
        self.assertEqual(delivery.get_fee(), 0)

if __name__ == "__main__":
    unittest.main()
