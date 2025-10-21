# Laborator 1 și 2

# Setarea mediului de lucru (din Anaconda Prompt):
# 1)	ieșire din environment: conda deactivate;
# 2)	creare environment: conda create -p D:/AnacondaEnvs/LaboratoarePython (-p mediul va fi creat exact acolo unde vrem, -n mediul va fi creat în folderul implicit al Anaconda);
# 3)	activare environment: conda activate D:/AnacondaEnvs/LaboratoarePython;
# 4)	intrare în VS code din environment (anaconda prompt): code .;
# 5)	creare folder nou în environment pentru fiecare laborator;
# 6)	dacă vrem să rulăm un fișier Python din linia de comandă (Command Prompt, PowerShell sau terminal) scriem python numeproiect.py;
# 7)	se poate verifica funcționarea mediului Python cu comenzile: python -V, pip -V, conda -V.

# În VS code, cu CTRL + / comentați/decomentați mai multe linii de cod deodată.
# Pentru a deschide un terminal folosește Ctrl + ’.

# Tipuri de variabile în Python:
# •	text type: str;
# •	numeric types: int, float, complex (2 + 3j, 2 partea reală și 3j partea imaginară);
# •	sequence types: list (colecție ordonată și modificabilă de elemente), tuple (colecție ordonată și nemodificabilă de elemente), range (creează o secvență ordonată de numere);
# •	mapping type: dict (key-value pairs);
# •	set types: set (o colecție neordonată și modificabilă de elemente unice), frozenset (ca set dar nemodificabil);
# •	boolean type: bool (true, false);
# •	binary types: bytes, bytearray, memoryview.

# Numele de variabile în Python sunt case sensitive!!!

# VARIABILE

x = 1
y = 2
a = b = 3   # a si b au aceeasi valoare dar au zone de memorie diferite
c, d = 4, 5 # c si d au valori si zone de memorie diferite
print(x, y, a, b, c, d)

x = y = 1
print(x, y)

a, b, c = 1, 10, 100
print(a, b, c)

# Functia type() ne arata ce tipuri de variabile avem

text = "Hello"
x = 5
tip_text = type(text)
tip_x = type(x)
print(tip_text, tip_x)

x = 2; y = 5
xy = "Servus"
print(type(x), type(xy))

# Exercitiile 1 si 2 

x = 3.14
y = "Buna ziua tuturor"
print(type(x), type(y))

# CASTING inseamna conversia unei variabile dintr-un tip de date in altul

x = 5
f_x = float(x) # casting: nume_tip(valoare)
print(f_x)

x = 3.14159
y = int(x)
print(x)
print(y)

x = int(1)
y = int(2.3)
z = float(3)
q = float(3.567)
t = float("2.3") # aici 2.3 este string pentru ca are " "
a = str(2) # aici a devine din int 2 in string "2"
print(x, y, z, q, t, a)

# OPERATORI ARITMETICI 

# + adunare (1 + 3 = 2)
# - scadere (2 - 1 = 1)
# / impartire (1 / 2 = 0) impartirea intre int-uri face impartirea intreaga, adica ia doar partea intreaga a rezultatului exemplu 1 / 2 = 0 chiar daca normal ar fi 0.5
# % rest (15 % 10 = 5)
# * inmultire (1 * 2 = 2)
# // impartire intreaga (converteste rezultatul spre intregul cel mai apropriat: 2.8 // 2.0 = 1.0, rezultatul este 1.4 dar 1.0 este cel mai apropriat intreg)
# ** ridicare la putere (2 ** 2 = 4)

# PRINT

text = "Hello"
text_2 = "world"
print(text, text_2) # print cu spatiu intre valori

text = "Hello"
text_2 = "world"
print(text + text_2) # concatenare, fara spatiu

name = "Alexandra"
age = 21
print(f"My name is {name} and I am {age} years old.") # f-string, util pentru formatare de string, se pune 'f' in fata stringului, tot ce pui intre {} se inlocuieste cu valoarea variabilei sau chiar cu expresii

# ' ' pentru un singur caracter
# " " pentru un sir de caractere
# """ """ pentru afisarea unui paragraf cu mai multe linii 
 
print("""    Numele meu este Alexandra.
          Imi place limbajul Python.""") # textul este afisat exact asa cum este formatat, util in docstrings

