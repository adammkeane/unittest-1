import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    def setUp(self):
        print('setUp')
        self.student = Student("Adam", "Smith")
 
    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, "Adam Smith")

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, "adam.smith@email.com")

    def test_apply_extension(self):
        print('test_apply_extension')
        old_date = self.student.end_date
        self.student.apply_extension(4)
        self.assertEqual(self.student.end_date, old_date + timedelta(days=4))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_fail(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request")

if __name__ == '__main__':
    unittest.main()