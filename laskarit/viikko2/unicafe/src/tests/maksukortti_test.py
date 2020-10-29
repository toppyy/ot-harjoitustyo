import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    
    def test_kortin_saldo_alussa_oikein(self):
        
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataaminen_kasvattaa_saldoa(self):
        
        self.maksukortti.lataa_rahaa(15)
        self.assertEqual(self.maksukortti.saldo, 25)

    def test_rahaa_ottaminen_toimii(self):
        
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(self.maksukortti.saldo, 6)

    def test_saldo_sailyy_jos_se_ei_riita(self):
        
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldon_palauttaa_oikean_totuusarvon(self):

        totuusarvo = self.maksukortti.ota_rahaa(4)
        self.assertTrue(totuusarvo)

        totuusarvo = self.maksukortti.ota_rahaa(10)
        self.assertFalse(totuusarvo)
