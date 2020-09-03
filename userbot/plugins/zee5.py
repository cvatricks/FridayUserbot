""" Powered by @Google
Available Commands:
.zee5 <query> credits to owner of bot
"""

import asyncio
import os
from re import findall
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
from urllib.parse import quote_plus
from urllib.error import HTTPError
from google_images_download import google_images_download
from gsearch.googlesearch import search
from userbot.utils import admin_cmd
from search_engine_parser import GoogleSearch
import requests
import bs4
import re
import html5lib


def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))



@borg.on(admin_cmd("zee5 (.*)"))
async def gsearch(q_event):
    """ For .google command, do a Google search. """
    match = q_event.pattern_match.group(1)
    url = match
    t = "https://useraction.zee5.com/tokennd/"
    q = requests.get(t)
    t1 = (eval(q.text)["video_token"])
    r = requests.get(url)
    b = bs4.BeautifulSoup(r.content.decode('utf-8'), "html5lib")
    c = b.find_all("script")[9].prettify()
    G = []
    for i in c.split(","):
      if "hls" in i:
        G.append(i)
    #pr = ((G[-1])[11:-1]).replace("drm", "hls")
    #te = ("https://{}".format("zee5vodnd.akamaized.net") + pr + t1)
    pr = ("https://zee5vodnd.akamaized.net{}".format((G[-1])[11:-1] + t1).replace("drm", "hls"))
    await q_event.edit(pr,
                       link_preview=False)
