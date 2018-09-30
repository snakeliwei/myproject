# test.py
#!/usr/bin/env python3
# encoding: utf-8
# Author: lyndon
# dependence: selenium & chromedriver


import os
import time
import csv
import asyncio
import threading
import random
from selenium import webdriver

async def meeting_join(data):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    prefs = {'profile.content_settings.exceptions.plugins': {
                    "http://e.vhall.com:80,*": {
                        "last_modified": "13169358065549109",
                        "setting": 1
                    },
                    "http://live.vhall.com:80,*": {
                        "last_modified": "13171618834348431",
                        "setting": 1
                    },
                    "http://daiichisankyo.mctoday.cn:80,*": {
                        "last_modified": "13172056641866684",
                        "setting": 1
                    }
                }
            }
    options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options = options)

    browser.get('http://daiichisankyo.mctoday.cn/index.php/Home/Index/Index/id/e2c32ecCRThBUJja2Hdaq1GcLaWAwVdjJcBQ6H50HQcqCX2/position/signin')
    browser.implicitly_wait(10)
    browser.add_cookie({'name': 'Sangong_Key','value': str(data)})
    browser.get('http://daiichisankyo.mctoday.cn/index.php/Home/Index/Index/id/e2c32ecCRThBUJja2Hdaq1GcLaWAwVdjJcBQ6H50HQcqCX2/position/signin')
    # await asyncio.sleep(300)
    # browser.save_screenshot(data[1]+'.png')
    await asyncio.sleep(3600)
    browser.quit()
    

if __name__=='__main__':
    # filename = './user.csv'
    # with open(filename) as f:
    #     reader = csv.reader(f)
    reader=random.sample(range(28540,28556),12)
    loop = asyncio.get_event_loop()
    tasks = [meeting_join(data) for data in reader]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
