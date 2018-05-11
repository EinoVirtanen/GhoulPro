bank_x_offset = 3
bank_y_offset = 25
ghouls_x_offset = 90
ghouls_y_offset = 245
canifis_x_offset = 50
canifis_y_offset = 180
xp_per_run = 4751175 - 4746545 
runs = 0

import smtplib
import autopy
from random import uniform, randint
from time import sleep
bank_icon = autopy.bitmap.Bitmap.open("bank_icon.png")
bank_coordinates = []

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
        print "Sleeping for", amount-i, "until", reason
        sleep(1)
    sleep(uniform(0, 1))

def click_bank():
    screenshot = autopy.bitmap.capture_screen()
    bank_coordinates = screenshot.find_every_bitmap(bank_icon)

    if len(bank_coordinates) != 1:
        print "Successful runs", runs, "and about", runs * xp_per_run, "XP gained"
        send_mail()
        quit("Error: " + str(len(bank_coordinates)) + " bank icons detected")

    autopy.mouse.smooth_move(bank_coordinates[0][0] + bank_x_offset + randint(-2, 2),
                             bank_coordinates[0][1] + bank_y_offset + randint(-2, 2))
    wait(2, "clicking bank")
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
    sleep(uniform(0.1, 0.2))
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)

def click_ghouls():
    screenshot = autopy.bitmap.capture_screen()
    global bank_coordinates
    bank_coordinates = screenshot.find_every_bitmap(bank_icon)

    if len(bank_coordinates) != 1:
        print "Successful runs", runs, "and about", runs * xp_per_run, "XP gained"
        send_mail()
        quit("Error: " + str(len(bank_coordinates)) + " bank icons detected")

    autopy.mouse.smooth_move(bank_coordinates[0][0] + ghouls_x_offset + randint(-2, 2),
                             bank_coordinates[0][1] + ghouls_y_offset + randint(-2, 2))
    wait(2, "clicking ghouls")
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
    sleep(uniform(0.1, 0.2))
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)

def click_canifis():
    autopy.mouse.smooth_move(bank_coordinates[0][0] - canifis_x_offset + randint(-2, 2),
                             bank_coordinates[0][1] - canifis_y_offset + randint(-2, 2))
    wait(2, "clicking Canifis")
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
    sleep(uniform(0.1, 0.2))
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)


def main():
    print "Do not use this in Jagex RuneScape. Usage violates the ToS/CoC/etc."

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
