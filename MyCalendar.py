import datetime
import jdatetime
from bidi.algorithm import get_display
import arabic_reshaper

class Calendar:
    def __init__(self):
        self.today = datetime.date.today()
        self.jtoday = jdatetime.date.today()
        
        self.weekdays_fa = {
            'Saturday': 'شنبه',
            'Sunday': 'یک‌شنبه',
            'Monday': 'دو‌شنبه',
            'Tuesday': 'سه‌شنبه',
            'Wednesday': 'چهار‌شنبه',
            'Thursday': 'پنج‌شنبه',
            'Friday': 'جمعه'
        }
        
        self.months_fa = {
            'January': 'ژانویه',
            'February': 'فوریه',
            'March': 'مارس',
            'April': 'آوریل',
            'May': 'مه',
            'June': 'ژوئن',
            'July': 'ژوئیه',
            'August': 'اوت',
            'September': 'سپتامبر',
            'October': 'اکتبر',
            'November': 'نوامبر',
            'December': 'دسامبر'
        }
    
    def get_days_in_next_30_days(self):
        start_date = self.today
        end_date = self.today + datetime.timedelta(days=30)
        delta = datetime.timedelta(days=1)
        
        days = []
        while start_date <= end_date:
            days.append(start_date)
            start_date += delta
        return days

    def generate_calendar_str(self) -> str:
        days_in_period = self.get_days_in_next_30_days()

        result = []
        
        for day in days_in_period:
            jdate = jdatetime.date.fromgregorian(date=day)
            
            # ایجاد رشته تاریخ با فاصله‌های اضافی
            jalali_day_str = f"{jdate.day}       {jdate.j_months_fa[jdate.month-1]}       {jdate.year}"
            gregorian_month_fa = self.months_fa[day.strftime('%B')]
            gregorian_day_str = f"{day.day}       {gregorian_month_fa}       {day.year}"
            
            weekday_fa = self.weekdays_fa[day.strftime('%A')]
            
            # Reshape و راست‌چین کردن متن
            jalali_day_str = get_display(arabic_reshaper.reshape(jalali_day_str))
            weekday_fa = get_display(arabic_reshaper.reshape(weekday_fa))
            gregorian_day_str = get_display(arabic_reshaper.reshape(gregorian_day_str))
            
            entry = f"{weekday_fa}\n{jalali_day_str}\n{gregorian_day_str}\n"
            result.append(entry)
        
        return '\n'.join(result)
