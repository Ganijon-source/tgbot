import requests

TOKEN = '7542472244:AAF_uzh6u6yy9wVZcGJ7r-Z9rhR51byUv04'

CHAT_ID = 5518313994

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }   
    r = requests.post(url, params=params)
    return r.json()

def send_audio(chat_id):

    url=f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    a='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
    params= {
        'chat_id': chat_id,
        'audio':a
    }
    response=requests.post(url,data=params)
    return response.json()

def send_photo(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    photo = 'https://www.bing.com/images/search?view=detailV2&ccid=fUyaSZN2&id=F79F42503F2AD53FA1D1200833969D4CE038D611&thid=OIP.fUyaSZN2qwjjnKmJpWAwZgHaD4&mediaurl=https%3a%2f%2fi.pinimg.com%2foriginals%2f3d%2faa%2f29%2f3daa29a746de6ce99cb4256050c2bd47.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.7d4c9a499376ab08e39ca989a5603066%3frik%3dEdY44EydljMIIA%26pid%3dImgRaw%26r%3d0&exph=1423&expw=2711&q=mustang&simid=608054790385846220&FORM=IRPRST&ck=C4E9CB1487B3F41C25E5B55716E4DC11&selectedIndex=9&itb=0'
    params = {
        'chat_id': chat_id,
        'photo': photo
    }
    response = requests.post(url, params=params)
    return response.json()

def send_document(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    document = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    params = {
        'chat_id': chat_id,
        'document': document
    }
    response = requests.post(url, params=params)
    return response.json()

def send_video(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    video = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    params = {
        'chat_id': chat_id,
        'video': video
    }
    response = requests.post(url, params=params)
    return response.json()

def send_sticker(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
    sticker = "CAADAgADBQADAAECAf6qKQ5-k_a-Ag"
    params = {
        'chat_id': chat_id,
        'sticker': sticker
    }
    response = requests.post(url, params=params)
    return response.json()

def send_location(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
    latitude = 38.8977
    longitude = -77.0365
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude
    }
    response = requests.post(url, params=params)

    return response.json()

def send_contact(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendContact"
    phone_number = "+998999999999"
    first_name = "G'anijon"
    last_name = "Abdiraxmonov"
    params = {
        'chat_id': chat_id,
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name
    }
    response = requests.post(url, params=params)
    return response.json()

def send_poll(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"
    question = "What's your favorite color?"
    options = ["red", "blue", "green"]
    params = {
        'chat_id': chat_id,
        'question': question,
        'options': options,
        'is_anonymous': True,
        'type': "regular"
    }
    response = requests.post(url, params=params)
    return response.json()
if __name__ == "__main__":

    send_message("Hello! G'anijon, I am you AI.", CHAT_ID)
    send_audio(CHAT_ID)
    send_photo(CHAT_ID)
    send_document(CHAT_ID)
    send_video(CHAT_ID)
    send_sticker(CHAT_ID)
    send_location(CHAT_ID)
    send_contact(CHAT_ID)
    send_poll(CHAT_ID)

    updates = get_updates()
    print("Latest updates:", updates)
