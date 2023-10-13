from pykeyboard import PyKeyboard
import pyperclip
import requests
import time
import random
import sqlite3

k = PyKeyboard()


def sendMsg(msg):
    pyperclip.copy(msg)
    time.sleep(.1)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    time.sleep(.1)
    k.tap_key(k.enter_key)


if __name__ == "__main__":
    time.sleep(1)
    conn = sqlite3.connect('../data.db')
    c = conn.cursor()
    try:
        while True:
            c.execute('SELECT * FROM main ORDER BY RANDOM() limit 1')
            data = (c.fetchall())[0][1]
            data1 = data.replace("妈", "🐴")
            sendMsg(data1)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("exit,bye")
        conn.close()
        sys.exit(0)
