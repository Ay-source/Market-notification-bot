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
    import playsound
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta
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
    while True:
        value_gotten_from_data, _type = get_chart_data()
        if value_gotten_from_data == True:
            for i in range(2):
                try:
                    playaudio(audio_file_path)
                except KeyboardInterrupt:
                    pass
            print(f"You should {_type}")
        time.sleep(20)

def get_chart_data():
    tv = tvDatafeed.TvDatafeed(chromedriver_path=None)#chromedriver_path=r"C:\Users\aolam\Downloads\installation_files\chromedriver_win32")
    data_interval = tv.get_hist('XAUUSD', 'GLOBALPRIME', interval = tvDatafeed.Interval.in_15_minute, n_bars = 5)
    open = list(data_interval['open'])
    open.reverse()
    close = list(data_interval['close'])
    close.reverse()
    high = list(data_interval['high'])
    high.reverse()
    low = list(data_interval['low'])
    low.reverse()
    datet = list(data_interval.index)
    datet.reverse()
    if ((datetime.now() - datet[0]) <= timedelta(minutes = 15)):
        for i in [open, close, high, low]:
            del(i[0])
    _type = pinbar(open[0], high[0], low[0], close[0])
    if _type:
        return True, _type
    else:
        return False, False

def pinbar(o, h, l, c):
    """Checks if the market printed a pinbar formation."""
    bearish = False
    if o > c:
        bearish = True
    if (((h - o) >= abs(o - c)) or (((h - c) >= abs(o - c)) and not bearish)):
        return 'sell'
    elif ((((o - l) >= abs(o - c)) and not bearish) or ((c -l) >= abs(o - c))):
        return 'buy'

def playaudio(file_path):
    #song = pydub.AudioSegment(file_path)
    #pydub.playback.play(song)
    playsound.playsound(file_path)

if __name__ == '__main__':
    while True:
        value_gotten_from_data = False
        audio_file_path = r"C:\Users\aolam\Documents\IT\dev\Codes\self_projects\python\market_notification_bot\mixkit-city-alert-siren-alert.wav"
        #audio_file_path = r"C:\Users\aolam\Documents\IT\dev\Codes\self_projects\python\market_notification_bot\mixkit-classic-alarm-notify.wav"
        #audio_file_path = r"C:\Users\user\Music\Other\I_miss_you(256k).mp3"
        main(value_gotten_from_data)
        time.sleep(60)
