import os
import threading
from flask import Flask
import telebot
from telebot import types

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_flask, daemon=True).start()

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_price = types.KeyboardButton('⛽️ د تیلو قیمتونه')
    btn_services = types.KeyboardButton('🛠 زموږ خدمات')
    btn_location = types.KeyboardButton('📍 زموږ څانګې (موقعیت)')
    btn_contact = types.KeyboardButton('📞 د اړیکې شمیرې')
    btn_team = types.KeyboardButton('👥 د ادارې او رهبرۍ ټیم')
    btn_about = types.KeyboardButton('ℹ️ زموږ په اړه')

    markup.add(btn_price, btn_services)
    markup.add(btn_location, btn_contact)
    markup.add(btn_team, btn_about)

    text = """⛽️ **نظیف الله حسین خیل پټرولیم**
**Nazifullah Hussainkhel Petroleum**

🇦🇫 السلام علیکم! ښه راغلاست نظیف الله حسین خیل پټرولیم ته.
موږ ستاسو د باوري او آرام سفر ضامن یو. مهرباني وکړئ له لاندې مینو څخه خپل د اړتیا وړ انتخاب وټاکئ.

🇬🇧 Welcome to Nazifullah Hussainkhel Petroleum.
We are dedicated to providing you with high-quality fuel and exceptional service!"""

    if os.path.exists('logo.jpg'):
        with open('logo.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text, parse_mode='Markdown', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if 'د تیلو قیمتونه' in message.text:
        msg = """📊 **د تیلو او ګاز ننني تعقیب شوي نرخونه:**

🔴 **پټرول:** 88 افغانۍ
🟡 **ډیزل:** 66 افغانۍ
🔵 **ګاز:** 55 افغانۍ

💡 *یادونه: زموږ نرخونه تل د شفافیت او عالي کوالټۍ پر بنسټ ټاکل کېږي.*"""
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif 'زموږ خدمات' in message.text:
        msg = """🛠 **د نظیف الله حسین خیل پټرولیم ځانګړي خدمات:**

✨ **۱. عالي او خالص کوالټي:** ۱۰۰٪ تضمین شوي عالي پټرول، ډیزل او ګاز.
🎯 **۲. ډیجیټل او دقیق مېټرونه:** د هر ډول غبن او کموالي څخه پاک شفاف اندازه کول.
🧼 **۳. عصري موټر شویی (Car Wash):** ستاسو د موټرو د باکیفیته پاکوالي مرکز.
🏪 **۴. فعال سوپر سټور:** د سفر د اړتیا وړ توکو ۲۴ ساعته وړاندې کول.
🕌 **۵. مجهز جومات او اعاشه:** د لمونځ او استراحت لپاره ډاډمن او پاک چاپیریال.
⏱ **۶. ۲۴/۷ پیرودونکو ته خدمات:** په پرتیزه توګه په هره شېبه کې ستاسو په خدمت کې."""
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif 'زموږ څانګې' in message.text:
        msg = """📍 **زموږ د پمپ سټېشنونو ادرسونه او څانګې:**

🏢 **لومړۍ څانګه:** لغمان، مهترلام ښار - قلعه دامان
🏢 **دویمه څانګه:** لغمان ښار - یونس چوک
🏢 **درېیمه څانګه:** د کابل - ننګرهار عمومی لاره، سرخکان

🚗 *ستاسو د سفر په اوږدو کې ستاسو د خدمت لپاره تل پرانیستی دی!*"""
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif 'د اړیکې شمیرې' in message.text:
        msg = """📞 **له موږ سره مستقیمې اړیکې:**

د پوښتنو، وړاندیزونو او همکاریو لپاره له لاندې شمیرو ګټه واخلئ:
📱 **موبایل / واټساپ:** 0784717385
📱 **ارتباطي شمیره:** 0788403610"""
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif 'د ادارې او رهبرۍ ټیم' in message.text:
        msg = """👥 **د نظیف الله حسین خیل پټرولیم اداري او کاری ټیم:**

👤 **قاري یوسف صافی** (د مالي او حسابدارۍ مسؤل)
👤 **مهراب خان صافی**
👤 **مبین خان صافی**
👤 **غلام علی صافی**
👤 **فیضان خان صافی**
👤 **مراد حسین خیل**
👤 **واصل حسین خیل**
👤 **ساحل حسین خیل**
👤 **متوکل حسین خیل**

🤝 *یو ژمن او زړه سواند ټیم ستاسو د سم او چټک خدمت لپاره!*"""
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif 'زموږ په اړه' in message.text:
        msg = """ℹ️ **زموږ په اړه (About Us):**

🌟 **نظیف الله حسین خیل پټرولیم** د درنو هیوادوالو د پام وړ او ډاډمن برانډ!

موږ ژمن یو چې خپلو مشتریانو ته د سیمې پر کچه تر ټولو لوړ کوالټي مواد (پټرول، ډیزل او ګاز) وړاندې کړو. زموږ موخه او اهداف:

🔹 د پېرودونکو رضایت او هوساینه
🔹 په دقیقو او معیاري سټنډرډونو برابر خدمات
🔹 په لغمان او شاوخوا سیمو کې ستاسو د سفر ریښتینی ملګری

*مننه چې پر موږ باور کوئ!* ❤️"""
        bot.reply_to(message, msg, parse_mode='Markdown')

    else:
        bot.reply_to(message, "مهرباني وکړئ له لاندې تڼیو څخه یو وټاکئ 👇")

bot.infinity_polling(skip_pending=True)