# Se pot folosi si liste de variabile in functia print 
string1 = "world"
string2 = '!'
print("Hello", string1, string2)

# in acest caz se poate folosi si operatorul + de concatenare a stringurilor
string1 = "world"
string2 = '!'
print("Hello" + ' ' + string1 + string2)

# STRUCTURI DE DATE

lista = [] # lista goala

lista = ['a', 2, 'b', 1]
print(len(lista)) # afiseaza numarul de elemente din lista

lista = ['a', 2, 'b', 1]
print(lista[0]) # afiseaza primul element din lista, elementul de la index-ul 0
print(lista[1]) # afiseaza al doilea element din lista, elementul de la index-ul 1

lista = [0, 'a', 1, 'b', 'c'] # poate avea valori de diverse tipuri
lista.append(2) # adaugarea in lista a elementului 2 la coada, acest gen de operatie nu  este permisa la tuple!
print(lista)

lista = [0, 'a', 1, 'b', 'c']
lista.extend(['c', 3]) # concatenare cu o alta lista, acest gen de operatie nu este permisa la tuple!
print(lista)

lista = [0, 'a', 1, 'b', 'c']
lista.insert(2, "test") # adaugare pe indexul 2 a valorii "test", muta restul valorilor cu un index in plus
print(lista)

lista = [0, 'a', 1, 'b', 'c']
lista.pop(1) # stergere (dupa index) elementul din pozitia 1
print(lista)

lista = [0, 'a', 1, 'b', 'c']
lista.remove('c') # sterge prima aparitie a lui 'c' din lista
print(lista)

# DICTIONARE

dictionar = {} # dictionar gol

dictionar = {'Ion':4, 'Andrei':8, 'Ana': 10}
print(list(dictionar.keys())) # cheile dictionarului. ATENTIE returneaza obiect dict_keys NU lista

dictionar = {'Ion':4, 'Andrei':8, 'Ana':10}
print(dictionar.values())  # valorile dictionarului. ATENTIE returneaza obiect dict_values NU lista

dictionar = {'Ion':4, 'Andrei':8, 'Ana':10}
dictionar['Maria'] = 10 # inserarea se face prin atribuire directa, nu cu append/insert ca la liste
print(dictionar.items()) # perechile cheie-valoare ale dictionarului. ATENTIE returneaza obiect dict_items NU lista

dictionar = {'Ion':4, 'Andrei':8, 'Ana':10}
dictionar['Maria'] = 3 # adaugarea unui element cu o cheie care exista deja in dictionar va inlocui elementul existent, asadar cheile dictionarului trebui esa fie UNICE!
print(dictionar.items())

dictionar= {'Ion':4, 'Andrei':8, 'Ana':10}
dictionar.pop("Ana") # stergerea se face precizand cheia
print(dictionar.items())

dictionar = {0 : "a",
             "b" : 1} # cheie-valoare, atat cheile cat si valorile pot fi de tipuri diferite

interval = range(0, 10) # returneaza obiect de tip range; util pentru iteratii
print(list(interval))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

interval = range(0, 10)
print(interval)

# CONDITII

# IF

x = 12
if x > 10:
    print("Servus")

x = 2
y = 3
if x == 2 and y == 3:
    print("X este 2 si Y este 3") # daca se respecta ambele conditii
if x == 2 or y == 1:
    print("Ori X este egal cu 2 or y este egal cu 1") # daca se respecta una din conditii
if (x == 2 and x > 1) and y == 3: # daca se respecta toate conditiile
    print("\n")
    print("X este 2 si mai mare ca 1 si Y este 3")

# IF-ELSE

x = 12
if x > 10:
    print("Servus")
else:
    print("Salut") 

x = 2
if x > 2: # dupa fiecare identare trebuie sa punem :
    print("X este mai mare ca 2")
elif x == 2: # else if (altfel daca) 
    print("X este egal cu 2")
else:
    print("X este mai mic ca 2")

# FOR

for i in range(5):
    print(i, end = " ")

persoane = ["Mihai", "George", "Maria"] # parcurgem elementele unei liste
for p in persoane:
    print (p, end = " ")

varste = {"Mihai":25, "George":28, "Maria":21} # afisam cheile si valorile dintr-un dictionar
for cheie, valoare in varste.items():
    print(cheie, valoare)

