from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Venom import OWNER
from Venom import VenomX

DEV_OP = [
    [
        InlineKeyboardButton(text="🍭ᴏᴡɴᴇʀ🍭", user_id=OWNER),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="**❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍**",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="**❍ 𝐘ᴏᴜʀ 𝐂ᴏᴍᴍᴀɴᴅ ❍**", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍁ᴋʜᴜsʜɪ🍁", callback_data="SOURCE"),
        InlineKeyboardButton(text="☁️ ᴀʙᴏᴜᴛ ☁️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="😍 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 😍",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✨ ᴄʟᴏsᴇ ✨",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
        InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="🐳 ʙᴀᴄᴋ 🐳", callback_data="SBACK"),
        InlineKeyboardButton(text="🌲 ᴄʟᴏsᴇ 🌲", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", callback_data="HELP"),
        InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="🚀 ʜᴇʟᴘ 🚀", url=f"https://t.me/{VenomX.username}?start=help"
        ),
        InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="🚀 ʜᴇʟᴘ ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ", user_id=OWNER),
    ],
    [
        InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="BACK"),
    ],
]
