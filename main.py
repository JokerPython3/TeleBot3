#راح نشرح شون تضيف اشتراك اجباري في بوتت وشون تضيف اوامر بوتك بي شي اسمه menum اي قاىمة
import telebot
tok="Token"
bot=telebot.TeleBot(tok)
@bot.message_handler(commands=["start"])
def start(message):
    id=message.from_user.id
    #هاي شارحها بي شروحات قديمه تلكاها بل قناة
    channel="@SourceTelethon"
    #تحط يوزر قناتك مع @ وترفع بوت ادمن بل قناة حتى يعرف مستخدم مشترك بل ققناة لو لا
    m=bot.get_chat_member(channel,id)
    #هينا امرنا بوت يروح لي هاي قناة ويبحث عن شخص هسا اذا اطبعها راح تطلعلي جميع معلوماته مثل مشترك لو لا
    #تحتاج الامر الى يوزر قناتك و ايدي مستخدم المراد تحقق من اشتراكه بل قناة
    print(m)
    #طبع معلوماتي ومعلوماتي بل قناة 
    #status => حالتي بل قناة مشترك لو مغادر 
    status=m.status
    #هسا واحد يكول ليش ماناخذ معلومات بي استخدام اقواس معكوفه [] 
    #  يطلع error هاي ليست json بل قيمة رجع  chatmember 
    #شروط تحقق من اشتراك




    if status=='left':#اذا  status يساوي left يعني مغادر طالع من قناة
        #دزله هاي رساله
        bot.send_message(message.chat.id,f"join my channel : {channel}  and send /start command")
    else:
        #اذا لم يتحقق شرط يعني هو منضم بل قناة 
        #دزله هاي رسالة 

        bot.send_message(message.chat.id,"you Join my channel welcome")
#كود ووضع الاوامر في قاىمة بوت ال menum
bot.set_my_commands([
    telebot.types.BotCommand("start","لبداء البوت"),#start => امر رقم واحد / لبدء البوت هو وصف بوت
    #تكدر تضيف بعد اوامر بكيفك 
    #تحط بي اول واحد امر
    #ثاني واحط وصف امر
    telebot.types.BotCommand("help","شرح البون")
]) 
#set_my_commands => هذا امر يضع اوامرك بل قاىمة بوت  
bot.infinity_polling()
#حتى يشتغل بوت مايقف حتى لو صار error 
#خلي نشغل
# انتضرونا بي شروحات قادمه
# by => @JokerPython3
