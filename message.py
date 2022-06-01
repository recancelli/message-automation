import pyautogui
import time

# Lyric
script = "all the time I turn around brothas gather round always looking at me up and down looking at my UHHH I just wanna say it now, I ain't tryin' to round up drama, little mama I don't wanna take your man and I know I'm comin' off just a little bit conceited and I keep on repeating how the boys wanna eat it but I'm tryin' to tell that I can't be treated like clientele cause they say she delicious so delicioussss"

# Open whatsapp
# Numbers of whatsapp's location on my computer
pyautogui.moveTo(863, 751, duration=2)
pyautogui.click()
time.sleep(2)

# Type and Enter
for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")
    # time.sleep(0.10)
