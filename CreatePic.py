from PIL import Image, ImageDraw, ImageFont
import os

class ImageCreator:
    def __init__(self, template_path, output_dir):
        self.template_path = template_path  # مسیر به تصویر قالب
        self.output_dir = output_dir  # مسیر دایرکتوری خروجی
        self.text_color = (2, 48, 71)  # رنگ پیش‌فرض
        self.weekday_color = (255, 255, 255)  # رنگ سفید برای روزهای هفته
        self.font_path = "E:/CodPractice/pythons/Python/Telegram Bots/My Assistant Calender/font/Aviny2.ttf"
        self.font_size = 50

        # اگر پوشه خروجی وجود ندارد، آن را ایجاد کنید
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_image_for_day(self, weekday_fa, jalali_str, gregorian_str, index):
        # بارگذاری تصویر قالب
        image = Image.open(self.template_path)
        draw = ImageDraw.Draw(image)

        # بارگذاری فونت
        font = ImageFont.truetype(self.font_path, self.font_size)

        # موقعیت‌های متن
        weekday_position = (216, 20)  # بالای تصویر
        central_position = (256, 155)  # وسط تصویر برای دو تاریخ

        # نوشتن متن بر روی تصویر
        draw.text(weekday_position, weekday_fa, font=font, fill=self.weekday_color)  # رنگ سفید برای روزهای هفته

        # محاسبه مکان یابی برای تاریخ های مرکزی
        jalali_bbox = draw.textbbox((0, 0), jalali_str, font=font)
        w, h = jalali_bbox[2] - jalali_bbox[0], jalali_bbox[3] - jalali_bbox[1]
        jalali_position = (central_position[0] - w // 2, central_position[1] - h // 2)
        draw.text(jalali_position, jalali_str, font=font, fill=self.text_color)

        gregorian_bbox = draw.textbbox((0, 0), gregorian_str, font=font)
        w, h = gregorian_bbox[2] - gregorian_bbox[0], gregorian_bbox[3] - gregorian_bbox[1]
        gregorian_position = (central_position[0] - w // 2, central_position[1] + 40)
        draw.text(gregorian_position, gregorian_str, font=font, fill=self.text_color)

        # ذخیره تصویر
        image_name = f"day_{index}.png"
        image.save(os.path.join(self.output_dir, image_name))

    def create_images_for_days(self, days_info):
        for index, (weekday_fa, jalali_str, gregorian_str) in enumerate(days_info, start=1):
            self.create_image_for_day(weekday_fa, jalali_str, gregorian_str, index)
