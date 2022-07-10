from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🌹 **Hey** <b>{}</b>

**Welcome to** <b>{}</b>

**ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴅᴏᴄᴜᴍᴇɴᴛs ᴀɴᴅ ꜰɪʟᴇs ᴡɪᴛʜ ᴄᴇʀᴛᴀɪɴ ᴏᴛʜᴇʀ ꜰᴇᴀᴛᴜʀᴇs ᴜsᴇ /help ᴛᴏ ʟᴇᴀʀɴ ʜᴏw!** 

**ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❗** **@robo_glitch**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔮 ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs🔮", url="https://t.me/futurebackups")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓", callback_data="help"),
            InlineKeyboardButton("😈 ᴀʙᴏᴜᴛ 😈", callback_data="about")
        ],
        [InlineKeyboardButton("📢 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💡", url="https://t.me/hddubhub4u")],
        [InlineKeyboardButton("📮 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 📮", url="https://t.me/hddubhub4uhelp")],
    ]

    # Help Message
    HELP = """
**Just send a document / video to start renaming. Then when asked, give the new name for the file. The bot will download the file and upload with new name**

1) To have a custom thumbnail on your file, add an 'jpg' image as thumbnail using /thumbnail command.
2) By default, videos are uploaded as videos. To prompt the bot to upload video as document, use /settings to change settings.

🛠 **Available Commands** 🛠

/thumbnail - Change thumbnail settings
/settings - Change default settings
/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**✧✧✧ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ✧✧✧**

📍 📁 **ꜰɪʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ ʙʏ** **@robo_glitch**

📞 **ᴄᴏɴᴛᴀᴄᴛ** : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](http://t.me/GlitchAssistantBot)**〡**[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Chat_With_Mr_Devil_bot)**

📢 **ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ** ❤ : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](http://t.me/hddubhub4u)**

📮**Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 📮** : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/hddubuhub4uhelp)**

🎥 **ᴍᴏᴠɪᴇ's ɢʀᴏᴜᴘ** : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/dubbedweb)**

😈 **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : **@the_glitchs**
    """
