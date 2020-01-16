# Punjac

Instrukcije i opis rada sistema implementiranog na Raspberry Pi 3.

Kod je napisan u Pythonu i za GUI je koristen paket GUI Zero - fajl testni.py.

Koristene komponente:

*Raspberry Pi 3 - CPU
*16 Relay Module - aktiviranje punjaca
*Touch screen
*VGA <-> HDMI konverter kabal
*74HC595 Shift registar 
*ULN2003A Darlingtonovi parovi
*Napajanje 5V 40A

Raspberry Pi nema VGA port koji je integrisan u monitoru pa je potreban VGA <-> HDMI konverter da sve radi bez problema. Ovaj koji koristim je u Merkatoru 15ak KM.

Releji rade na 5V i aktiviraju se tako sto se na odgovarajuce pinove dovede 0V, inace je na pinovima napon 5V. Posto Raspberry Pi radi na 3V3, potrebno je malo periferne elektronike da bi se ovaj problem zaobisao. Dodatni problem je sto releji mogu da povuku dosta vecu struju nego sto pinovi Raspberry Pi mogu da obezbijede. Rjesenje je u kombinaciji 74HC595 shift registra i ULN2003A pojacavaca sa Darlingtonovim parovima. Raspberry Pi upise odgovarajucu kombinaciju bita u shift registar koji ih cuva sve dok ne dodje do neke promjene. Posto sam shift registar moze da obezbijedi maksimalnu struju od 70mA, sto nije dovoljno u slucaju da su svi releji aktivirni, potrebno je pojacati te signale i to je postignuto koristenjem ULN2003A integrisanog kola. Elektricna shema je prikazana na slici u folderu.



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



To make this setup work just replace `CardReaderGui.py` with `keyboard.py` in `script.sh` and run it like before.

Stvari koje je potrebno dodati:

* Zetonjeru da se moze i skupiti koja marka 
* Reklame koje ce se smjenjivati na pocetnom ekranu
* Urediti dizajn da bude vizuelno ljepse
** Umjesto na breadboard, zalemiti sve komponente na perfboard ili napraviti PCB
