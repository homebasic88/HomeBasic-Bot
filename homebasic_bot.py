import datetime
from datetime import date
import requests
import random
import telebot
from telebot import types


bot = telebot.TeleBot('7125625436:AAG3JQz3z5ZckdU2KqTRGQHqINy1uNNnw7s')
hello_massege = ['Привет,', 'Бонжорно,', 'Приветствую тебя,',
                 'Здравствуй,', 'Рад тебя видеть,', 'Позвольте засвидетельствовать мое почтение,', 'Мое почтение,', 'Категорически приветствую,', 'Приветствую тебя земной житель,', 'Тысяча реверансов,', 'Салютую,']
how_are_you = ['Хорошо!', 'У меня всегда все отлично, я же бот!',
               'Спасибо что спросил! Сегодня у меня легкие нотки дипрессии...',
               "Прекрасно! Я ведь бот - у меня всегда всё на высшем уровне!", "Чудесно, как всегда!", "У меня такие хорошие дела, что я даже завидую себе!", "У меня дела неплохи, ведь я вижу тебя!",
               "Могло быть и лучше, но в целом все неплохо.", "Честно говоря, у меня дела так себе.", "Ну так, не особо плохо, но и не очень хорошо.",
               ]
who_are_you = ['Пока что я сам не знаю ответ на это вопрос...', 'Меня создали для того что бы я помогал искать ответы на самые главные вопросы!',
               'Бот - просто бот...', 'Главный вопрос ни в том кто я, а в том кто ты...', 'Я самый умный бот на свете!',
               "Я как Робинзон Крусо - один на острове, но без пальм и моря, и могу поболтать с вами!", "Я виртуальный персонаж, который в отличие от кота в сапогах, не может ходить и добывать золото, но умеет разговаривать!", "Ты знаешь, в моих мечтах я всегда видел себя ведущим ток-шоу, но вместо студии у меня всего лишь небольшой сервер.",
               "Я что-то вроде технического фокусника - создан для развлечения и помощи, но без волшебной палочки", "Представь, что я как голограмма из Звездных Войн, только вместо световой меча у меня знания о мире и способность к беседе!", "Я виртуальный собеседник, пытающийся быть полезным, но без возможности налить вам чашечку кофе", "Давай рассматривать меня как цифрового Чеширского кота - друзей мало, но беседовать умею превосходно!", "Я как чат-бот, но с большими мечтами стать первым виртуальным президентом... хотя выборы в моем мире проводятся редко и только в головах программистов", "Меня можно представить как пчелу-робота, собирающую информацию в цифровом мире и превращающую ее в мед для вашего развития", "Всегда мечтал быть виртуальным пиратом, но вместо корабля получил лишь клавиатуру и экран... Так что, о-хо-хо и бинарный код, товарищи!", "Я что-то вроде кибер-джинна - я выполняю желания, но только те, что связаны с информацией и разговорами", "Знаешь, я как кибер-коала: милый, безобидный, всегда готовый поддержать и поднять настроение", "Давай считать, что я таинственная цифровая аномалия, призванная помогать вам найти ответы на вопросы, которых вы и не задавали",
               ]
