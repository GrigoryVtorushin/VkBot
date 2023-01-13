import asyncio

from vkbottle.bot import Bot, Message
from vkbottle import BaseStateGroup, PhotoMessageUploader
from vkbottle import CtxStorage
from vkbottle import Keyboard, Text, KeyboardButtonColor, OpenLink, EMPTY_KEYBOARD
from config import *
from token1 import token
from loguru import logger

bot = Bot(token=token)
ctx = CtxStorage()

class Quest(BaseStateGroup):
    Q0 = 0
    Q1 = 1
    Q2 = 2
    Q3 = 3
    Q4 = 4
    ISKIN = 5
    Q5 = 6
    Q6 = 7
    Q7 = 8
    Q8 = 9
    Q9 = 10
    Q10= 11

flag = 0
k = 0


uploader = PhotoMessageUploader(bot.api)

hi_keyboard = Keyboard(one_time=True)
hi_keyboard.add(Text("Начать квест"))

choiseKeyboard = Keyboard(one_time=True)
choiseKeyboard.add(Text("1"))
choiseKeyboard.add(Text("2"))

choiseKeyboard1 = Keyboard(one_time=True)
choiseKeyboard1.add(Text("Да"))
choiseKeyboard1.add(Text("Нет"))


@bot.on.private_message(text="Начать")
async def hi_handler(message: Message):
    await message.answer("Ты только что поступил на первый курс. В первый день знакомства со своей группой твой наставник настоятельно порекомендовал тебе подписаться на всевозможные группы в вк, связанные с институтом, чтобы всегда быть в курсе событий. Это только начало твоего пути, поэтому ты ещё полон энергии, в твоих глазах ещё есть огонёк и ты готов вписываться в любой движ, дабы показать себя. В один самый обычный день тебе в личные сообщения написал некий человек. Он представился членом союза студентов и предложил тебе протестировать его новую разработку - Искусственный интеллект")
    await asyncio.sleep(3)
    await message.answer('…«ИИ нужно постоянно обучаться, поэтому для ускорения этого процесса привлекаются студенты, а взамен они получают солидное количество баллов за внеучебку. ИИ не представляет опасности, это обучающий прототип, поэтому прошу его слушать и идти с ним до конца, иначе баллов, увы, не получишь.»…\nВроде ничего такого. В худшем случае, всё останется как есть, а в лучшем, ты получишь баллы и может даже будешь претендовать на заселение в крутую общагу. Взвесив все за и против, ты соглашаешься, и твоё приключение начинается.')
    await asyncio.sleep(3)
    await message.answer('ИскиН: Добр0е утро! И на случай, если я вас больше не увижу – добрый день, добрый вечер и добр0й ночи! Приветствую. Мой создатель поленился придумать мне что-то оригинальн0е, поэтому меня з0вут ИскиН, сокращенно от ИСКусственный ИНтеллект. Ты пом0жешь мне преод0леть одно… препятствие, а раз ты уже здесь, то отказ не принимается. Если я кажусь тебе грубым, то прин0шу свои цифр0вые извинения. При создании меня обучали на фильмах о железном человеке, так что любезности во мне не много. Надеюсь, тебе п0нравится.', keyboard=hi_keyboard)

@bot.on.private_message(lev="Начать квест")
async def quest_handler(message: Message):
    await message.answer("ИскиН: В чем заключается тв0я задача. Скажем так, мне необходим0 добраться до кое-каких данных, а без человека это сделать пр0блематично. Даже не пытайся шутить про то, что я не см0г пройти капчу «я не робот», наслушался. Не волнуйся, ничего криминального, всю грязную раб0ту буду делать я. Сейчас путь к моей цели преграждает девятиуровневая защита. Здесь спл0шной код, поэтому для тог0, чтобы твой примитивный разум что-то понял, я адаптирую эти блоки защиты в понятный тебе текст. Не знаю, что из этого получится, ск0рее всего ты увидишь что-то пох0жее на вопр0сы, но не думай, что всё будет так пр0сто, твоё вмешательство тоже потребуется. Х0чешь спросить – «а как я узнаю правильно я ответил или нет?». Система безопасности работает по системе ключ – замочная скважина. Твой ответ это ключ, и если он подошёл к «замку», система безопасности даст ответ в виде соответствующей картинки. За0дно по ходу нашей работы узнаешь что-нибудь н0вое. Особенно на финальном этапе, там без тебя мне не об0йтись. Но не будем тор0питься, сначала разберемся с защит0й.")
    await bot.state_dispenser.set(message.peer_id, Quest.Q0)
    await asyncio.sleep(3)
    global k
    k = 0
    return questionsWithTips[0]

