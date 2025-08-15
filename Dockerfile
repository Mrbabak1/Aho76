# انتخاب تصویر پایه
FROM python:3.9

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt .

# نصب کتابخانه‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کد ربات
COPY . .

# اجرای ربات
CMD ["python", "bot.py"]
