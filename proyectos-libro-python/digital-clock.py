# Proyecto # 19 del libro The big book of small python projects
import sys
import time
import sevSegDisplay
import os

try:
    while True:
        #print('\n' * 60)
        os.system('cls' if os.name == 'nt' else 'clear')

        currentTime = time.localtime()

        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        hDigits = sevSegDisplay.getSevStr(hours, 2)
        hTopRow, hMidRow, hBottomRow = hDigits.splitlines()

        mDigits = sevSegDisplay.getSevStr(minutes, 2)
        mTopRow, mMidRow, mBottomRow = mDigits.splitlines()

        sDigits = sevSegDisplay.getSevStr(seconds, 2)
        sTopRow, sMidRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + '   ' + mTopRow + '   ' + sTopRow)
        print(hMidRow + ' * ' + mMidRow + ' * ' + sMidRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    print('Adiooooos')
    sys.exit()