lista_nume = ["Alex", "Maria", "Ana"]
for nume in lista_nume: # for variabila in variabla
    print(nume)

lista_nume = ["Alex", "Maria", "Ana"]
for i, nume in enumerate(lista_nume): # pt index
    print(i, nume)

lista_nume = ["Alex", "Maria", "Ana"]
note = [8, 9, 10]
for nota, nume in zip(note, lista_nume): # parcurgere in acelasi timp a mai multor liste, pana la lista cea mai scurta
    print(nota, nume)

lista_de_liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # parcurgere liste imbricate
for lista in lista_de_liste:
    print(lista)

d = {"Alex" : 8,
     "Maria" : 9,
     "Ana" : 10}

# WHILE

i = 1
while i <= 10:
    print (i ** 2)
    i = i+1
print("Sfarsit de secventa de patrate perfecte")

# BREAK

for i in range(100):
    print(i)
    if i >= 7:
        break

i = 0
while i <= 5:
    i += 1
    if i == 2:
        continue # se continua blocul cu urmatoarea valoare
    if i == 4:
        break # se iese din bloc
    print(i)

# FUNCTII

def f(x, y, z): # forma generala a unei functii
    # instructiuni 
    # return rezultat

# x este argument obligatoriu, y si z sunt optionali iar daca lipsesc vor primi valorile indicate
# daca unele argumente nu sunt obligatorii, li se poate asocia o valoare implicita
def f(x, y = 1, z = None):

def functieArgOptionale(x, y = 5, z = 10):
    return x * y * z
print(functieArgOptionale(100)) # x nu are o valoare implicita asa ca va lua valoarea 100, y si z au o valoarea implicita si va ramane aceea

def functieArgOptionale(x, y = 5, z = 10):
    return x * y * z
print(functieArgOptionale(100, 2)) # y are o valoare implicita dar va lua valoarea 2 pentru ca a fost specificata

def functieArgOptionale(x, y = 5, z = 10):
    return x * y * z
print(functieArgOptionale(100, 2, 3)) # y si z vor lua valorile 2 si 3,  nu valorile implicite

def functieArgOptionale(x, y = 5, z = 10):
    return x * y * z
print(functieArgOptionale(z = 3, x = 5)) # z va lua valoarea 3, x valoarea 5, iar y va lua valoarea implicita adica 5

# variabilele de tip functie au ca valoare corpul unei functii (nu valoarea returnata de functie)
def patrat(x):
    return x * x
a = patrat(10)
print(a)

# a e o variabila normala ce a preluat rezultatul returnat de functie
def dublare(x):
    return x + x
a = dublare(10)
print(a)

def suma(x, y):
    return x + y
print(suma(2, 3))

def adunare(x, y):
    return x + y
print(f"Suma este: {adunare(1, 2)}")

def codpar(x):
    return ord(str(x)) % 2 == 0
print(codpar('A'))

def ridicare_la_putere(baza, exponent = 2): # valoare default
    return baza ** exponent
print(ridicare_la_putere(2))

def ridicare_la_putere(baza, exponent = 2): # valoare default
    return baza ** exponent
print(f"Puterea este: {ridicare_la_putere(2)}")

def ridicare_la_putere(baza, exponent = 2): # valoare default
    return baza ** exponent
print(f"Puterea este: {ridicare_la_putere(2, 3)}")

def ridicare_la_putere(baza, exponent = 2): # valoare default
    return baza ** exponent
print(f"Puterea este: {ridicare_la_putere(baza = 2, exponent = 4)}")

def ridicare_la_putere(baza, exponent = 2): # valoare default
    return baza ** exponent
print(f"Puterea este: {ridicare_la_putere(exponent = 2, baza = 4)}")

def afisare_text(nume : str, specializare : str = None, an : int = None) -> str: 
    
    # """Afiseaza numele si, daca exista, specializarea si anul

    # Args:
    #     nume (str): Numele studentului.
    #     specializare (str, optional): Specializarea studentului. Defaults to None.
    #     an (int, optional): Anul de studii. Defaults to None.

    # Returns:
    #     str: Un text
    # """