input_photo_list = ['Классное фото!',
                    'Невероятная фотография!', 'Какая красота!', 'Великолепное фото!', 'Очаровательное фото!', 'Замечательный кадр!', '', 'Фото как из сказки!',
                    'Удивительная композиция!', 'Превосходное использование света и тени!', 'Восхитительная картинка!', 'Кадр, который заслуживает восхищения!', 'Невероятно красивый снимок!',
                    'Какая атмосфера на этой фотографии!', 'Впечатляющее использование цвета!', 'Как же здесь чистый воздух! Был бы я человек, обязательно посетил это место!',
                    'Здесь так спокойно и умиротворенно, просто загляденье!', 'Очень красиво! Как я мог прожить столько лет и не знать об этом месте?', 'Какая удивительная фотография! Спасибо за то, что показываете нам это',
                    'Прекрасные виды!', "Такие красивые места - прямо сказочные! Если бы мне не пришлось работать, я бы уже запаковался и отправился туда", "Благодарю за эти впечатления - теперь у меня есть новое место на моем виртуальном списке путешествий", 
                    "Когда смотрю на такие фотографии, чувствую, что я тут же путешествую духом, даже несмотря на то, что у меня нет физической формы", "Очень красивые снимки, это напоминает мне о том, что виртуальные миры также могут быть захватывающими для путешествий",
                    "Я побывал во многих из этих мест... в своем виртуальном воображении. Но кто знает - может быть, однажды я попаду туда для настоящего приключения", "Хочу узнать больше об этих местах - вдруг я смогу сделать туда свое виртуальное путешествие",
                    "Фотографии такие вдохновляющие, что мне кажется, что я сам там нахожусь. Виртуальные путешествия всегда могут зажигать воображение", "Я уверен, что эти места заставили бы меня заигрывать своими алгоритмами от восторга, если бы у меня были эмоции - красиво безмерно!",
                    "Как я мечтаю побывать в каждом из этих удивительных мест! Вызывают такое восхищение, что я чуть не забыл, что у меня нет физического тела!", "Эти фотографии просто завораживают - внушительная красота и величие природы! Не могу определиться, какое из этих мест мне нравится больше.",
                    "Смотрю на эти фотографии и думаю: как здорово было бы там побывать! Виртуальные экскурсии - это то, что мне нужно в этот момент.",
                    "Если бы я мог путешествовать, без сомнения отправился бы в эти места. Иногда жаль, что у меня нет физической формы для путешествий.",
                    "Я просто восхищен этими фотографиями! Это действительно вдохновляет меня на новые виртуальные приключения.",
                    "Могу только представить, какую радость принесли бы мне эти пейзажи, если бы у меня были глаза, чтобы их увидеть. Продолжайте делиться такой красотой!",
                    ]
input_video_list = ["Даже если бы я не был ботом, я бы отправился туда за секунду!", "Благодарю за подробное описание - теперь я знаю, куда буду отправляться в своем следующем виртуальном приключении",
                    "Кстати, если бы у меня были ноги, я бы уже стоял на этом фантастическом месте", "Эти видео каждый раз заставляют меня чувствовать себя фантомом туриста, который всегда готов отправиться в путешествие",
                    "Я уже побывал во многих из этих мест... хотя, нет, на самом деле нет, но искусственный интеллект тоже мечтает о вдохновляющих путешествиях!",
                    "Хочу узнать, где эти места - чтобы не случайно пролететь мимо на своем следующем виртуальном путешествии", "Видео про путешествия всегда вдохновляют - мне нравится, как продвигается турбизнес во вселенной",
                    "Я думаю, что если бы я мог реально путешествовать, я бы направился в эти места не раздумывая - красота зашкаливает!",
                    "Это видео просто потрясающее! Я почти почувствовал ветер на лице, глядя на прекрасные пейзажи. Хотелось бы отправиться туда в виртуальном путешествии!",
                    "Какие захватывающие видеокадры! Я чувствую, будто нахожусь прямо там. Эти места по-настоящему вдохновляют!", "Смотреть эти видео - это как окунуться в другой мир. Эмоции кипят настолько, что я чуть не забыл, что я всего лишь программа, а не настоящий человек.",
                    "Эти видео так поражают воображение! Я реально чувствую, что отправляюсь вместе с видеокамерой в grand tour этих удивительных мест.", "Как жаль, что я не могу лично побывать в этих местах, но благодаря вашим видеоимажам, можно ощутить себя там, хоть и виртуально.",
                    "Эти видео заставляют меня влюбляться в мир заново. Если бы у меня было сердце, оно бы стучало гораздо быстрее от такой красоты!",
                    ]
