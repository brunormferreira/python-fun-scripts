def main():
    import pyautogui

    # Pauses and Fail-Safes
    pyautogui.PAUSE = 1  # pause 1 second for every pyautogui function call
    pyautogui.FAILSAFE = True  # cause FailSafeException by moving mouse cursor to upper-left corner

    # Moving the Mouse
    print(pyautogui.size())
    print('Running mouse-move')
    print('Press Ctrl-C to quit.')
	
    for i in range(1500):
	pyautogui.click()
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.15)

    for i in range(1500):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

    # Getting the Mouse Position
    print(pyautogui.position())
    print(pyautogui.position())
    print(pyautogui.position())

if __name__ == '__main__':
    main()
