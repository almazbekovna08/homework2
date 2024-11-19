from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
     [KeyboardButton(text='О нас'), KeyboardButton(text='Направления')],
     [KeyboardButton(text='Контакты ')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,  input_field_placeholder='Выберите кнопку')

dir_keyboard=ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend')], [KeyboardButton(text='UI-UX дизайн')],
     [KeyboardButton(text='Android'), KeyboardButton(text='IOS')], 
],  input_field_placeholder='Выберите кнопку')