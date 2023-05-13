import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), 'No string input provided') # test when null is given as input.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given as input.
               

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), 'No string input provided') # test when null is given as input.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input.
        
        
unittest.main()