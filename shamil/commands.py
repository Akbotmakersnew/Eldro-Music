# A Subinps Project
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT


HELP = """
🎧 <b>I Can Play Music On VoiceChats 🤪</b>

🎶 **Common Commands**:
• `/current`  __Show current playing song__
• `/help` __Show help for commands__
• `/mwk` __Shows the playlist__
• `/stickerid` __To Get Id Of Replied Sticker__

🎶 **Admin Commands**:
• `/play`  __Reply to an audio file or YouTube link to play it or use /p <song name>__
• `/dplay` __Play music from Deezer, Use /d <song name>__
• `/skip [n]` __...Skip current or n where n >= 2__
• `/join`  __Join voice chat__
• `/leave`  __Leave current voice chat__
• `/mwk`  __Check which VC is joined__
• `/stop`  __Stop playing__
• `/radio` __Start Radio__
• `/stopradio` __Stops Radio Stream__
• `/replay`  __Play from the beginning__
• `/clear`  __Remove unused RAW PCM files__
• `/pause` __Pause playing__
• `/resume` __Resume playing__
• `/mute`  __Mute in VC__
• `/unmute`  __Unmute in VC__
• `/update` __Update Current Settings n Restarts the Bot__

© Powered By 
  @EldroSupportGroup
"""
