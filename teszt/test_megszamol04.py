from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import megszamol

class TestOsszeg(TestCase):
    def test_feladat04(self):
        aktualis = megszamol.feladat04()
        elvart = 12
        self.assertEqual(elvart, aktualis, "A kétjegyű számok számát nem jól határozta meg!")
