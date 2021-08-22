import schedule
import time
from plyer import notification
import playsound


def water_reminder():

    notification.notify(
        title="**Please Drink Water Now!!",
        message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters)of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon="<icon(.ico) path>",

    )
    playsound.playsound("drink.mp3")

def coding():

    notification.notify(
        title="**coding time**",
        message="Its coding time get up and grab a cup of coffee and dig in",
        app_icon="icon(.ico)  path",
    )
    playsound.playsound('coding.mp3')

def play():

    notification.notify(
        title="**playing time**",
        message="Its playing time go outside and enjoy",
        app_icon="icon(.ico)  path",
    )
    playsound.playsound('playing.mp3')

def classes():

    notification.notify(
        title="**Class time**",
        message="Hey, Your class will start soon. get up",
        app_icon="icon(.ico)  path",
    )
    playsound.playsound('class.mp3')

schedule.every().day.at("21:54").do(coding)
schedule.every(30).minutes.do(water_reminder)
schedule.every().day.at("21:55").do(play)
schedule.every().day.at("21:56").do(classes)

while True:
    schedule.run_pending()
    time.sleep(1)