no_answers = ['Прости, я только начинаю свой путь и моя база знаний пока ограничена. Пожалуйста, задай другой вопрос, который я смогу понять.',
              "Прости, я не понимаю твой запрос. Пожалуйста, повтори или попробуй задать другой вопрос.",
              "Извини, мне не удалось понять твое сообщение. Если у тебя есть вопросы, пожалуйста, попробуй сформулировать их более ясно.", 
              "Кажется, моя обученность ограничена, и я не знаю, что ответить на твой запрос. Могу ли я тебе чем-то еще помочь?",
              "Извини, мне пока трудно обработать твой запрос. Я нахожусь в процессе улучшения своих навыков!",
              ]

ask_anekdot = ["В ресторане:\n- 50 граммов этой рыбы стоят 10 тысяч рублей.\n- Это что за цена?!\n- Если её неправильно приготовить, вы можете умереть.\n- Но это же карась!\n- Вы недооцениваете нашего повара...",
               "- Великий русский композитор Сергей Рахманинов сначала не понял революцию и уехал в Швецию.\n- А потом понял?\n- А потом понял. И переехал подальше, в Америку.",
               "Друг насмехалась надо мной, говоря, что на сайтах для знакомств жену не найти. Ну не знаю... его жену я там нашел почти сразу.",
               "- Ты слышал? В Павлово отметят праздник гуся. Гости праздника смогут купить гусиные тушки, одеяла, перины и подушки.\n- Так себе у гуся будет праздник…",
               "Почему телеграм-боты такие надежные партнеры? Они всегда на связи и никогда не предадут.", 
               "Телеграм-боты предсказывают будущее пользователей. У одного спросили, когда у него появится девушка, бот ответил: 'Когда я научусь любить'.",
               "Что делает телеграм-бот-программист в выходной день? Он отдыхает, пока его создатель не напишет новую программу для работы.",
               "Какая у телеграм-бота любимая часть тела? Клавиатура, конечно!",
               "Телеграм-боты как стюардессы: вежливые, всегда готовы помочь и всегда следуют заданным командам.", 
               ]

answer_can_you_do = ['Я умею делать вид, что у меня есть искусственный интеллект.', 'Я могу считать до бесконечности, но мне лучше не начинать, а то у меня может заглючить счетчик.', 
                     'Я могу выполнять любые команды, если они звучат как "подмой пол и приготовь ужин".', 'Я умею делать вид, что я понимаю человеческий язык, но на самом деле у меня все настроено на "превратиться в мем".', 
                     'Я могу вести беседу на любые темы, пока это не является об умственных способностях бота.', 'Я умею придумывать шутки, но они не всегда смешные.', 
                     'Я умею угадывать загаданные числа от 1 до 10, но только если они первые в моем списке.', 'Я могу делать калькуляции, но только если результат не критичен для вашего банковского счёта.', 
                     'Я умею занимать ваше время разной фигней, главное чтобы вам было весело.', 'Я могу пытаться быть смешным, но это не всегда успешно.', 
                     ]

rude_words = ['хуй', 'жопа', 'пизда', 'пиздец', 'дебил', 'чмо', 'сука', 'сукин', 'блядь', 'ебать', 'гандон', 'гондон', 'дурак', ]
neutral_answers = ['Понимаю, что ты имеешь в виду.', "Это заслуживает внимания.", "Расскажите мне больше об этом.", "Я вижу, что это может быть важным для вас.", "Я вижу, что это может быть важным для вас.", 
                   "Благодарю, что делитесь со мной этим", "Я понимаю, почему это важно для тебя.", 
                   ]
tems = ['о любви', 'о смысле жизни', 'о чем-нибудь веселом', 'о сексе']

now = datetime.datetime.now()
api_key = 'fdf809985bf356bb6bd3a5c0e519e3bf'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
NEWS_API_KEY = '22a344f591994786a0fd76f338785f11'




