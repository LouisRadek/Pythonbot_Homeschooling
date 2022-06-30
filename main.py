import datetime, time, os, pyautogui, playsound

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def min(x, y):
    x *= 60
    return (x + y)

updating_Animation = [
    '[.  ]     ',
    '[.. ]     ',
    '[...]     '
]

started = False
updating_Frame = 0
executed = 0
weekday = datetime.date.today().weekday()
currentTime = min(datetime.datetime.now().hour, datetime.datetime.now().minute)
os.system ("cls")

def Start():
    if (weekday >= 5 or Holiday() == True):
        time.sleep(30)
        Discord()
        os.system ('start ""')
        time.sleep(1)
        pyautogui.write('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"  https://www.youtube.com/ https://www.netflix.com/browse/ https://geizhals.de/' '&& exit')
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(1)
        pyautogui.click(1600, 700)
        time.sleep(5)
        exit()

def CheckHoliday(x, y, _y, z, _z): #year, month, monthEnd, day, dayEnd
    days = (datetime.date(x, y, z) - datetime.date.today()).days
    _days = (datetime.date(x, _y, _z) - datetime.date.today()).days
    if (days <= 0 and _days >= 0):
        return True
    return False

def Holiday():
    if (CheckHoliday(2021, 3, 4, 31, 11)):
        return True
    elif (CheckHoliday(2021, 5, 6, 23, 6)):
        return True
    elif (CheckHoliday(2021, 7, 9, 29, 11)):
        return True
    elif (CheckHoliday(2021, 5, 5, 13, 16)):
        return True
    return False

def Execution(path, x, *screen):
    try: 
        execution = pyautogui.locateCenterOnScreen('Images/' + path, region = (screen))
        pyautogui.click(execution.x - 1920, execution.y)
        time.sleep(x)
    except: playsound.playsound('Sounds/Error.mp3')

def Discord():
    Execution('Discord.png', 1, 0, 265, 1400, 840)
    Execution('Channel.png', 0, 0, 265, 1400, 840)

def Join(): 
    time.sleep(1)
    pyautogui.click(395, 180)
    time.sleep(2)
    pyautogui.click(1150, 780)
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    pyautogui.hotkey('ctrl', 'w')
    playsound.playsound("Sounds/Message.mp3")

def Complete(j):
    Execution( j , 3, 3720, 700, 2500, 840)
    pyautogui.click(1076, 598)
    pyautogui.click(1220, 700)
    pyautogui.hotkey('ctrl', 'w')
   
def Open_Link(id):
    os.system ('start ""') 
    time.sleep(1)
    pyautogui.write('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" https://04104644.moodle.belwue.de/moodle/' + id +' && exit')
    pyautogui.press('enter')

def BBB_Join():
    time.sleep(2)
    repeat = 0
    if (pyautogui.locateCenterOnScreen('Images/notakepart.png', region = (2390, 700, 860, 900))):
        while pyautogui.locateCenterOnScreen('Images/takepart.png', region = (2390, 700, 860, 900)) == False and repeat <= 50:
            repeat += 1 
            time.sleep(5)
        if (repeat > 50):
            playsound.playsound("Sounds/Error.mp3")
            return
        elif (pyautogui.locateCenterOnScreen('Images/takepart.png', region = (2390, 700, 860, 900))):
            Execution('takepart.png', 1, 2390, 700, 860, 900)
            for _ in range(5):
                time.sleep(2)
                if (pyautogui.locateCenterOnScreen('Images/micro.png', region = (2920, 635, 1300, 920))):
                    Execution('micro.png', 2920, 635, 1300, 920)
                    break
            time.sleep(1)
            Join() 
        else:
            pyautogui.hotkey('ctrl', 'w')
            return
    else:
        Execution('takepart.png', 10, 2390, 700, 860, 900)
        Execution('micro.png', 3, 2920, 635, 1300, 920)
        Join()

def Attendence_complete():
    time.sleep(3)
    pyautogui.moveTo(100, 100)
    for i in range(5):
        if(pyautogui.locateCenterOnScreen('Images/Capture.png', region = (3820, 640, 2450, 1100))):
            Complete('Capture.png')
            break
        else:
            if(pyautogui.locateCenterOnScreen('Images/Capture2.png', region = (3820, 640, 2450, 1100))):
                Complete('Capture2.png')
                break
            else:
                pyautogui.scroll(-425)
                if (i == 4):
                    playsound.playsound("Sounds/Error.mp3")
                    pyautogui.hotkey('ctrl', 'w')
        
def BBB_search():
    time.sleep(3)
    for i in range(10): 
        if (pyautogui.locateCenterOnScreen('Images/BBB.png', region = (2465, 475, 1360, 1180))):
            Execution('BBB.png', 1, 2465, 475, 1360, 1180)
            break
        else:
            pyautogui.scroll(-425)
            if (i == 9):
                playsound.playsound("Sounds/Error.mp3")
                pyautogui.hotkey('ctrl', 'w')

def Schedule(): 
    global started 
    global weekday
    if (started == False):
            started = True
            time.sleep(30)
            Discord()
            os.system('start ""')
            time.sleep(1)
            pyautogui.write('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" https://www.youtube.com/ https://04104644.moodle.belwue.de/moodle/my/ https://www.netflix.com/browse/ https://geizhals.de/ && exit')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.click(1040, 630)
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.click(1600, 700)
            pyautogui.hotkey('ctrl', '1')
    elif (weekday == 0): 
        Monday()
    elif (weekday == 1):
        Thuesday()
    elif (weekday == 2):
        Wednesday()
    elif (weekday == 3):
        Thursday()
    elif (weekday == 4):
        Friday()

