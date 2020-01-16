# Punjac

#Instrukcije i opis rada sistema implementiranog na Raspberry Pi 3.

Kod je napisan u Pythonu i za GUI je koristen paket GUI Zero - fajl testni.py.
Raspberry Pi 

```
#!/bin/bash
cd /home/pi/go/src/baza_testna
python3 CardReaderGui.py &
unclutter -idle 0.00001 -root &
go run main.go &&
fg
$ 
```

`unclutter -idle 0.00001 -root` makes the mouse pointer disappear after time in seconds written after `-idle`, in this case after 0.00001 seconds.
This is done to make the GUI look cleaner.

`Note: Python app CardReaderGui.py is not going to work if the RFID card reader is not connected to the device.`

To make everything work, as mentioned before, you should firstly modify the paths to your setup.
If the script is located in the same folder as all of the other files, delete the line `cd /home/pi/go/src/baza_testna`.
After you have done that, just run the script with:
```
    $   bash script.sh 
```

[keyboard.py](keyboard.py): App which implements functionality of a keyboard needed for code input in case of workers forgetting their RFID cards.
It also has a minimize/maximize button which switches between kiosk and service mode. After running, GUI opens in kiosk mode. When you press the minimize button, another window opens which asks for login code. This is done for security measures, it prevents everybody else from entering service mode. Code for minimizing is `0000`. Minimize button converts to maximize button after switching to service mode and requires no code when pressed.
It is possible to run the system with this keyboard GUI instead of the first one. It can be run without RFID reader connected because it works only as a keyboard.

To make this setup work just replace `CardReaderGui.py` with `keyboard.py` in `script.sh` and run it like before.

Things to be added:

* Adding a unique RFID code to every person. This can be done after the RFID cards are bought and distributed to the staff.
* Adding a new field which contains codes for keyboard access for every person.
* Creating new GUI which combines functionalities of the two GUIs.
* Adding a control for RFID codes and keyboard codes - if a code is entered or acquired by a reader which cannot be found in a database, do not allow access and write an appropriate message to GUI. Can be tested after both of them are inserted to the database.
