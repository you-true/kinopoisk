from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config.maping import channels


def genmarkup():
    markup = InlineKeyboardMarkup(row_width=5)
    markup.add(*[InlineKeyboardButton(channels[data]['button'],
                                      callback_data=channels[data]['callback']) for data in channels])
    return markup