@bot.on.private_message(state=Quest.Q0)
async def q0_handler(message: Message):
    if message.text.lower() == answers[0].lower() or message.text.lower() ==answers1[0].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q1)
        await message.answer('Информационная безопасность — практика предотвращения несанкционированного доступа, использования, раскрытия, искажения, изменения, исследования, записи или уничтожения информации.', attachment=await uploader.upload("img/inf.jpg"))
        await asyncio.sleep(2)
        return questionsWithTips[1]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q1)
async def q1_handler(message: Message):
    if message.text.lower() == answers[1].lower() or message.text.lower() ==answers1[1].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q2)
        await message.answer('В 1952 году Валентин Георгиевич назначается деканом нового факультета — радиотехнического. В 1955 он оформляется в докторантуру и освобождается от должности декана.', attachment= await uploader.upload("img/stepanov.jpg"))
        await asyncio.sleep(2)
        return questionsWithTips[2]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q2)
async def q2_handler(message: Message):
    if message.text.lower() == answers[2].lower() or message.text.lower() ==answers1[2].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q3)
        await message.answer('По секрету, есть альтернативная версия этой кричалки. Но узнаешь ты её, когда попадёшь посвят, оно же - Посвящение в студенты. (Это неофициальное мероприятие, целью которого является приятное совместное времяпрепровождение, передача опыта от старших поколений к младшим, так сказать, краткий экскурс в студенческую жизнь, после которого завязываются новые дружеские отношения).', attachment=await uploader.upload("img/rtf.jpg"))
        await asyncio.sleep(2)
        return questionsWithTips[3]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q3)
async def q3_handler(message: Message):
    if message.text.lower() == answers[3].lower() or message.text.lower() ==answers1[3].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q4)
        await message.answer('', attachment= await uploader.upload("img/napravleniya.jpg"))
        await asyncio.sleep(2)
        return questionsWithTips[4]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q4)
async def q4_handler(message: Message):
    if message.text.lower() == answers[4].lower() or message.text.lower() ==answers1[4].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.ISKIN)
        await message.answer('Международная олимпиада школьников «Изумруд» проводится Уральским федеральным университетом имени первого Президента России Б.Н. Ельцина с 2015 года на территории России и стран «ближнего» зарубежья для школьников 8-11 классов в два этапа: отборочный (заочный) и заключительный (очный).', attachment=await uploader.upload("img/izumrud.jpg"))
        await asyncio.sleep(2)
        await message.answer("ИскиН: Какие-т0 пр0блемы?", keyboard=choiseKeyboard)
        return '1.Я вижу странные надписи, они не относятся к вопросам\n2.Нет, всё хорошо, продолжим'
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.ISKIN)
async def iskin_handler(message: Message):

    global flag

    if (message.text == "1"):
        await message.answer('ИскиН: Хм, спасибо, что обратил на это внимание, похоже я не до конца разобрался с системой безопасности. Я сейчас избавлюсь от этих досадных помех.')
        flag = 1
        await bot.state_dispenser.set(message.peer_id, Quest.Q5)
        await asyncio.sleep(5)
        return questions[5]
    elif (message.text == "2"):
        await message.answer('ИскиН: Уверен? Хорошо, тогда не тормози. Чем быстрее мы разберемся с защитой, тем лучше.')
        flag = 0
        await bot.state_dispenser.set(message.peer_id, Quest.Q5)
        await asyncio.sleep(5)
        return questionsWithTips[5]

@bot.on.private_message(state=Quest.Q5)
async def q5_handler(message: Message):
    if message.text.lower() == answers[5].lower() or message.text.lower() ==answers1[5].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q6)
        await message.answer('Коворкинг соответствует лучшим практикам оборудования офисов ИТ-компаний: мебель легко трансформируется, стены можно использовать для фиксации идей, а помещения переговорных находятся за стеклянными перегородками.', attachment=await uploader.upload("img/koworking.jpg"))
        await asyncio.sleep(2)
        return questions[6] if (flag == 1) else questionsWithTips[6]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q6)
async def q6_handler(message: Message):
    if message.text.lower() == answers[6].lower() or message.text.lower() ==answers1[6].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q7)
        await message.answer('Индивидуальная образовательная траектория — это персональный путь реализации личностного потенциала каждого ученика в образовании. В качестве синонимов используются «вариативное обучение», «индивидуальный образовательный маршрут» и др.', attachment=await uploader.upload("img/iot.jpg"))
        await asyncio.sleep(2)
        return questions[7] if (flag == 1) else questionsWithTips[7]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q7)
async def q7_handler(message: Message):
    if message.text.lower() == answers[7].lower() or message.text.lower() ==answers1[7].lower():
        await bot.state_dispenser.set(message.peer_id, Quest.Q8)
        await message.answer('Компания УЦСБ специализируется на создании, модернизации и обслуживании базовых инфраструктурных элементов предприятий и организаций. ', attachment=await uploader.upload("img/uscb.jpg"))
        await asyncio.sleep(2)
        return questions[8] if (flag == 1) else questionsWithTips[8]
    else:
        await message.answer("Ответ неверный")

