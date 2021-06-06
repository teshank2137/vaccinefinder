import requests
from datetime import date
import time
# import playsound

flag = 0
i = 0
while True:
    today = date.today()
    today = today.strftime("%d-%m-%y")
    # print(today)

    response = requests.get(
        f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=365&date={today}')

    response_obj = response.json()
    try:
        for center in response_obj['centers']:
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session['available_capacity_dose1'] > 0:
                    print('found a vaccine session')
                    # playsound.playsound(
                    #     'D:/Work/Projects/MyProjects/vaccine/found.mp3', True)

                    if flag == 0:
                        mail = requests.get(
                            'https://teshank2137.pythonanywhere.com/send/')
                        if mail.text == "Success":
                            flag = 1
                            print("Mail sent successfully")

                    time.sleep(1200)
                    continue

    except:
        print("error in fetching from api")
        time.sleep(5)
        continue

    finally:
        print('not found', i)
        i += 1
    time.sleep(120)
