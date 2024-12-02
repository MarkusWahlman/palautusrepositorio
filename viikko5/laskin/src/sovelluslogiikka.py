class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset_arvot = [arvo]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._edelliset_arvot.append(self._arvo)

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._edelliset_arvot.append(self._arvo)

    def nollaa(self):
        self._arvo = 0
        self._edelliset_arvot.append(self._arvo)

    def kumoa(self):
        if len(self._edelliset_arvot) < 2:
            return
        self._arvo = self._edelliset_arvot[-2]
        self._edelliset_arvot.pop()

    def edelliset_arvot_pituus(self):
        return len(self._edelliset_arvot)

    def arvo(self):
        return self._arvo
