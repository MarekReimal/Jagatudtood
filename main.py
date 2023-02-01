"""
Rakendus, mis annab etteantud isikutele (õpilastele) juhuslikud ülesanded.
Isikute nimed ja ülesanded on eraldi tekstifailis (näidised on ülesandega kaasa antud).

Funktsionaalsus
1. Rakendus peab olema graafilise kasutajaliidesega (GUI).
2. Rakendus peab olema intuitiivne. Muidu tuleb rakenduse kasutusjuhend juurde kirjutada.
3. Rakenduse loomisel tuleb kasutada Mudel-Vaade-Kontroller (MVC) lahendust.
4. Rakendusel peab olema vähemalt üks oma loodud klass (class), millel nii konstruktor (init)
kui ka vähemalt üks meetod (def).
5. Faili avamisel (nimed ja ülesanded) peavad olema avatavad hiire klikiga mitte koodi
kirjutatud faili nimedega (.askopenfilename()). Mõlema faili jaoks peab olema eraldi nupp!
6. Valitud isikute nimed ja ülesannete nimed peavad peale faili avamist olema nähtavad ka
kasutajale.
7. Isikute ja ülesannete segamist peaks kasutaja saama ise „segada“. Klikkida nupul ja
isiku(te)l on uus ülesanne.
8. Lõpp tulemust võib näidata ekraanil, kuid kindlasti peab kasutaja saama tulemuse
salvestada ka arvutisse endale sobivasse kohta (.asksaveasfile()) tekstifailina (.txt).
Tingimused
1. Kui ülesandeid on vähem, kui isikuid, siis informeeritakse kasutajat ja „segamist“ ei toimu.
2. Kui ülesandeid on rohkem, siis on kõik ülesanded kasutatavad vastavalt isikute arvule.
3. Täpitähed (ä, ö, õ, ü, ž, š, Ä, Ö, Õ, Ü, Ž, Š jne) peavad kõikjal toimima.
4. Mis juhtub kui avatavad fail(id) on tühjad või neid pole valitud. Informeeritakse kasutajat
või soovitatakse lahendust.
5. Rakenduse töötamise ajal ei tohi õpetaja konsoolis midagi näha.

"""
from Controller import Controller


class Sharedtasks:

    def __init__(self):
        Controller().main()


if __name__ == '__main__':
    Sharedtasks()