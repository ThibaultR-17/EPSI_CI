import unittest

from personnage import Personnage


class RpgTest(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personnage = Personnage()
        self.assertEqual(10, personnage.get_hp())

    def test_attaquer_retranche_1_hp(self):
        attaquant = Personnage()
        defenseur = Personnage()

        defenseur.recevoir_attaque(attaquant)

        self.assertEqual(9, defenseur.get_hp())

    def test_attaquer_2_fois_retranche_2_hp(self):
        attaquant = Personnage()
        defenseur = Personnage()

        defenseur.recevoir_attaque(attaquant)
        defenseur.recevoir_attaque(attaquant)

        self.assertEqual(8, defenseur.get_hp())

    def test_0_hp_est_mort(self):
        personnage = Personnage()

        for _ in range(0, 10):
            personnage.recevoir_attaque(Personnage())

        self.assertTrue(personnage.est_mort())

    def test_1_hp_pas_mort(self):
        personnage = Personnage()

        for _ in range(0, 9):
            personnage.recevoir_attaque(Personnage())

        self.assertFalse(personnage.est_mort())

if __name__ == '__main__':
    unittest.main()