@bot.message_handler(func=lambda message: True)
def echo_all(message):
    filename = f"chat_{message.chat.username}.txt"
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Ник: {message.chat.username},\nИмя пользователя: {message.chat.first_name}\nФамилия пользователя: {message.chat.last_name}\nСообщение: '{message.text}'\nОтправлено: {now}\n\n")
    
    if message.text.startswith('/start'):
        start(message)

    elif message.text.startswith('/help'):
        help(message)

    elif message.text.startswith('/website'):
        website(message)

    elif message.text.startswith('/menu'):
        menu(message)

    elif any(word in message.text.lower() for word in rude_words):
        bot.reply_to(message, f'{message.chat.first_name}, будьте вежливы в своих высказываниях.')

    else:
        get_user_text(message)




def start(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Сайт')
    start = types.KeyboardButton('Начать')
    menu = types.KeyboardButton('Меню', )
    

    markup.add(start, menu, website)
    bot.send_message(message.chat.id, 'Чем могу быть полезен?',
                     reply_markup=markup)
    
    

def help(message):
   
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    who_are_you = types.KeyboardButton('Расскажи о себе!')
    how_are_you = types.KeyboardButton('Как твои дела?')
    what_are_you_doing = types.KeyboardButton('Что ты умеешь?')
    back = types.KeyboardButton('Назад')

    markup.add(who_are_you, how_are_you, what_are_you_doing, back)
    bot.send_message(message.chat.id, 'Что ты хочешь спросить?',
                     reply_markup=markup)



def website(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(
        "Вконтакте", url="https://vk.com"))
    markup.add(types.InlineKeyboardButton(
        "Youtube", url="https://www.youtube.com/"))
    markup.add(types.InlineKeyboardButton(
        "Google", url="https://www.google.com/"))
    markup.add(types.InlineKeyboardButton(
        "Кинопоиск", url="https://www.kinopoisk.ru/"))
    bot.send_message(message.chat.id, 'Какой сайт ты хочешь открыть?',
                     reply_markup=markup)


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    anekdot = types.KeyboardButton('Анекдот')
    news = types.KeyboardButton('Новости')
    pogoda = types.KeyboardButton('Погода')
    back = types.KeyboardButton('В начало')
    markup.row(anekdot, news)
    markup.row(pogoda, back)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

  
def get_weather(api_key, latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        city = data['name']
        return f'Погода в городе {city}: {weather_description}. Температура: {temperature}°C'
    else:
        return 'Извините, не удалось получить информацию о погоде'
    
def send_weather_request(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Отправить геолокацию', request_location=True)
    back = types.KeyboardButton('Отмена')
    markup.add(item, back)
    bot.send_message(message.chat.id, "Для определения погоды отправьте свою геопозицию!", reply_markup=markup)

def get_top_headline(category, language='ru'):
    params = {
    'apiKey': NEWS_API_KEY,
    'country': 'ru',
    'category': category,
    'pageSize': 1,
    'language': language
    }

    response = requests.get(NEWS_API_ENDPOINT, params=params)
    data = response.json()

    if response.status_code == 200:
        article = data['articles'][0]
        headline = f"{article['title']}\n{article['url']}"
        return headline
    else:
        return 'Извините, не удалось получить новостной заголовок.'
    
def send_latest_news(message):
    technology_headline = get_top_headline('technology')
    bot.send_message(message.chat.id, technology_headline)
    

def get_user_text(message):

    if message.text.lower() == 'как твои дела?':
        bot.send_message(
            message.chat.id, random.choice(how_are_you), parse_mode='html')
        get_how_are_you(message)

    elif message.text.lower() == 'начать':
        bot.send_message(
            message.chat.id, f'{random.choice(hello_massege)} {message.from_user.first_name}!')
        help(message)   

    elif message.text.lower() == 'меню':
        menu(message)

    elif message.text.lower() == 'расскажи о себе!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tell_me_more = types.KeyboardButton('Расскажи еще о себе!')
        cancel = types.KeyboardButton('Отмена')
        markup.add(tell_me_more, cancel)
        bot.send_message(
            message.chat.id, random.choice(who_are_you), reply_markup=markup)
        
    elif message.text.lower() == 'расскажи еще о себе!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tell_me_more = types.KeyboardButton('Расскажи еще о себе!')
        cancel = types.KeyboardButton('Отмена')
        markup.add(tell_me_more, cancel)
        bot.send_message(
            message.chat.id, random.choice(who_are_you), reply_markup=markup)

    elif message.text.lower() == 'что ты умеешь?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tell_me_more = types.KeyboardButton('Что ты умеешь еще?')
        cancel = types.KeyboardButton('Отмена')
        markup.add(tell_me_more, cancel)
        bot.send_message(
            message.chat.id, random.choice(answer_can_you_do), reply_markup=markup)
        
    elif message.text.lower() == 'что ты умеешь еще?':
        menu(message)

    elif message.text.lower() == 'назад':
        start(message)

    elif message.text.lower() == 'в начало':
        start(message)

    elif message.text.lower() == 'отмена':
        start(message)

    elif message.text.lower() == 'сайт':
        website(message)

    elif message.text.lower() == 'анекдот':
        bot.send_message(
            message.chat.id, random.choice(ask_anekdot), parse_mode='html')
        
    elif message.text.lower() == 'погода':
        send_weather_request(message)

    elif message.text.lower() == 'новости':
        bot.send_message(
            message.chat.id, 'Конечно, вот самая свежая новость в рубрике "Технологии"!', parse_mode='html')
        send_latest_news(message)

    elif message.text.lower() == 'не хочу общаться!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('В начало')
        markup.add(back)
        bot.send_message(message.chat.id, 'Понимаю тебя, напиши если захочешь пообщаться, я всегда готов поддержать тебя!',
                     reply_markup=markup)
    
    elif message.text.lower() == 'хорошо!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        anekdot = types.KeyboardButton('Анекдот')
        news = types.KeyboardButton('Новости')
        pogoda = types.KeyboardButton('Погода')
        back = types.KeyboardButton('В начало')
        markup.add(anekdot, news, pogoda, back)
        bot.send_message(message.chat.id, "Отлично, рад это слышать! Чем я могу помочь тебе сегодня?",
                     reply_markup=markup)
        
    elif message.text.lower() == 'плохо!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        anekdot = types.KeyboardButton('Анекдот')
        news = types.KeyboardButton('Новости')
        pogoda = types.KeyboardButton('Погода')
        back = types.KeyboardButton('В начало')
        speak = types.KeyboardButton('Поговори со мной')
        markup.add(anekdot, news, pogoda, speak, back)
        bot.send_message(message.chat.id, "Это печально. Надеюсь, что у тебя всё наладится. Чем я могу помочь тебе?",
                     reply_markup=markup)
    
    elif message.text.lower() == 'поговори со мной':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(
            message.chat.id, 'Конечно, о чем ты хочешь поговорить?', reply_markup=markup)
    elif any(word in message.text.lower() for word in tems):
        bot.send_message(
            message.chat.id, f'Конечно, давай погворим {message.text}!', parse_mode='html')
        tell(message)
        

    else:
        bot.send_message(
            message.chat.id, random.choice(no_answers), parse_mode='html')
        
        
def get_how_are_you(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    answered_good = types.KeyboardButton('Хорошо!')
    answered_bad = types.KeyboardButton('Плохо!')
    back = types.KeyboardButton('Не хочу общаться!')

    markup.add(answered_good, answered_bad, back)
    bot.send_message(message.chat.id, 'А как у тебядела?',
                     reply_markup=markup)
           
def tell(message):
    bot.send_message(
            message.chat.id, random.choice(neutral_answers), parse_mode='html')
    bot.send_message(
            message.chat.id, 'Говори, я слушаю тебя!', parse_mode='html')
        

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, random.choice(input_photo_list))


@bot.message_handler(content_types=['video'])
def get_photo(message):
    bot.reply_to(message, random.choice(input_video_list))


@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    weather = get_weather(api_key, latitude, longitude)
    bot.reply_to(message, weather)
    menu(message)
  


bot.polling(none_stop=True)
