# Punjac

Instrukcije i opis rada sistema implementiranog na Raspberry Pi 3.

Kod je napisan u Pythonu i za GUI je koristen paket GUI Zero - fajl [testni.py]testni.py.

Koristene komponente:

* Raspberry Pi 3 - CPU
* 16 Relay Module - aktiviranje punjaca
* Touch screen
* VGA <-> HDMI konverter kabal
* 74HC595 Shift registar 
* ULN2003A Darlingtonovi parovi
* Napajanje 5V 40A

Raspberry Pi nema VGA port koji je integrisan u monitoru pa je potreban VGA <-> HDMI konverter da sve radi bez problema. Ovaj koji koristim je u Merkatoru 15ak KM.

Releji rade na 5V i aktiviraju se tako sto se na odgovarajuce pinove dovede 0V, inace je na pinovima napon 5V. Posto Raspberry Pi radi na 3V3, potrebno je malo periferne elektronike da bi se ovaj problem zaobisao. Dodatni problem je sto releji mogu da povuku dosta vecu struju nego sto pinovi Raspberry Pi mogu da obezbijede. Rjesenje je u kombinaciji 74HC595 shift registra i ULN2003A pojacavaca sa Darlingtonovim parovima. Raspberry Pi upise odgovarajucu kombinaciju bita u shift registar koji ih cuva sve dok ne dodje do neke promjene. Posto sam shift registar moze da obezbijedi maksimalnu struju od 70mA, sto nije dovoljno u slucaju da su svi releji aktivirani, potrebno je pojacati te signale i to je postignuto koristenjem ULN2003A integrisanog kola. Elektricna shema je prikazana na slici u folderu.

Princip rada:

* Pocetni ekran - reklame se prikazuju u intervalima od 5 sekundi i pise poruka za klik
* Nakon klika otvara se ekran na kojem se bira zeljeni punjac i postavlja se timer od 30 sekundi za odabir punjaca. Timer sluzi kao sigurnosni mehanizam - ako neko slucajno ili namjerno klikne ekran i ne odabere punjac, nakon isteka timera vrati se na pocetni ekran s reklamama.
* Odabrani punjac je slobodan:
    * Ako je punjac slobodan u tom polju ce pisati samo broj 
    * Nakon klika na to polje se aktivira relej, ispisuje se odgovarajuca poruka i vraca se na pocetni ekran s reklamama.
* Odabrani punjac je zauzet:
    * Ispod broja punjaca ce pisati i vrijeme do kada je punjac zauzet
    * Nakon klika na to polje se ispisuje poruka da je punjac zauzet i da se odabere neki drugi punjac.
* Nakon odabira punjaca on ostaje ukljucen 30 minuta. Nakon isteka tog vremena se relej iskljucuje i brise se vrijeme u odgovarajucem polju

Stvari koje je potrebno dodati:

* Zetonjeru da se moze i skupiti koja marka 
* Reklame koje ce se smjenjivati na pocetnom ekranu
* Urediti dizajn da bude vizuelno ljepse
* Umjesto na breadboard, zalemiti sve komponente na perfboard ili napraviti PCB
* Elektronske brave
* USB portove spojiti sa napajanjem i relejima.
