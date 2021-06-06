print('Start Mobile testing')

print('\nImport test begin')
try:
    import requests
    from datetime import date
    import time
    print("Import test passed")
except:
    print("Import test Failed")

print('\nRequests test begin')
try:
    today = date.today()
    today = today.strftime("%d-%m-%y")
    response = requests.get(
        f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=365&date={today}')
    print(response.text[:23])
    print('\n\nrequest test Passed\n')
except:
    print('\n\nrequest test Failed\n')

print('\nMail test begins')
try:
    mail = requests.get('https://teshank2137.pythonanywhere.com/senderror/')
    if mail.text == "Success":
        print("test Passed\n")
except:
    print('Failed')
