from CreatePic import ImageCreator
from MyCalendar import Calendar

img_template = "E:\CodPractice\pythons\Python\Telegram Bots\My Assistant Calender\img\pic.png"
imgs_products = "E:\CodPractice\pythons\Python\Telegram Bots\My Assistant Calender\Products"
if __name__ == "__main__":
    calendar = Calendar()
    calendar_str = calendar.generate_calendar_str()

    # روزها را به لیست سه‌تایی‌ها تقسیم کنید
    days_list = [day.split("\n") for day in calendar_str.strip().split("\n\n")]

    # ایجاد کننده تصویر با مسیر به قالب و دایرکتوری خروجی
    creator = ImageCreator(img_template,imgs_products)
    creator.create_images_for_days(days_list)
