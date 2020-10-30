

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestiKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

        self.edullisen_hinta = 240
        self.maukkaan_hinta  = 400



    def test_kassapaatteet_saldot_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 )
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)


    def test_oikeat_vaihtorahat(self):

        edullinenVaihtoraha = self.kassapaate.syo_edullisesti_kateisella( self.edullisen_hinta + 10 )
        maukasVaihtoraha    = self.kassapaate.syo_maukkaasti_kateisella(  self.maukkaan_hinta + 100)
   
        self.assertEqual( edullinenVaihtoraha , 10  )
        self.assertEqual( maukasVaihtoraha    , 100 )


    def test_lounaiden_maara_kasvaa_oikein(self):

        self.kassapaate.syo_edullisesti_kateisella(self.edullisen_hinta)
        self.kassapaate.syo_edullisesti_kateisella(self.edullisen_hinta)
        self.kassapaate.syo_maukkaasti_kateisella(self.maukkaan_hinta)

        self.assertEqual( self.kassapaate.edulliset , 2 )
        self.assertEqual( self.kassapaate.maukkaat  , 1 )

    def test_kassa_karttuu_oikein(self):

        rahaa_alussa = self.kassapaate.kassassa_rahaa

        self.kassapaate.syo_edullisesti_kateisella(self.edullisen_hinta)
        self.kassapaate.syo_maukkaasti_kateisella(self.maukkaan_hinta)

        self.assertEqual( self.kassapaate.kassassa_rahaa , rahaa_alussa + self.edullisen_hinta + self.maukkaan_hinta )

    def test_kateisella_ruokailu_toimii(self):


        rahat = self.edullisen_hinta - 1 # Ei riita

        edullinenRiittamaton = self.kassapaate.syo_edullisesti_kateisella(rahat)
        maukasRiittamaton    = self.kassapaate.syo_maukkaasti_kateisella(rahat)

        self.assertEqual( edullinenRiittamaton , rahat  )
        self.assertEqual( maukasRiittamaton    , rahat )


    def test_kortilla_voi_syoda_rahojen_riittaessa(self):

        kortti = Maksukortti( self.maukkaan_hinta + self.edullisen_hinta )

        self.assertTrue( self.kassapaate.syo_edullisesti_kortilla(kortti) )
        self.assertTrue( self.kassapaate.syo_maukkaasti_kortilla(kortti)  )

    def test_kortilla_ei_voi_syoda_ilman_rahaa(self):

        kortti = Maksukortti( 1 )

        self.assertFalse( self.kassapaate.syo_edullisesti_kortilla(kortti) )
        self.assertFalse( self.kassapaate.syo_maukkaasti_kortilla(kortti)  )


    def test_kortilla_syominen_kasvattaa_lounaiden_maaraa(self):

        kortti = Maksukortti( self.maukkaan_hinta * 10 )

        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual( self.kassapaate.edulliset , 2 )
        self.assertEqual( self.kassapaate.maukkaat  , 3 )


    def test_kortilla_syominen_ei_kasvata_saldoa(self):

        rahaa_alussa = self.kassapaate.kassassa_rahaa

        kortti = Maksukortti( self.maukkaan_hinta * 10 )

        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
    
        self.assertEqual( rahaa_alussa, self.kassapaate.kassassa_rahaa)

    def test_rahan_lataus_toimii(self):

        kortti = Maksukortti(650)

        rahaa_alussa = self.kassapaate.kassassa_rahaa

        lisays = 123

        self.kassapaate.lataa_rahaa_kortille(kortti,lisays)
        self.assertEqual( rahaa_alussa + lisays , self.kassapaate.kassassa_rahaa )

        self.kassapaate.lataa_rahaa_kortille(kortti,-1)
        self.assertEqual( rahaa_alussa + lisays , self.kassapaate.kassassa_rahaa )

