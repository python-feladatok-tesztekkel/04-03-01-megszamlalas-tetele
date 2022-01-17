from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import megszamol

class TestOsszeg(TestCase):
    def test_feladat03(self):
        aktualis = megszamol.feladat03()
        elvart = 9
        self.assertEqual(elvart, aktualis, "Az egyjegyű számok számát nem jól határozta meg!")
