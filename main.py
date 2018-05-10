bank_x_offset = 8
bank_y_offset = 25
ghouls_x_offset = 90
ghouls_y_offset = 245

import autopy
from random import randint
from time import sleep
bank_icon = autopy.bitmap.Bitmap.open("bank_icon.png")

def click_bank():
    screenshot = autopy.bitmap.capture_screen()
    bank_coordinates = screenshot.find_every_bitmap(bank_icon)

    if len(bank_coordinates) != 1:
        quit("Error: " + str(len(bank_coordinates)) + " bank icons detected")

    autopy.mouse.smooth_move(bank_coordinates[0][0] + bank_x_offset + randint(-2, 2),
                             bank_coordinates[0][1] + bank_y_offset + randint(-2, 2))
    sleep(2)
    autopy.mouse.click()
    autopy.mouse.click()

def click_ghouls():
    screenshot = autopy.bitmap.capture_screen()
    bank_coordinates = screenshot.find_every_bitmap(bank_icon)

    if len(bank_coordinates) != 1:
        quit("Error: " + str(len(bank_coordinates)) + " bank icons detected")

    autopy.mouse.smooth_move(bank_coordinates[0][0] + ghouls_x_offset + randint(-2, 2),
                             bank_coordinates[0][1] + ghouls_y_offset + randint(-2, 2))
    sleep(2)
    autopy.mouse.click()
    autopy.mouse.click()

def main():
    print "Do not use this in Jagex RuneScape. Usage violates the ToS/CoC/etc."

    click_bank()
    sleep(45)

    while(True):
        click_ghouls()
        sleep(5 * 60 - 20 + randint(-2, 2))
        click_bank()
        sleep(45 + randint(-2,2))

main()
