import unittest
from main import duration_min, duration_sec  # Import your functions here

class TestCode(unittest.TestCase):

    def test_duration_min(self):
        # Test conversion from milliseconds to minutes
        self.assertEqual(duration_min(0), 0)
        self.assertEqual(duration_min(60000), 1)  # 60,000 ms = 1 minute
        self.assertEqual(duration_min(90000), 1)  # 90,000 ms = 1 minute and 30 seconds
        self.assertEqual(duration_min(180000), 3)  # 180,000 ms = 3 minutes

    def test_duration_sec(self):
        # Test conversion from milliseconds to seconds
        self.assertEqual(duration_sec(0), 0)
        self.assertEqual(duration_sec(1000), 1)  # 1 second
        self.assertEqual(duration_sec(61000), 1)  # 1 second (after one minute)
        self.assertEqual(duration_sec(90500), 30)  # 30 seconds (after one minute and 30 seconds)

# If you are running this code as a script, this block will execute the tests
if __name__ == '__main__':
    unittest.main()
