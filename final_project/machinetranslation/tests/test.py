import unittest

from sqlalchemy import null

from translator import english_to_french, french_to_english

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('apple').lower(),'pomme') # test when apple is translated to pomme.

    def test2(self): 
        self.assertEqual(english_to_french('car').lower(),'voiture') # test when car is translated to voiture.

    def test3(self): 
        self.assertEqual(french_to_english('vélo').lower(),'bike') # test when vélo is translated to bike.

    def test4(self): 
        self.assertEqual(french_to_english('banane').lower(),'banana') # test when banane is translated to banana.

    def test5(self): 
        self.assertEqual(english_to_french(null).lower(),'') # test null.

    def test6(self): 
        self.assertEqual(french_to_english(null).lower(),'') # test null.

    def test7(self): 
        self.assertEqual(english_to_french("Hello".lower()).lower(),'Bonjour'.lower()) # test Hello.

    def test8(self): 
        self.assertEqual(french_to_english('Bonjour'.lower()).lower(),'Hello'.lower()) # test Bonjour.


unittest.main()