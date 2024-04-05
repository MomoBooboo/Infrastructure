import unittest
from trade_producer import send_trade_data

class TestTradeProducer(unittest.TestCase):

    def test_send_trade_data(self):
        # Call the function to send trade data
        response = send_trade_data()
        
        # Check if the response is successful (you can customize this based on your implementation)
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()
