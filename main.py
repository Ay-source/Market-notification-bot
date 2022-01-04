#usr python3
"""
This program plays an mp3 file when an engulfing candle or pin bar is printed on the market.

Requirements:


This program was started by Oke Ayomide on the 11th of December, 2021.
Social media:
twitter:
Whatsapp: +2349061145027
Instagram
"""

try:
    import tvDatafeed
    #import pydub
    import playsound
    try:
        from credentials import username, password
    except:
        username = input("Please input your tradingview username: ")
        password = input("Please input your tradingview password: ")
        with open('credentials.py', 'w+') as f:
            f.write('username = ' + username + '\n')
            f.write('password = ' + password + '\n')
except:
    raise ImportError("""You haven't imported the required modules from requirements.txt
             You can fix this by running the command 'python -m pip install -r requirements.txt'
    """)

def main():
    get_chart_data()
    for i in range(2):
        try:
            playaudio(audio_file_path)
        except KeyboardInterrupt:
            pass
        print(f"played {i}")
    pass

def get_chart_data():
    tv = tvDatafeed.TvDatafeed(username, password)
    data_interval = tv.get_hist('XAUUSD', interval = tvDatafeed.Interval.in_15_minute)
    print(data_interval)
    pass

def playaudio(file_path):
    #song = pydub.AudioSegment(file_path)
    #pydub.playback.play(song)
    playsound.playsound(file_path)

if __name__ == '__main__':
    audio_file_path = r"C:\Users\user\Documents\Codes\self_projects\python\market_notification_bot\mixkit-classic-alarm-notify.wav"
    #audio_file_path = r"C:\Users\user\Music\Other\I_miss_you(256k).mp3"
    main()
