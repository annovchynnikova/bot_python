import telebot
import config

from telebot import types

bot=telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp','rb')
    bot.send_message(message.chat.id, "Привіт і привет and hi старушка Даша! Тобі сьогодні доведеться пройти незабутню подорож, попрацювати ручками і трошечки подумати)) Ми (Аня і Поля, якщо ти ще не зрозуміла) ще раз тебе вітаємо і бажаємо удачі! Цілуємо :*")
    bot.send_sticker(message.chat.id,sti)
    bot.send_message(message.chat.id, "Надішли мені /go , як тільки будеш готова!")
@bot.message_handler(commands=['go'])
def first(message):
    sti = open('sticker.webp','rb')
    music1 = open('music1.ogg','rb')
    bot.send_message(message.chat.id, "Ну що жжжжж, почнемо твою питку!")
    bot.send_message(message.chat.id, "І перший раунд: Музикальний, адже ти так любиш музику!")
    bot.send_message(message.chat.id, "Твоє завдання: дати відповіді на питання або продовжити текст (відповідь надсилай мені, я чекаю тільки правильну!)")
    bot.send_sticker(message.chat.id, sti)
    bot.send_voice(message.chat.id, music1)

# перший раунд 
# перше завдання
@bot.message_handler(regexp="13")
def r1z1try1(message):
    music2 = open('music2.ogg','rb')
    bot.send_message(message.chat.id, "Ну що ж першe завдання першого раунду ти осилила!!! А як щодо такого? Завдання 2")
    bot.send_voice(message.chat.id, music2)
@bot.message_handler(regexp="тринадцать")
def r1z1try2(message):
    music2 = open('music2.ogg','rb')
    bot.send_message(message.chat.id, "Ну що ж першe завдання першого раунду ти осилила!!! А як щодо такого? Завдання 2")
    bot.send_voice(message.chat.id, music2)
@bot.message_handler(regexp="тринадцять")
def r1z1try3(message):
    music2 = open('music2.ogg','rb')
    bot.send_message(message.chat.id, "Ну що ж першe завдання першого раунду ти осилила!!! А як щодо такого? Завдання 2")
    bot.send_voice(message.chat.id, music2)

# друге завдання
@bot.message_handler(regexp="школьное")
def r1z2try1(message):
    music3 = open('music3.ogg','rb')
    bot.send_message(message.chat.id, "Опа опа красотка! Продовжуєм! А як щодо третього?")
    bot.send_voice(message.chat.id, music3)

# третє завдання
# @bot.message_handler(regexp="Это новый кадилак")
# def r1z3try1(message):
#     bot.send_message(message.chat.id, "Такс такс ъдем катосить на кадылаку? нене, вирішуй 4 завдання!")
#     bot.send_voice(message.chat.id, music4)

# 4 завдання
@bot.message_handler(regexp="У інших")
def r1z4try1(message):
    music51 = open('music51.ogg','rb')
    music52 = open('music52.ogg','rb')
    music53 = open('music53.ogg','rb')
    bot.send_message(message.chat.id, "Хммм.. Невже все так легко? Наступне?)")
    bot.send_voice(message.chat.id, music51)
    bot.send_voice(message.chat.id, music52)
    bot.send_voice(message.chat.id, music53)
@bot.message_handler(regexp="У других")
def r1z4try2(message):
    music51 = open('music51.ogg','rb')
    music52 = open('music52.ogg','rb')
    music53 = open('music53.ogg','rb')
    
    bot.send_message(message.chat.id, "Хммм.. Невже все так легко? Наступне?)")
    bot.send_voice(message.chat.id, music51)
    bot.send_voice(message.chat.id, music52)
    bot.send_voice(message.chat.id, music53)

