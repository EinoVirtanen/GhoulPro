bank_offset = (3, 25)
ghouls_offset = (90, 245)
canifis_offset = (-50, -180)
xp_per_run = 4751175 - 4746545 

import smtplib
import autopy
from random import uniform, randint
from time import sleep

bank_coordinates = (0, 0)
bank_icon = autopy.bitmap.Bitmap.open("bank_icon.png")
runs = 0

def click(coordinates, offset, target):
    coordinates = tuple(map(sum, zip(coordinates, offset)))
    autopy.mouse.smooth_move(coordinates[0] + randint(-2, 2),
                             coordinates[1] + randint(-2, 2))
    wait(2, "clicking " + target)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
    sleep(uniform(0.1, 0.2))
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)

def send_mail():
    file_descriptor = open("credentials.txt", "r")
    file_data = file_descriptor.read().split("\n")
    file_descriptor.close()
    address = file_data[0]
    password = file_data[1]
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.starttls()
    mail_server.login(address, password)
    mail_server.sendmail(address, address, "RS3")
    mail_server.quit()

def wait(amount, reason):
    for i in range(amount):
        for a in range(1000):
            print " "
        print "Sleeping for", amount - i, "until", reason
        sleep(1)
    sleep(uniform(0, 1))


def find_bank():
    screenshot = autopy.bitmap.capture_screen()
    bank_coordinate_list = screenshot.find_every_bitmap(bank_icon)

    if len(bank_coordinate_list) != 1:
        print "Successful runs", runs, "and about", runs * xp_per_run, "XP gained"
        send_mail()
        autopy.bitmap.capture_screen().save("fail.png")
        quit("Error: " + str(len(bank_coordinate_list)) + " bank icons detected")

    global bank_coordinates
    bank_coordinates = (bank_coordinate_list[0][0], bank_coordinate_list[0][1])


def click_bank():
    find_bank()
    click(bank_coordinates, bank_offset, "bank")

def click_ghouls():
    find_bank()
    click(bank_coordinates, ghouls_offset, "ghouls")

def click_canifis():
    click(bank_coordinates, canifis_offset, "Canifis")

def main():

    print "Do not use this in Jagex RuneScape. Usage violates the ToS/CoC/etc."
    sleep(2)

    click_bank()
    wait(30, "clicking ghouls for the first time")

    global runs

    while(True):
        click_ghouls()
        wait(5 * 60 - 30, "clicking Canifis")
        click_canifis()
        wait(30, "clicking bank")
        click_bank()
        wait(10, "clicking ghouls")
        runs = runs + 1

main()
