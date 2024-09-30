from telethon import TelegramClient, events
import asyncio

# معلومات API الخاصة بحسابك من موقع my.telegram.org
api_id = 20594349
api_hash = "910f6f24cc713731e0a3d8a3ec74870e"
phone_number = "+201204266907"

# معرف الحساب الشخصي الذي يشغل البوت (يمكنك الحصول عليه عند بدء التشغيل)
owner_user_id = 6846590904

# إنشاء عميل تليجرام
client = TelegramClient("my_session", api_id, api_hash)

# قائمة لتخزين وظائف الجدولة والرسائل لكل شات
jobs = {}
muted_users = set()  # لتخزين المستخدمين المكتمين

# بقية الكود الخاص بالبوت (الذي كتبته سابقًا) سيظل كما هو هنا...

async def main():
    await client.start(phone=phone_number)
    print("Client Created")
    
    # إرسال رسالة إلى الرسائل المحفوظة عند بدء التشغيل
    await send_startup_message()

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
