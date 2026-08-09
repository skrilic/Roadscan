# RoadScan

[**English**](README.md) · **Hrvatski**

RoadScan je naslijeđeni terenski sustav za mobilno kartiranje
radiofrekvencijskoga spektra. U jednom mjernom ciklusu softver pridružuje
položaj vanjskoga GPS prijamnika tragu spektra s analizatora Rohde & Schwarz
FSH6, dodaje sustavsko UTC vrijeme te rezultate sprema kao CSV i PNG.

Sustav je u različitim razdobljima uporabe odradio više stvarnih mjernih
vožnji, uključujući sesije koje su trajale po nekoliko sati. Zatečene
hardverske i sustavske zaobilaznice zato treba promatrati u vremenskom i
operativnom kontekstu u kojem su nastale, a ne kao dokaz da sustav nije bio
funkcionalan.

## Izvorna motivacija

RoadScan je nastao radi indikativne, neovisne terenske provjere koliko stvarna
pokrivenost radijskim i komunikacijskim uslugama odgovara javno deklariranim
podacima i obvezama operatora iz dodijeljenih dozvola. Mjerenja nisu zamišljena
kao konačni regulatorni dokaz ni kao alat za sankcioniranje, nego kao grubi
pregled stanja mreže koji može otkriti područja za detaljniju provjeru te dati
korisne informacije operatorima, regulatoru i korisnicima.

Izmjerena jakost signala nužan je, ali ne i dovoljan uvjet za postizanje
određene kvalitete veze. Ako je u konkretnoj točki i uvjetima mjerenja razina
signala niža od potrebnoga praga, deklarirana kvaliteta ondje nije teoretski
ostvariva. Razina iznad praga potvrđuje samo postojanje osnovnoga RF preduvjeta;
kvaliteta veze, brzina prijenosa, latencija i raspoloživost ovise i o
interferenciji, odnosu signala i šuma, kapacitetu, opterećenju mreže i drugim
čimbenicima.

Zbirni `measlog.csv` služi za naknadnu izradu KML putanje s poveznicama na
pojedinačne spektre.

```text
GPS + FSH6 + INI profil
          │
          v
     mjerni ciklus
          │
          ├── pojedinačni CSV traga
          ├── measlog.csv
          └── PNG spektra
                    │
                    v
               KML izvoz
```

Softver GPS i FSH6 podatke dohvaća sekvencijski; postojeći kod ne jamči
njihovu istodobnost ni zajedničku vremensku sinkronizaciju.

## Razvojne inačice

Repozitorij sadrži nekoliko razvojnih generacija:

- `gpspectrum.py` — izvorni monolitni program za naredbeni redak;
- `roadscan-cli.py` — novija inačica za naredbeni redak;
- `roadscan-gui.py` — Tkinter GUI iznad novijega hardverskog sloja;
- `maplayer.py` i `maplayer-gui.py` — naknadni izvoz `measlog.csv` u KML.

Kod je konačno razvijan za Python 2.7 i Linux. Povijesni rad sa stvarnim
FSH6/GPS sklopom potvrđen je terenskim mjerenjima, ali zatečena revizija nije
ponovno ispitana sa suvremenim Pythonom, današnjim Linuxom ni eventualno
drukčijom inačicom ugrađenoga softvera FSH6. Ovisnosti nisu zaključane niti
potpuno navedene. Skripte za pokretanje predstavljaju povijesno terensko
okruženje, a ne trenutačno reproducibilan postupak instalacije.

## Dokumentacija

Detaljan opis razvojnih grana, modula, mjernoga toka, serijskoga protokola,
formata podataka, vizualizacije i poznatih problematičnih mjesta nalazi se u:

- [Arhitektura i poznata problematična mjesta](docs/arhitektura-i-poznati-problemi.md)

Dokumentacija posebno odvaja potvrđene programske nedostatke, potvrđene
protokolarne zahtjeve FSH6 i ostale povijesne zaobilaznice koje prije izmjene
treba provjeriti snimkom stvarne komunikacije.
