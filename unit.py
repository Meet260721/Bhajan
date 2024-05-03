import unittest
from main import duration_time
from validation import is_valid_integer,is_valid_email, is_valid_username, is_valid_special_character,is_valid_alpha,is_valid_date


class TestCode(unittest.TestCase):

    #Test cases for duration time conversion from MS to Minute and Second
    def test_duration_time(self):
        # Test conversion from milliseconds to minutes
        self.assertEqual(duration_time(0), "0:00")
        self.assertEqual(duration_time(60000), "1:00")  # 60,000 ms = 1 minute
        self.assertEqual(duration_time(90000), "1:30")  # 90,000 ms = 1 minute and 30 seconds
        self.assertEqual(duration_time(180000), "3:00")  # 180,000 ms = 3 minutes

    # Test cases for is_valid_integer check function
    def test_integer(self):
        self.assertEqual(is_valid_integer(10),True)
        self.assertEqual(is_valid_integer("mike"),False)
        self.assertEqual(is_valid_integer('mike21'),False)
        self.assertEqual(is_valid_integer(34.23), False)
        self.assertEqual(is_valid_integer(False), True)

    # Test cases for is_valid_email check function
    def test_email(self):
        self.assertEqual(is_valid_email("mike434@gmail.com"),True)
        self.assertEqual(is_valid_email("mike23234@gmailcom"), False)
        self.assertEqual(is_valid_email("mufe4334gmail.com"), False)
        # self.assertEqual(is_valid_email(45653546646), False)

    # Test cases for is_valid_username check function
    def test_username(self):
        self.assertEqual(is_valid_username("ffdfs_3425"),True)
        self.assertEqual(is_valid_username("ffdfs3425"),True)
        self.assertEqual(is_valid_username("me457"),False)
        self.assertEqual(is_valid_username("pafdg@6553"),False)
        # self.assertEqual(is_valid_username(335342), False)

    # Test cases for is_valid_special_character check function
    def test_specChar(self):
        self.assertTrue(is_valid_special_character("Mreer@#|(pasff23)"))
        self.assertFalse(is_valid_special_character("Mt_09"))
        self.assertTrue(is_valid_special_character("Mt_0%^9"))
        # self.assertFalse(is_valid_special_character(231432124))

    # Test cases for is_valid_alpha check function
    def test_alpha(self):
        self.assertTrue(is_valid_alpha("Masf. rutgrds"))
        self.assertFalse(is_valid_alpha("dvsv.23gdgvd"))
        self.assertFalse(is_valid_alpha("dvdv@#rgrgs"))
        # self.assertFalse(is_valid_alpha(4555532))

    # Test cases for is_valid_date check function
    def test_date(self):
        self.assertTrue(is_valid_date("2023-12-21"))
        self.assertFalse(is_valid_date("2026-12-21"))
        self.assertFalse(is_valid_date("2023-2-30"))
        self.assertFalse(is_valid_date("20-12-2021"))
        self.assertFalse(is_valid_date("2023-02-29"))
        # self.assertFalse(is_valid_date(435455565))

# If you are running this code as a script, this block will execute the tests
if __name__ == '__main__':
    unittest.main()
