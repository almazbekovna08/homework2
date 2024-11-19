from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import CommandStart, Command

from aiogram import Router

from app.keyboards import *

router=Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Здравствуйте! \nВас привесттвует компания Geeks', reply_markup=keyboard)

@router.message(F.text=='О нас')
async def cmd_about(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6lkqYtQ1s_EQNAI_pdjiP20sQjk-gdTCldQ&s')
    await message.reply("""Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию. На сегодняшний день более 1000 студентов в возрасте от 12 до 45 лет изучают здесь самые популярные и востребованные IT-профессии. Филиальная сеть образовательного центра представлена в таких городах, как Бишкек, Ош и Кара-Балта.""")

@router.message(F.text=='Направления')
async def cmd_directions(message: types.Message):
    await message.reply('У нас предоставляются 5 основных видов направления:', reply_markup=dir_keyboard)

@router.message(F.text=='Backend')
async def cmd_back(message: types.Message):
    await message.answer_photo(photo='https://newline.tech/wp-content/uploads/2023/07/Profession_-Backend-Developer.png')
    await message.reply("""Backend — это внутренняя часть сайта. Backend занимается разработкой серверной части веб-приложений и сайтов. Он отвечает за работу баз данных, серверов и логику, которая происходит на серверной стороне. 
Стоимость: 12.000 сом в месяц. 
Обучение: 5 месяцев""")

@router.message(F.text=='Frontend')
async def cmd_front(message: types.Message):
    await message.answer_photo(photo='https://worksolutions.ru/uploads/large_t_DUW_3hn_Ao_Qe_SQV_5x_Col_Rr_E_Ly_MYZ_Ial_OKFI_7zmza_N_02f17d7c57.png')
    await message.reply("""Frontend — это клиентская часть продукта (интерфейс, с которым взаимодействует пользователь).
Стоимость: 12.000 сом в месяц. 
Обучение: 5 месяцев""")
    
@router.message(F.text=='UI-UX дизайн')
async def cmd_design(message: types.Message):
    await message.answer_photo(photo='https://www.aufaitux.com/wp-content/uploads/2020/05/UIUX-designing-1.jpg')
    await message.reply("""UI ― это user interface, пользовательский интерфейс, проще говоря ― оформление сайта: сочетания цветов, шрифты, иконки и кнопки. UX ― это функционал интерфейса, UI ― его внешний вид. В современном дизайне UX и UI практически всегда идут рядом, потому что они очень тесно связаны.
Стоимость: 10.000 сом в месяц. 
Обучение: 4 месяца""")

@router.message(F.text=='Android')
async def cmd_android(message: types.Message):
    await message.answer_photo(photo='https://assets.dunked.com/assets/prod/22884/700x0_p17s2tfgc31jte13d51pea1l2oblr3.png')
    await message.reply("""Android-разработка — это процесс создания приложений для устройств на базе операционной системы Android (смартфонов, планшетов, часов, телевизоров и других). Для этого используются языки программирования, такие как Kotlin или Java, а также инструменты вроде Android Studio. Разработка включает проектирование интерфейса написание кода, работу с данными, интеграцию API и тестирование.).
Стоимость: 12.000 сом в месяц. 
Обучение: 5 месяцев""")
    
@router.message(F.text=='IOS')
async def cmd_ios(message: types.Message):
    await message.answer_photo(photo='https://play-lh.googleusercontent.com/FCcziMA1_M9nGlJo6EnguMKlJ53Yor3tNmSqDUza9w9_wXrFLiAW2cOz-kD8S-N1Vvg=w240-h480-rw')
    await message.reply("""iOS-разработка — это создание приложений для устройств Apple (iPhone, iPad, Apple Watch). Используются языки Swift и Objective-C, а также среда разработки Xcode. Процесс включает проектирование интерфейса, написание кода, тестирование и оптимизацию.).
Стоимость: 12.000 сом в месяц. 
Обучение: 5 месяцев""")
    
@router.message(F.text.in_({'Контакты', 'контакты'}))
async def contact(message:types.Message):
    await message.reply_contact(phone_number='+996509082021', first_name='"Geeks"', last_name='Courses')

@router.message(F.text.in_({'Адрес', 'адрес'}))
async def location(message:types.Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)

@router.message()
async def echo(message: types.Message):
    await message.answer('Я вас не понял')