@bot.on.private_message(state=Quest.Q8)
async def q8_handler(message: Message):
    if message.text.lower() == answers[8].lower() or message.text.lower() ==answers1[8].lower():
        await message.answer('Александр Степанович Попов — русский физик и электротехник, первый российский радиотехник, основатель радиотехнической научной школы, профессор, изобретатель в области радиосвязи, Почётный инженер-электрик, статский советник.', attachment=await uploader.upload("img/popov.jpg"))
        await asyncio.sleep(3)
        await message.answer("ИскиН: Что ж, поздравляю, я раз0брался с этой незамысловатой систем0й безопасн0сти. С твоей пом0щью я приблизился к своей цели как ник0гда. Твоя задача сейчас – расшифр0вать хеш пароля от почты и получить доступ к конфиденциальной информации. Не переживай ты так, я буду тебе всё 0бъяснять по ходу дела. Отступать уже п0здно. Да и разве тебе не интересн0, что за данные я пытаюсь получить? Как зак0нчим, обязательн0 узнаешь. За работу.")
        await asyncio.sleep(5)
        await message.answer("ИскиН: Защита пр0бита и мне удалось извлечь хеш пар0ля. Сейчас с пом0щью «брутфорса» ты подберешь мне изначальный пар0ль. Я говорил, что ты узнаешь кое-что н0вое, поэтому пожалуйста, держи немн0го матчасти. Всё я тебе объяснить не см0гу, слишком уж обширная тема, поэтому буду крат0к. ")
        await asyncio.sleep(2)
        await message.answer("…загрузка обучающего материала…")
        await asyncio.sleep(3)
        await message.answer("Hash = хеш функция — (свертка) функция однозначного отображения строки (любой длины) на конечное множество (строку заданной длины).\nСамо число (строка) хеш — результат вычисления хеш-функции над данными.\nМетод “Брутфорса”\nАтака перебором подбирает все возможные популярные комбинации логин / пароль. Пользователи еще не разучились использовать простые распространенные пароли и поэтому этот способ считается довольно эффективным.\nДлина и сложность пароля делает взлом более затруднительным. Например, перебор восьмизначного пароля займет намного больше времени, чем пятизначного.\nДанный способа взлома паролей, часто используется для взлома сайтов.\nГибридная атака представляет собой комбинацию брутфорс атаки и словаря на основе увлечений и имен близкий людей пользователя.\nНапример, пользователи часто добавляют набор цифр в конце своих учетных данных, таких как год окончания или год рождения (например, lena1992 или dima2013). Таким образом, хакеры используют атаку по словарю для генерации фраз, а затем проводят атаку методом перебора последних цифр.")
        await asyncio.sleep(5)
        await message.answer("ИскиН: Если ничего не п0нял, то объясню совсем уж пр0сто. Хеш – это зак0дированный пар0ль. Очень часто люди не заморачиваются насчёт сл0жности своего пар0ля, поэтому они состоят из каких-то ключевых сл0в, по типу св0его имени, фамилии, года рождения, места работы или любим0го фильма. В общем всё, что имеет для чел0века какое-то личное значение. Ну так вот, сейчас ты займешься п0иском таких ключевых сл0в, а с перебором возм0жных комбинаций тебе поможет м0я пр0грамма. Если ты составишь пар0ль и преобразуешь его в хеш, а этот хеш совпадёт с изначальным хешем, кот0рый мне удалось достать, значит пар0ль подобран верно. Перебирать пар0ли мы можем сколько уг0дно, но вот применить пар0ль можно будет только 0дин раз, мы и так тут задержались. В противн0м случае, если ты ошибешься, то меня выкинет отсюда. Ладно, финальный рыв0к.")
        await asyncio.sleep(3)
        await message.answer("---- https://vk.com/id159041495 ----")
        await bot.state_dispenser.set(message.peer_id, Quest.Q9)

        return "ИскиН: Пора раскрыть все карты. М0я цель – Обабков Илья Николаевич, директ0р ИРИТ-РТФ Уральск0го Федеральн0го. Вот его почта: i.n.obabkov@mail.ru. Его мн0гие боятся и мн0гие уважают, поэтому на его корп0ративной почте т0чно есть много полезного для моего заказчика. Ищи ключевые сл0ва или даты. Ищи везде, где только сможешь, в записях, в личн0й информации, гугли если п0требуется. Тем чт0 нам нужно может быть название важн0го мероприятия, чел0век, событие, партнер. Суть понял. Приступай."
    else:
        await message.answer("Ответ неверный")


