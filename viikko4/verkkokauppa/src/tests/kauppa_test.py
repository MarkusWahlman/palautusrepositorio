import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0
            return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            if tuote_id == 3:
                return Tuote(3, "mehu", 7)
            return None

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_kahden_eri_tuotteen_ostos(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("test2", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("test2", 42, "54321", ANY, 8)

    def test_kahden_saman_tuotteen_ostos(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("test3", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("test3", 42, "11111", ANY, 10)

    def test_loppuneen_tuotteen_ostos(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("test4", "22222")

        self.pankki_mock.tilisiirto.assert_called_with("test4", 42, "22222", ANY, 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("test1", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("test1", 42, "12345", ANY, 5)

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("test2", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("test2", 42, "54321", ANY, 3)

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_tuote_poistuu_korista(self):
        self.kauppa.aloita_asiointi()

        self.kauppa.lisaa_koriin(1) 
        self.varasto_mock.saldo.assert_called_with(1)

        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))

        self.kauppa.tilimaksu("test", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("test", ANY, "12345", ANY, 0)