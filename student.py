from datetime import date, timedelta
import requests


class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        # the _ before first_name below lets other develops know it's
        # a read only property (ie that the property can't be updated
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def apply_extension(self, days_added):
        self.end_date = self.end_date + timedelta(days=days_added)

    def course_schedule(self):
        response = requests.get(
            f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request"