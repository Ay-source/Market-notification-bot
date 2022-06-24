#usr python3
"""
This program plays an mp3 file when an engulfing candle or pin bar is printed on the market.

Requirements:


This program was created by Oke Ayomide on the 11th of December, 2021.
Social media:
twitter:
Whatsapp: +2349061145027
Instagram
"""

try:
    import time
    import tvDatafeed
    #import pydub
    import playsound
    import csv
    import pandas as pd
    try:
        from credentials import username, password
    except:
        username = input("Please input your tradingview username: ")
        password = input("Please input your tradingview password: ")
        with open('credentials.py', 'w+') as f:
            f.write('username = "' + username + '"\n')
            f.write('password = "' + password + '"\n')
except:
    raise ImportError("""You haven't imported the required modules from requirements.txt
             You can fix this by running the command 'python -m pip install -r requirements.txt'
    """)

def main(value_gotten_from_data):
    while value_gotten_from_data == False:
        value_gotten_from_data = get_chart_data()
        if value_gotten_from_data == True:
            for i in range(2):
                try:
                    playaudio(audio_file_path)
                except KeyboardInterrupt:
                    pass
                print(f"played {i}")

def get_chart_data():
    tv = tvDatafeed.TvDatafeed(username, password, chromedriver_path=r"C:\Users\aolam\Downloads\installation_files\chromedriver_win32")
    data_interval = tv.get_hist('XAUUSD', 'GLOBALPRIME', interval = tvDatafeed.Interval.in_15_minute, n_bars = 5)
    open = list(data_interval['open'])
    close = list(data_interval['close'])
    high = list(data_interval['high'])
    low = list(data_interval['low'])
    '''
    if (condition):
        return True
    else:
        return False
    '''
    return True

def pinbar(o, h, l, c):
    bearish = False
    if o > c:
        bearish = True

    print(bearish)
    if (((h - o) >= abs(o - c)) or (((h - c) >= abs(o - c)) and not bearish)):
        return True, 'sell'
    elif ((((o - l) >= abs(o - c)) and bearish) or ((c -l) >= abs(o - c))):
        return True, 'buy'

def playaudio(file_path):
    #song = pydub.AudioSegment(file_path)
    #pydub.playback.play(song)
    playsound.playsound(file_path)

if __name__ == '__main__':
    while True:
        value_gotten_from_data = False
        audio_file_path = r"C:\Users\user\Documents\IT\dev\Codes\self_projects\python\market_notification_bot\mixkit-city-alert-siren-alert.wav"
        #audio_file_path = r"C:\Users\user\Documents\IT\dev\Codes\self_projects\python\market_notification_bot\mixkit-classic-alarm-notify.wav"
        #audio_file_path = r"C:\Users\user\Music\Other\I_miss_you(256k).mp3"
        if main(value_gotten_from_data) is True:
            playsound(audio_file_path)
        time.sleep(60)
