#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from config import Config
import pyrogram
if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "tilon",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
