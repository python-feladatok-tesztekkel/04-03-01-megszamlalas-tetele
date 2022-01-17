from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import megszamol

class TestOsszeg(TestCase):
    def test_feladat01(self):
        aktualis = megszamol.feladat01()
        elvart = 8
        self.assertEqual(elvart, aktualis, "Az ötösök számát nem jól határozta meg!")