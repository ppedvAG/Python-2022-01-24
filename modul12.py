# Tests
# In Python integriertes Testframework

import unittest
from personen import Mensch
# Benötigen eine Test-Klasse, die von TestCase erbt
# Klassen Methoden, die jeweils mit test beginnen
# Methoden müssen eine der assert Funktion enthalten
# Ganz am Ende muss unittest.main() aufgerufen werden

class test_Mensch(unittest.TestCase):
    def test_Instance(self):
        mensch1 = Mensch.Mensch()
        self.assertIsInstance(mensch1, Mensch.Mensch)
        self.assertNotIsInstance(mensch1.alter, str)
        # self.assertIsInstance(mensch1, int)


def addiere(x,y):
    return x + y


class test_addiere(unittest.TestCase):
    def test_Result(self):
        result = addiere(21, 21)
        self.assertEqual(42, result, f"Ergebnisse nicht gleich: {result}")

if __name__ == "__main__":
    unittest.main()
