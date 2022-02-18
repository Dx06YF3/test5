

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Button(object):

      BUTTONS01 = InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="📁 lol", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜv", switch_inline_query_current_chat="1 ") ],
                                          [ InlineKeyboardButton(text="📁 lol", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜv", switch_inline_query_current_chat="2 ") ],
                                          [ InlineKeyboardButton(text="📁 lol", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜj", switch_inline_query_current_chat="3 " ) ],
                                          [ InlineKeyboardButton(text="📁 lol", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜh", switch_inline_query_current_chat="4 ") ],
                                          [ InlineKeyboardButton(text="❌", callback_data="X0") ] ] )
