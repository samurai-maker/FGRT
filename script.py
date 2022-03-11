class Script(object):
    START_TXT = """
      
<b>ഹായ് {}!!</b>

<b>വെൽക്കം ടു കുല്സിതം</b>

"""
HELP_TXT = """

    


<b>ലിങ്ക് എനിക്ക് അയച്ചു താ ഞാൻ ഡൌൺലോഡ് ചെയ്യാം</b>

"""

    ABOUT_TXT = """
nothing
"""

    SOURCE_TXT = """
 
<b>നീലതാമര</b>
"""

    MANUALFILTER_TXT = """nothing



"""

    BUTTON_TXT = """nothing"""

    FILLINGS_TXT = """nothing
"""

    AUTOFILTER_TXT = """nothing."""

    CONNECTION_TXT = """nothing"""

    AUTO_MANUAL_TXT = """nothing"""

    PASTE_TXT = """nothing

"""

    TGRAPH_TXT = """nothing"""

    INFO_TXT = """ nothing."""

    TORRENT_TXT = """nothing"""

    GTRANS_TXT = """nothing"""

    SEARCH_TXT = """nothing."""

    PURGE_TXT = """nothing"""

    RESTRIC_TXT = """nothing"""

    PIN_MESSAGE_TXT = """nothing"""

    ADMIN_TXT = """

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """

എന്റെ സേവനം ലഭ്യമാക്കാൻ ഈ ചാനലിൽ ജോയിൻ ചെയ്യുക
"""

    MEMES_TXT = """Help: <b>Memes</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
• /throw or /dart - t𝗈 m𝖺𝗄𝖾 drat 
• /roll or /dice - roll the dice 
• /goal or /shoot - to make a goal or shoot
• /luck or /cownd - Spin the Lucky
• /runs strings

"""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.



<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """nothing."""

    MUSIC_TXT = """nothing"""

    PASSWORD_GEN_TXT = """nothing"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""