def afisare_text(nume : str, specializare : str = None, an : int = None) -> str: 
    text_de_afisat = f"Student: {nume}, {specializare}" if specializare else f"Student: {nume}" # shorthand if - value_if_true if condition else value_if_false
    text_de_afisat += f", {an}" if an else ""
    return text_de_afisat
print(afisare_text("Alex"))

def afisare_text(nume : str, specializare : str = None, an : int = None) -> str: 
    text_de_afisat = f"Student: {nume}, {specializare}" if specializare else f"Student: {nume}" # shorthand if - value_if_true if condition else value_if_false
    text_de_afisat += f", {an}" if an else ""
    return text_de_afisat
print(afisare_text("Alex", "IE"))

def afisare_text(nume : str, specializare : str = None, an : int = None) -> str: 
    text_de_afisat = f"Student: {nume}, {specializare}" if specializare else f"Student: {nume}" # shorthand if - value_if_true if condition else value_if_false
    text_de_afisat += f", {an}" if an else ""
    return text_de_afisat
print(afisare_text("Alex", "IE", 3))

# CLASE

# crearea unei clase 

class Dog:

    breed = "Saint Bernard"
    owner = "Dinu Alexandra"
    color = "black and white"
    age = 12

myDog = Dog()
print(myDog.breed)
print(myDog.owner)
print(myDog.color)
print(myDog.age)

# self este o referinta la obiectul curent
# practic, spune: „proprietatile si metodele pe care le definesc aici apartin acestui obiect”
# fara self, Python nu stie ca age si name sunt atribute ale obiectului, si nu simple variabile locale

class Dog:

    def __init__(self, age, name): #constructor (functia __init__ este apelata de fiecare data cand un obiect este instantiat)
      self.age = age #proprietate
      self.name = name #proprietate

myDog = Dog(12, "Sasha") # creeaza obiect 
print(myDog.age) # acceseaza proprietatea
print(myDog.name) # acceseaza proprietatea

# un obiect poate avea, de asemenea, mai multe functii (functiile se numesc metode sau actiuni pentru un anumit obiect)

class Dog:

    def __init__ (self, age, name):
        self.age = age
        self.name = name
    
    def bark(self):
        print(self.name + ' ' + "latra!")

    def run(self):
        print(self.name + ' ' + "alearga.")

    def showAge(self):
        print(self.name + ' ' + "are 5 ani.")

myDog = Dog(5, "Sasha")
myDog.bark()
myDog.run()
myDog.showAge()

# MOSTENIREA

# clasa parinte (base class/parent class)

