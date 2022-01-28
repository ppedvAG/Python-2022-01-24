# Klassen

# Erlauben uns das dartstellen von komplexen Verhältnissen und Objekten

# Verfügen über Attribute (props) und Methoden

# Methoden und Attribute sind immer public
# Private Pros sind in der Konvention mit _ zu kennzeichnen

# Klassen sind Blaupausen für ein Objekt
# Erleichtern das Abkapseln und die logische Struktur des Codes
# Vererbung existiert

# Syntax:
# class-Keyword Namen:
# def __init__ Funktion (Constructor)
from typing import NewType

print(f"{__name__} wurde importiert")

class MyClass():
    # Klassenvariablen werden außerhalb des Constructors definiert
    x = 100

    # __ die doppelten Unterstriche symbolisieren besondere Methoden, wie z.b. den Constructor
    def __init__(self, ersterWertPara: float,
                 zweiterWerPara: float):  # self steht sinnbildlich für die zu erstellende Instanz
        """
        Ich bin ein Test String
        :param ersterWertPara: float
        :param zweiterWerPara: float
        """
        self._ersterWert = ersterWertPara  # Instanzvariable, gilt als protected/private
        self._zweiterWert = zweiterWerPara  # Instanzvariable

    # Die __str__ Methode ist dafür da um das Objekt als String darzustellen
    # region predefined
    def __str__(self):
        return f"ErsterWert: {self._ersterWert}\nZweiter Wert: {self._zweiterWert}"

    @staticmethod
    def __repr__():
        return "Instanz der Klasse MyClass"

    # def __iter__(self):
    #     for attr, value in self.__dict__.items():
    #         if str(value[1]) == "_":
    #             pass
    #         else:
    #             yield attr, value
    # endregion

    @property  # Wird zum getter
    def ersterWert(self):
        print("ersterWert getter wird aufgerufen")
        return self._ersterWert

    @ersterWert.setter
    def ersterWert(self, neuerWert):
        print("ersterWert setter wird aufgerufen")
        if neuerWert > 0:
            self._ersterWert = neuerWert
        else:
            print("Negative Zahlen sind nicht erlaubt.")

    @ersterWert.deleter
    def ersterWert(self):
        print("Deleter wird aufgerufen")
        del self._ersterWert

    @property
    def zweiterWert(self):
        return self._zweiterWert

    @zweiterWert.setter
    def zweiterWert(self, neuerWert):
        self._zweiterWert = neuerWert

    def wertSumme(self):
        return self._ersterWert + self._zweiterWert


# print(mySecondInstance.dritterWert) # Änderung bezieht sich nur auf die Instanz, deshalb kennt mySecondInstance
# das Prop dritter Wert nicht

# Löschen von props

# del myThirdInstance.dritterWert
# print(myThirdInstance.dritterWert)  # Fehler, da der Wert gerade gelöscht wurde

# del myThirdInstance.x # Wirft Fehler, da Klassenvariablen nicht gelöscht werden dürfen
# print(myThirdInstance.x)


# Übung 1:
# Erstelle eine Klasse Lebewesen
# Sie soll über die Eigenschaften alter, gliedmassen, getter und setter
# methode, die alle Eigenschaften als string wiedergibt (__str__)
# methode, die das Lebewesen um ein Jahr altern lässt


# static methods
# Eigener Decorator:
# @staticmethod
# Deklariert Methode zu einer statischen Methode, hat aber paar Einschränkungen
# Darf self, cls nicht enthalten

class Lebewesen:
    def __init__(self, alter: int, gliedmassen: int):
        self._alter = alter
        self._gliedmassen = gliedmassen

    def __str__(self):
        return f"Alter: {self._alter}\nGliedmassen: {self._gliedmassen}"

    @property
    def alter(self):
        return self._alter

    @alter.setter
    def alter(self, newAlter):
        self._alter = newAlter

    @property
    def gliedmassen(self):
        return self._gliedmassen

    @gliedmassen.setter
    def gliedmassen(self, newGliedmassen):
        self._gliedmassen = newGliedmassen

    def altern(self):
        self._alter += 1


# Vererbung in Python

class Hund(Lebewesen):

    def __init__(self, alter, name: str, rasse: str, farbe: str):
        super().__init__(alter, 4)  # super() greift auf Basisklasse zu, greife dann auf constructor zu
        self._name = name
        self._rasse = rasse
        self._farbe = farbe

    def __str__(self):
        return super().__str__() + f"\nName: {self._name}\nRasse: {self._rasse}\nFarbe: {self._farbe}"





# Typing wird auch vererbt, aber Namen der Variablen müssen übereinstimmen


def createDog() -> Hund:
    return Hund(1, "Hund", "Generisch", "Farblos")


TestType = NewType("TestType", int)  # Erstellt neuen Typen TestType der von integer erbt
UserID = NewType("UserId", str)  # Erstellt Typen UserId der von String erbt


# Können dann im Typing verwendet werden
# Eigenen Klassen werden immer als Typ hinterlegt


def createUserId(user: Lebewesen) -> UserID:
    """
    Docstring dienen der Beschreibung einer Funktion/Klasse
    :param user:
    :return:
    """
    return user


# Typing erlaubt es uns auf dei Attribute der Typen zuzugreifen bei Intellisense

class Collie(Hund):

    def __init__(self, alter, name, farbe, geretteteKinder=0):
        super().__init__(alter=alter, name=name, rasse="Collie", farbe=farbe)
        self.geretteteKinder = geretteteKinder

    def retteKind(self):
        print("Kind wurde gerettet.")
        self.geretteteKinder += 1
        print(f"Bisher gerettete Kinder: {self.geretteteKinder}")


# Erstelle eine Klasse Person:
# SIe erbt von der Grundklasse Lebewesen
# Zusätzliche Attribute: Vorname, Nachname, Geschlecht
# Methoden: vorstellen(): Gibt in der Konsole den Vor- und Nachname aus

# Erstelle eine Klasse Mann/Frau:
# Die von der Kasse Person erben und einfach das Geschlecht fix übergeben
# TODO: Module, Lambda

def summe(x,y):
    return x+y

if __name__ == "__main__":
    myInstance = MyClass(150, 200)
# Ändern der Props
    myInstance._zweiterWert = 40  # Setzt das Prop _zweiterWert auf 40
    myInstance.x = 120  # Ändert nur lokal auf Instanz bezogen
    print(myInstance.x)

    mySecondInstance = MyClass(400, 500)
    print(mySecondInstance.x)
    # Klassenvariablen können ohne Instanz aufgerufen werden
    print(MyClass.x)
    print(myInstance.wertSumme())
    print(mySecondInstance.wertSumme())
    print(f"{myInstance!r}")  # !r => repr
    print(myInstance)  # => ruft __str__ Methode auf
    print(f"{myInstance!s}")  # !s => __str__ Methode

    myThirdInstance = MyClass(50, 55.5)
    # print(myThirdInstance.dritterWert)

    # Hinzufügen neuer Props
    lessie = Hund(8, "Lessie", "Collie", "Beige")
    print(lessie)
    myThirdInstance.dritterWert = 90
    print(mySecondInstance.ersterWert)  # ruft Getter auf
    mySecondInstance.ersterWert = 555  # ruft Setter auf
    print(mySecondInstance.ersterWert)  # getter
    mySecondInstance.ersterWert = -500
    print(mySecondInstance.ersterWert)
    lessieZwei = Collie(8, "Lessie Zwei", "Beige")
    lessieZwei.retteKind()
    lessieZwei.retteKind()
    lessieZwei.retteKind()
    hund1 = createDog()