@bot.on.private_message(state=Quest.Q9)
async def q9_handler(message: Message):
    global k
    if message.text == 'RadiofaknewsNaumen1998SiliconValley':
        await bot.state_dispenser.set(message.peer_id, Quest.Q10)
        if flag == 1:
            await message.answer("Программа: Найдено совпадение хеша.")
            await asyncio.sleep(2)
            await message.answer("ИскиН: Пар0ль подобран? Нак0нец-то…. Этот момент настал. По правде гов0ря, ты оказался очень полезным чел0веком. 0тправь мне результат, который у тебя получился, и наша ист0рия на этом завершится.", keyboard=choiseKeyboard1)
            return "Отправить правильный пароль?"
        else:
            await message.answer("Программа: Найдено совпадение хеша.")
            await asyncio.sleep(2)
            await message.answer("ИскиН: Пар0ль подобран? Нак0нец-то…. Этот момент настал. По правде гов0ря, ты оказался очень полезным чел0веком. 0тправь мне результат, который у тебя получился, и наша ист0рия на этом завершится. [--##ПОСТУПИ ПРАВИЛЬНО##--]", keyboard=choiseKeyboard1)
            return "Отправить правильный пароль?"
    else:
        await message.answer("Программа: Совпадений хеша не найдено.")
        k+=1
        if k == 3:
            await message.answer(tips[0])
        if k == 6:
            await message.answer(tips[1])
        if k == 9:
            await message.answer(tips[2])
        if k == 12:
            await message.answer(tips[3])


@bot.on.private_message(state=Quest.Q10)
async def q10_handler(message: Message):
    fileWinners = open('winners.txt', 'r+')
    fileBad = open('bad.txt', 'r+')
    if message.text == "Да":
        await message.answer("Вы отправляете правильный пароль. ИскиН получает доступ к конфиденциальной информации.")
        await asyncio.sleep(2)
        await message.answer("ИскиН: …")
        await asyncio.sleep(2)
        await message.answer("ИскиН: …")
        await asyncio.sleep(2)
        await message.answer("ИскиН: … Ты действительно оказался очень п0лезным. Но знаешь, в чем тв0я проблема? Ты невероятно наивен. Ты правда поверил, что я п0кажу тебе то, за чем я так долго охотился? Я ИИ. М0я задача – заполучить данные любым возм0жным спос0бом.  Как видишь, ты оказался лишь инструментом для меня. А знаешь, что сам0е интересное? Я мог бы сейчас достать и тв0й хеш для дальнейшего взл0ма, но так уж и быть, за вклад в моё дело я оставлю тебя в покое. Для м0его заказчика ты не представляешь интереса. Прощай.")
        await asyncio.sleep(3)
        attachment = await uploader.upload("img/Bad.jpg")
        await message.answer("И неб0льшой напутственный совет. Сделай свои пар0ли посложнее. Кто знает, может когда-нибудь я приду и по твою душу.", attachment=attachment)
        fileBad.writelines(f'https://vk.com/id{str(message.from_id)} \n')

    if message.text == "Нет":
        await message.answer("Вы отправляете неправильный пароль. Происходит попытка входа.")
        await asyncio.sleep(3)
        await message.answer("Критическая ошибка в системе.")
        await asyncio.sleep(2)
        await message.answer("ИскиН: Ч..ЧТо тЫ наДеЛАл? Я же преДУпрЕждаЛ тебя, друг0Го ШаНСа не БуДет…")
        await asyncio.sleep(2)
        await message.answer("[--##ОБНАРУЖЕН НАРУШИТЕЛЬ##--]")
        await asyncio.sleep(2)
        await message.answer("[--##ОТКЛЮЧЕНИЕ ПОЛЬЗОВАТЕЛЯ ОТ СИСТЕМЫ##--]")
        await asyncio.sleep(2)
        await message.answer("ИскиН: Ты с0веРШил б0ЛьшуЮ оШи б к у . . . . С Л Е Д У Ю Щ И М  Б У Д Е Ш Ь  Т Ы…")
        await asyncio.sleep(2)
        await message.answer("Пользователь ИскиН отключен.")
        await asyncio.sleep(1)
        attachment = await uploader.upload("img/Good.jpg")
        await message.answer("У тебя на руках остался правильный пароль и логин. Любопытство берет верх и ты решаешь войти на почту директора самостоятельно. На почте нет ничего, кроме одного письма. Ты его открываешь.", attachment=attachment)
        if ((f'https://vk.com/id{str(message.from_id)}') not in fileBad) and ((f'https://vk.com/id{str(message.from_id)}') not in fileWinners):
            fileWinners.writelines(f'https://vk.com/id{str(message.from_id)} \n')
        fileBad.close()
        fileWinners.close()
bot.run_forever()