# 5 перехід на другий раунд завдання
#локація до раунду два ребуси
@bot.message_handler(regexp="Самотній музика")
def r1z5try1(message):
    bot.send_message(message.chat.id, "Неперевершена пісня, яка заполонила серця багатьох! Як і ти наші! З першим раундом ти справилась! Час рухатись далі! Зараз ти маєш дійти оооось сюди, там тебе чекають ...")
    bot.send_location(message.chat.id, latitude='50.388095', longitude='30.477155')
    #'https://maps.google.com/maps?q=50.388095,30.477155&ll=50.388095,30.477155&z=16'
    bot.send_message(message.chat.id, "Коли дійдеш до цієї точки знайдеш, що робити далі)")

# другий раунд 
@bot.message_handler(commands=['hereroundtwo'])
def second(message):
    bot.send_message(message.chat.id, "Хей хоп на зв'язку квест-рум ~Взаперти~ раунд ЕРУДИТ, подивимось як ти справишся з ребусами) ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("Так!")
    item2= types.KeyboardButton("Омагад я боюсь")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Погнали?", reply_markup=markup)
# 2 раунд 2 завдання
@bot.message_handler(regexp="Угорь")
def r2z2try1(message):
    rebys2 = open('ребус2.JPG','rb')
    bot.send_message(message.chat.id, "Не питай як і не питай навіщо! Йдемо далі)")
    bot.send_message(message.chat.id, "№2")
    bot.send_photo(message.chat.id,  rebys2)
# 2раунд 3 завдання
@bot.message_handler(regexp="Запоріжжя")
def r2z3try1(message):
    rebys3 = open('ребус3.JPG','rb')
    bot.send_message(message.chat.id, "Дом милий дім.. Ти все ближче і ближче")
    bot.send_message(message.chat.id, "№3")
    bot.send_photo(message.chat.id, rebys3)
@bot.message_handler(regexp="Запорожье")
def r2z3try2(message):
    rebys3 = open('ребус3.JPG','rb')
    bot.send_message(message.chat.id, "Дом милий дім.. Ти все ближче і ближче")
    bot.send_message(message.chat.id, "№3")
    bot.send_photo(message.chat.id, rebys3)
    # 2раунд 4 завдання
@bot.message_handler(regexp="Лаванда")
def r2z4try1(message):
    bot.send_message(message.chat.id, "Пахне як ти, не ваня вобщем")
    bot.send_message(message.chat.id, "№4")
    bot.send_photo(message.chat.id, 'Ким ти станеш після весілля?')
    # 2раунд 5 завдання
@bot.message_handler(regexp="Маймусовой")
def r2z5try1(message):
    bot.send_message(message.chat.id, "МИ ЧЕКАЄМО ВЕСІЛЛЯ!")
    bot.send_message(message.chat.id, "Вау, да ти профі! Вітаємо,ти справилась з цим надскладним завданням, але далі не легше! Тримайся)")
    bot.send_location(message.chat.id, latitude='50.387780', longitude='30.475676')
    #'https://maps.google.com/maps?q=50.387780,30.475676&ll=50.387780,30.475676&z=16'
    bot.send_message(message.chat.id, "Коли дійдеш до цієї точки знайдеш, що робити далі)")
   
# третій раунд 
@bot.message_handler(commands=['threeidiots'])
def three(message):
    bot.send_message(message.chat.id, "Да, да просто threeidiots , все було так просто, але ти не переймайся далі буде!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("ГО")
    item2= types.KeyboardButton("Ви задовбали, я вас приб'ю")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Летс го?", reply_markup=markup)

# перше завдання знизу у тексті
# друге завдання третій раунд
@bot.message_handler(regexp="трипофобия")
def r3z2try1(message):
    bot.send_message(message.chat.id, "Мерзость! Добре, що без картинок)) Такс, некст квестіон")
    bot.send_message(message.chat.id, "Аня - зелений, Поля - малиновий, Даша - будь-який ...")
# 3 завдання третій раунд 
@bot.message_handler(regexp="чай")
def r3z3try1(message):
    bot.send_message(message.chat.id, "По чашечці? Потім) А ти йдеш далі!")
    bot.send_message(message.chat.id, "Большой, толстый, твердый, если укусить или сжать - больно и невкусно")
@bot.message_handler(regexp="хуй")
def r3z3try2(message):
    bot.send_message(message.chat.id, "Ха шалун! Бат ноу це не хуй) Думай далі")
    bot.send_message(message.chat.id, "Большой, толстый, твердый, если укусить или сжать - больно и невкусно")
  
 # 4 завдання третій раунд
@bot.message_handler(regexp="кактус")
def r3z4try1(message):
    bot.send_message(message.chat.id, ")))))))))))))))))))))))))))")
    bot.send_message(message.chat.id, "Лутшая мужская вещь женского гардероба")
# 5 завдання третій раунд
@bot.message_handler(regexp="рубашка")
def r3z5try1(message):
    bot.send_message(message.chat.id, "Отакі ми женщіни..")
    bot.send_message(message.chat.id, "Супер! Умнічка!")
@bot.message_handler(regexp="рубаха")
def r3z5try2(message):
    bot.send_message(message.chat.id, "Отакі ми женщіни..")
    bot.send_message(message.chat.id, "Супер! Умнічка!")

#локація четвертого раунду
    bot.send_location(message.chat.id, latitude='50.387598', longitude='30.476608')
    #'https://maps.google.com/maps?q=50.387598,30.476608&ll=50.387598,30.476608&z=16'
    bot.send_message(message.chat.id, "Коли дійдеш до цієї точки знайдеш, що робити далі)")

# четвертий раунд
@bot.message_handler(commands=['4'])
def four(message):
    bot.send_message(message.chat.id, "Парапапам")
    bot.send_message(message.chat.id, "DO OR DIE")
    bot.send_message(message.chat.id, "FIRST")
    bot.send_message(message.chat.id, "ІЗ того що бачиш навколо себе склади слово хуй, сфотографуй і надішли мені!!!")
#надсилання фото    
@bot.message_handler(content_types=['photo'])
def photo1(message):    
    bot.send_message(message.chat.id, "ЧУДОВО! Ти проживеш ще одне завдання")
    bot.send_message(message.chat.id, "Зніми мені відеоповідомлення де ти і як ти бачиш трьох ідіотів через 5 років")
#надсилання відеоповідомлення
#переклад ласт зав 4 раунда
@bot.message_handler(content_types=['video_note'])
def video1(message):    
    bot.send_message(message.chat.id, "Що це? Це взагалі малюнок? Ладно, прощаєм! Ідем далі!")
    bot.send_message(message.chat.id, "Переклади на людську мову:")
    bot.send_message(message.chat.id, "лупси")
@bot.message_handler(regexp="хлопя")
def r4z1try1(message):
    bot.send_message(message.chat.id, "кєс")
@bot.message_handler(regexp="кіоск")
def r4z2try1(message):
    bot.send_message(message.chat.id, "туркмяні")
@bot.message_handler(regexp="турки")
def r4z3try1(message):
    bot.send_message(message.chat.id, "нагєнси")
@bot.message_handler(regexp="наггетсы")
def r4z4try1(message):
    bot.send_message(message.chat.id, "ровер")
@bot.message_handler(regexp="велосипед")
def r4z5try1(message):
    bot.send_message(message.chat.id, "воровайка")
@bot.message_handler(regexp="вор")
def r4z6try1(message):
    bot.send_message(message.chat.id, "Олег")
@bot.message_handler(regexp="підарас")
def r4z7try1(message):
    bot.send_message(message.chat.id, "Вітаємо! Ви пройшли тест на адекватність! Треба й походить до наступного дерева, вирушаймо")
    #локація п'ятого раунду
    bot.send_location(message.chat.id, latitude='50.385417', longitude='30.473671')
    #'https://maps.google.com/maps?q=50.385417,30.473671&ll=50.385417,30.473671&z=16'
    bot.send_message(message.chat.id, "Коли дійдеш до цієї точки знайдеш, що робити далі)")
# пятий раунд 
@bot.message_handler(commands=['ochko'])
def five(message):
    bot.send_message(message.chat.id, "21 не срок!")
    bot.send_message(message.chat.id, "Раунд nostalgy")
    # перше завдання
    bot.send_message(message.chat.id, "Назови три цифры места в которое ты вернешся за этот длинный путь")
# 2 завдання 5 раунд
@bot.message_handler(regexp="307")
def r5z2try1(message):
    bot.send_message(message.chat.id, "Не плакай")
    bot.send_message(message.chat.id, "Лучшые средства передвижения по Киеву?")
# 3 завдання 5 раунд
@bot.message_handler(regexp="костыли")
def r5z3try1(message):
    bot.send_message(message.chat.id, "Что общего у губки и в улитки?")
@bot.message_handler(regexp="Боб")
def r5z4try1(message):
    bot.send_message(message.chat.id, "Дыти ви готовы?")    
    #локація шостого раунду
    bot.send_location(message.chat.id, latitude='50.383409', longitude='30.474986')
    #'https://maps.google.com/maps?q=50.383409,30.474986&ll=50.383409,30.474986&z=16'
    bot.send_message(message.chat.id, "Коли дійдеш до цієї точки знайдеш, що робити далі)")
# шостий раунд
@bot.message_handler(commands=['weloveyou'])
def six(message):
    bot.send_message(message.chat.id, "І хочемо побажати більше ніколи не проходити такі тупі квести як цей)")
# 1 завдання 6 раунд
    bot.send_message(message.chat.id, "Особливе, незмінне, смачне, центральне, з грибним супом і лате")
# 2 завдання 6 раунд
@bot.message_handler(regexp="Aroma Special")
def r6z2try1(message):
    bot.send_message(message.chat.id, "Їсти не захотілось? Ще трошкииии") 
    bot.send_message(message.chat.id, "Instagram, COVID-19 чи синяки під очима?")
# 3 завдання 6 раунд
@bot.message_handler(regexp="маска")
def r6z3try1(message):
    bot.send_message(message.chat.id, "Фінішна пряма!") 
    bot.send_message(message.chat.id, "Аня + Поля + Даша =") 
# the end
@bot.message_handler(regexp="три идиота")
def r6z4try1(message):
    bot.send_message(message.chat.id, "О да, і через 5 років і через 10 і навіть більше так і буде! Ми тебе любимо і вітаємо з днем народження!") 
    bot.send_message(message.chat.id, "Пссс.. Тобі сюди)")
    # локація на якій стоїмо ми
    bot.send_location(message.chat.id, latitude='50.381118', longitude='30.476304')
    #https://maps.google.com/maps?q=50.381118,30.476304&ll=50.381118,30.476304&z=16
#error
@bot.message_handler(content_types=['text'])
def err(message):
 # перше завдання другого раунду 
    if message.text=="Так!": 
        rebys1 = open('ребус1.JPG','rb')
        bot.send_message(message.chat.id, "№1")
        bot.send_photo(message.chat.id, rebys1)
    elif message.text=="Омагад я боюсь":
        bot.send_message(message.chat.id, "Донт воррі бі хеппі")
    elif message.text=="Ви задовбали, я вас приб'ю":
        bot.send_message(message.chat.id, "Спочатку знайди нас)))))))))))")
    elif message.text=="ГО": 
        bot.send_message(message.chat.id, "Фобия раз, фобия два, фобия ?")
    else:
        bot.send_message(message.chat.id, "Ой! Щось пішло не так! Мабуть що відповідь твоя не така уж і правильна(")
# # перше завдання третього раунду 
#     if message.text=="ГО": 
#         bot.send_message(message.chat.id, "Фобия раз, фобия два, фобия ?")
#     elif message.text=="Ви задовбали, я вас приб'ю":
#         bot.send_message(message.chat.id, "Спочатку знайди нас)))))))))))")
#     else:
#         bot.send_message(message.chat.id, "Ой! Щось пішло не так! Мабуть що відповідь твоя не така уж і правильна(")

bot.polling(none_stop=True)    