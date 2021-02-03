import re
import traceback
import urllib.request as ur
import winsound
from datetime import datetime
from time import sleep

url = 'https://finance.yahoo.com/quote/GME'
prefix = '32">'
regex = fr'{prefix}-?[.0-9]+'
pattern = re.compile(regex)
CHECK_COUNT = 0


def get_price():
    found_price_str = re.findall(pattern, str(ur.urlopen(url).read()))
    return float(found_price_str[0].split(prefix)[1])


def short_beep():
    frequency_hz = 500
    duration_ms = 500
    winsound.Beep(frequency_hz, duration_ms)


def wait_until_price_changes():
    global CHECK_COUNT
    while True:
        price = get_price()
        print(f'{price} - {datetime.now().strftime("%H:%M:%S")}')

        if not (90 <= price <= 110):
            return

        CHECK_COUNT += 1
        if CHECK_COUNT % 40 == 0:
            short_beep()
        sleep(15)


def strong_beep(frequency_hz=2500):
    duration_ms = 1000
    winsound.Beep(frequency_hz, duration_ms)
    sleep(0.5)


def beep_non_stop(freq=None):
    while True:
        strong_beep(freq)


if __name__ == '__main__':
    # Test sound level
    strong_beep()
    short_beep()

    try:
        wait_until_price_changes()
        beep_non_stop()
    except Exception as e:
        traceback.print_exc()
        beep_non_stop(400)
