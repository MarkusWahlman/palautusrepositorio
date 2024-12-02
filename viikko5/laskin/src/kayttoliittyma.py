from abc import abstractmethod
from enum import Enum
from tkinter import ttk, constants, StringVar


class CommandType(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Command:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._lue_syote = lue_syote
        self._sovelluslogiikka = sovelluslogiikka

    @abstractmethod
    def suorita(self):
        pass

class Summa(Command):
    def suorita(self):
        try:
            arvo = int(self._lue_syote())
            self._sovelluslogiikka.plus(arvo)
        except Exception:
            pass

class Erotus(Command):
    def suorita(self):
        try:
            arvo = int(self._lue_syote())
            self._sovelluslogiikka.miinus(arvo)
        except Exception:
            pass

class Nollaus(Command):
    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa(Command):
    def suorita(self):
        self._sovelluslogiikka.kumoa()

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            CommandType.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            CommandType.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            CommandType.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            CommandType.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote) # ei ehkä tarvita täällä...
        }

    def _lue_syote(self):
        return self._syote_kentta.get()

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(CommandType.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(CommandType.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(CommandType.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(CommandType.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()

        if self._sovelluslogiikka.edelliset_arvot_pituus() > 1:
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            self._kumoa_painike["state"] = constants.DISABLED

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())