def Monday(): 
    global executed 
    global currentTime
    if (currentTime == min(7,45) and executed != 1):
        executed = 1
        Open_Link('course/view.php?id=208') #Link Reli-Moodleraum
        BBB_search()
        BBB_Join()
        #Open_Link('course/view.php?id=208 && exit') #Link zum Reli-Raum 
        #Attendence_complete()
    elif (currentTime == min(9,35) and executed != 2):
        executed = 2    
        Open_Link('course/view.php?id=764') #Link zum IMP-Pysikraum
        BBB_search()
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=6599') #Anwesenheitslink IMP Physik
        Attendence_complete() 
    elif (currentTime == min(10,20) and executed != 3):
        executed = 3       
        Open_Link('course/view.php?id=419') #Link zum IMP-Informatik
        BBB_search()
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=15108') #Anwesenheitslink ImP-Info
        Attendence_complete()
    elif (currentTime == min(11,25) and executed != 4):
        executed = 4
        Open_Link('mod/bigbluebuttonbn/view.php?id=32375') #BBB Englisch
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=12126') #Anwesenheit Englisch
        Attendence_complete()
    elif (currentTime == min(12,10) and executed != 5):
        executed = 5
        Open_Link('mod/bigbluebuttonbn/view.php?id=32576') #BBB Mathe
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=6741') #Anwesenheit Mathe
        Attendence_complete() 
    elif (currentTime == min(15,40) and executed != 6):
        executed = 6
        Open_Link('mod/bigbluebuttonbn/view.php?id=35947') #BBB WBS
        BBB_Join()
        exit()

def Thuesday():
    global executed
    global currentTime
    if (currentTime == min(7,45) and executed != 1):
        executed = 1
        Open_Link('mod/bigbluebuttonbn/view.php?id=32907') #BBB Deutsch
        BBB_Join()
    elif (currentTime == min(8,30) and executed != 2):
        executed = 2    
        Open_Link('mod/bigbluebuttonbn/view.php?id=23953') #BBB Latein
        BBB_Join()
    elif (currentTime == min(11,25) and executed != 3):
        executed = 3       
        Open_Link('course/view.php?id=578') #Link zum Pysikraum
        BBB_search()
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=23299') #Anwesenheit Physik
        Attendence_complete()
    elif (currentTime == min(14,00) and executed != 4):
        executed = 4
        Open_Link('mod/bigbluebuttonbn/view.php?id=31114') #BBB Gk
        BBB_Join()
    elif (currentTime == min(15,40) and executed != 5):
        executed = 5
        Open_Link('mod/bigbluebuttonbn/view.php?id=1221') #BBB Chemie
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=2871') #Anwesenheit Chemie
        Attendence_complete()
        exit()

def Wednesday():
    global executed
    global currentTime
    if (currentTime == min(7,45) and executed != 1):
        executed = 1
        Open_Link('mod/bigbluebuttonbn/view.php?id=1480') #BBB Geschichte
        BBB_Join()
    elif (currentTime == min(9,35) and executed != 2):
        executed = 2    
        Open_Link('mod/bigbluebuttonbn/view.php?id=32907') #BBB Deutsch
        BBB_Join()
    elif (currentTime == min(11,25) and executed != 3):
        executed = 3       
        Open_Link('mod/bigbluebuttonbn/view.php?id=23953') #BBB Latein
        BBB_Join()
        exit()

def Thursday():
    global executed
    global currentTime
    if (currentTime == min(7,45) and executed != 1):
        executed = 1
        Open_Link('course/view.php?id=901 && exit') #Link zum Bioraum
        BBB_search()
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=16996') #Anwesenheit Bio 
        Attendence_complete()
    elif (currentTime == min(9,35) and executed != 2):
        executed = 2    
        Open_Link('mod/bigbluebuttonbn/view.php?id=32907') #BBB Deutsch
        BBB_Join()
    elif (currentTime == min(10,20) and executed != 3):
        executed = 3       
        Open_Link('mod/bigbluebuttonbn/view.php?id=32576') #BBB Mathe
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=6741') #Anwesenheit Mathe
        Attendence_complete()
    elif (currentTime == min(11,25) and executed != 4):
        executed = 4
        Open_Link('course/view.php?id=312') #Link zum IMP-Matheraum 
        BBB_search
        BBB_Join
        #Open_Link('course/view.php?id=312 && exit') #Link zum IMP-Matheraum
        #Attendence_complete()
        exit()

def Friday():
    global executed
    global currentTime
    if (currentTime == min(7,45) and executed != 1):
        executed = 1
        Open_Link('mod/bigbluebuttonbn/view.php?id=32576') #BBB Mathe
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=6741') #Anwesenheit Mathe
        Attendence_complete()
    elif (currentTime == min(9,35) and executed != 2):
        Open_Link('course/view.php?id=888') #Link zum BK-Raum
        executed = 2    
        BBB_search()
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=18799') #Anwesenheit BK
        Attendence_complete()
    elif (currentTime == min(11,25) and executed != 3):
        executed = 3       
        Open_Link('mod/bigbluebuttonbn/view.php?id=32375') #BBB Englisch
        BBB_Join()
        Open_Link('mod/attendance/view.php?id=12126') #Anwesenheit Englisch
        Attendence_complete()
        exit()

Start()

while True:
    currentTime = min(datetime.datetime.now().hour, datetime.datetime.now().minute)
    Schedule() 
    print(updating_Animation[updating_Frame % len(updating_Animation)], end = '\r')
    time.sleep(1)
    updating_Frame += 1