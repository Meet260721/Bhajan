import unittest
from main import duration_time # Import your functions here


class TestCode(unittest.TestCase):

    def test_duration_time(self):
        # Test conversion from milliseconds to minutes
        self.assertEqual(duration_time(0), 0)
        self.assertEqual(duration_time(60000), 1)  # 60,000 ms = 1 minute
        self.assertEqual(duration_time(90000), 1)  # 90,000 ms = 1 minute and 30 seconds
        self.assertEqual(duration_time(180000), 3)  # 180,000 ms = 3 minutes

# If you are running this code as a script, this block will execute the tests
if __name__ == '__main__':
    unittest.main()


