import datetime as dt
import unittest

from optionslib.types.enums import DayOfWeek, HolidayCalendarId
from optionslib.time.holiday_calendar import HolidayCalendar


class TestHolidayCalendar(unittest.TestCase):
    def test_christmas(self):
        london_calendar = HolidayCalendar(
            DayOfWeek.SATURDAY, DayOfWeek.SUNDAY, HolidayCalendarId.LONDON
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2023, 12, 25)),
            True,
            f"Failed christmas unit test : 25th December, 2023 is the Christmas day holiday!",
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2021, 12, 27)),
            True,
            f"Failed christmas unit test : 27th December, 2021 is the Christmas day holiday!",
        )

    def test_boxing_day(self):
        london_calendar = HolidayCalendar(
            DayOfWeek.SATURDAY, DayOfWeek.SUNDAY, HolidayCalendarId.LONDON
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2023, 12, 26)),
            True,
            f"Failed boxing day unit test : 26th December, 2023 is the boxing day holiday!",
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2021, 12, 28)),
            True,
            f"Failed boxing day unit test : 28th December, 2021 is the boxing day holiday!",
        )

    def test_weekend(self):
        london_calendar = HolidayCalendar(
            DayOfWeek.SATURDAY, DayOfWeek.SUNDAY, HolidayCalendarId.LONDON
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2023, 12, 9)),
            True,
            f"Failed weekend unit test : 09th Dec, 2023 falls on saturday and must be a holiday!",
        )

    def test_spring_day(self):
        london_calendar = HolidayCalendar(
            DayOfWeek.SATURDAY, DayOfWeek.SUNDAY, HolidayCalendarId.LONDON
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2024, 5, 27)),
            True,
            f"Failed spring day unit test : 27th May, 2024 was spring day and must be a holiday!",
        )

    def test_early_may(self):
        london_calendar = HolidayCalendar(
            DayOfWeek.SATURDAY, DayOfWeek.SUNDAY, HolidayCalendarId.LONDON
        )

        self.assertEqual(
            london_calendar.is_holiday(dt.date(2024, 5, 6)),
            True,
            f"Failed early may day unit test : 06th May, 2024 was early may day and must be a holiday!",
        )