class Animal:

    def __init__ (self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
    
    def printname(self):
        print(self.age, self.weight, self.name)

doggo = Animal(4, 6, "Archie")
doggo.printname()

# clasa copil (clasa derivata)

class Dog(Animal):
    def __init__ (self, age, weight, name, tail):
        Animal.__init__(self, age, weight, name)
        self.tail = tail
        
    def bark(self):
        print(self.name + ' ' + "latra acum!")

myDog = Dog(4, 6, "Archie", "short tail")
print(myDog.age)
print(myDog.weight)
myDog.bark()

# Summary:

# _single_underscore → "internal use" by convention

# __double_leading_underscore → name mangling, “private-like”

# __dunder__ → special methods (never private)

# Exercitiile de la finalul laboratorului 1

# 1. definiti un sir cu numele anotimpurilor, parcurgeti-le in bucla si imprimati fiecare sezon
anotimpuri = ["primavara", "vara", "toamna", "iarna"]
for sezon in anotimpuri:
    print(sezon)

# 2. definiti un string numit Mos Craciun vine in curand!, imprimati fiecare litera din acel string
text = "Mos Craciun vine in curand!"
for litera in text:
    print(litera)

# 3. scrieti un program python pentru a imprima patratul tuturor numerelor impare de la 0 la 10
for numar in range(0, 11):  # 0 pana la 10 inclusiv
    if numar % 2 != 0:      # verificam daca numarul e impar
        print(numar ** 2)   # printam patratul

# 4. scrieti un program python pentru a imprima patratul tutror numerelor care sunt divzibile cu 5 de la 0 la 100
for numar in range(0, 101): # 0 pana la 100 inclusiv
    if numar % 5 == 0:      # verificam daca numarul este divizibil cu 5
        print(numar ** 2)   #printam patratul

# 5. scrieti un program python pentru a imprima primul numar divizibil cu 15 de la 0 la 250 
for numar in range(20, 251): # de la 20 la 250 inclusiv 
    if numar % 15 == 0:      # verificam daca numarul este divizibil cu 15
        print(numar)         # printam primul numar care este divizibil cu 15
        break                # dupa printarea primului numar care este divizibil cu 15 se opreste 
  
# 6. creati doua functii pentru calcul maxim si minim intre 2 numere
def maxim(a, b):
    if a > b:
        return a
    else:
        return b

def minim(a, b):
    if a < b:
        return a
    else:
        return b
    
a = 10
b = 25

print("Maximul este:", maxim(a, b))
print("Minimul este:", minim(a, b))

# 7. functia create numita get_students care trimita o lista de 5 studenti ca argument si ii tipareste
def get_students(students):
    for student in students:
        print(student)

lista_studenti = ["Andreea", "Alexandra", "Oana", "Diana", "Simona"]
get_students(lista_studenti)

# Exercitii laborator 2 

# 1. creati o clasa numita Student, adaugati 2 proprietati pentru student si faceti 2 instante ale clasei Student
class Student:
    def __init__ (self, specializare, an):
        self.specializare = specializare
        self.an = an

stud = Student("IE", 3)
print(stud.specializare)
print(stud.an)

# 2. creati o clasa numita Car, adaugati 3 proprietati pentru aceasta clasa si faceti 2 instante ale clasei Car
class Car:
    def __init__ (self, marca, culoare, an):
        self.marca = marca # atribut
        self.culoare = culoare # atribut
        self.an = an # atribut

    def moveForward(self): # metoda
        print("Masina merge in fata!")

    def moveLeft(self): # metoda 
        print("Masina a virat la stanga!")

    def moveRight(self): # metoda
        print("Masina a virat la dreapta!")

    def moveDown(self): # metoda
        print("Masina da in marsarier!")

myCar1 = Car("BMW", "black", 2021) #instanta
myCar2 = Car("Audi", "white", 2020) #instanta
print(myCar1.marca, myCar1.culoare, myCar1.an) # accesarea atributelor instantelor
myCar1.moveForward()
print(myCar2.marca, myCar2.culoare, myCar2.an)
myCar2.moveLeft()

# 3. creati o clasa parinte numita SportPlayer cu urmatoarele proprietat: varsta, greutate, inaltime si o metoda de showName
class SportPlayer: 
    def __init__ (self, name, age, weight, height):
        self.name = name
        self.age = age # atribute
        self.weight = weight
        self.height = height

    def showName(self): # metode
        print("Sportivul se numeste:", self.name + '.')

SportPlayer1 = SportPlayer("Dinu Alexandra", 21, 41, 1.67) #instante
SportPlayer1.showName() # accesarea atributelor instantelor

# 4. creati o clasa copil numita FotballPlayer mostenind de la SportPlayer cu urmatoarele proprietati: pozitie si cu urmatoarele metode: shot(), pass()
class FootballPlayer(SportPlayer):
    def __init__ (self, name, age, weight, height, position):
        SportPlayer.__init__ (self, name, age, weight, height)
        self.position = position

    def sut(self):
        print(f"{self.name} a sutat la poarta!")

    def pasa(self):
        print(f"{self.name} a pasat mingea altui coleg!")

FootballPlayer1 = FootballPlayer("Hagi", 60, 80, 1.70, "atacant")
FootballPlayer1.sut()       
FootballPlayer2 = FootballPlayer("Ratiu", 25, 60, 1.80, "fundas dreapta")
FootballPlayer2.pasa() 

# 5. extra  adaugati o alta clasa copil pentru SportPlayer numita VolleyballPlayer
class VolleyballPlayer(SportPlayer):
    def __init__ (self, name, age, weight, height, spike_power):
        SportPlayer.__init__ (self, name, age, weight, height)
        self.spike_power = spike_power

VolleyballPlayer1 = VolleyballPlayer("Andreea", 21, 39, 1.58, 50)
print(VolleyballPlayer1.name, VolleyballPlayer1.age, VolleyballPlayer1.weight, VolleyballPlayer1.height, VolleyballPlayer1.spike_power)


# putem folosi super() in loc de SportPlayer.__init__, super().__init__ (este mai modern)


