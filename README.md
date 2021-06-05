# Grafy-2021

## Projekt 1

LAB1 - [Instrukcja uruchomienia](https://github.com/Fadikk367/Grafy-2021/blob/main/LAB1/README.md)  

## Projekty 2-4

W interakcję z programem wchodzimy za pomocą interfejsu konsolowego. 

Uruchomienie:
```
$ python main.py
```

> Wymagana wersja pythona: 3.8+.

> Brak potrzeby instalowania dodatkowych dependencji.

Ogólna postać komend wygląda następująco:

```
$ <operacja> <args> --in <data_source> <(?)filename> <data type> --out <data_destination>
```
gdzie:

* **operacja** to dostępna funkcja aplikacji (czyli zadanie z projektu)
* **args** argumenty, któe zostaną przekazane bezpośrednio do resolvera (funkcji przyjmującej wczytane dane, wywołującej odpowiednią metodę algorytmu oraz zwracającej rezultat)
* **--in** to flaga, która oznacza rozpoczęcie ciagu argumentów dotyczących wejścia programu
* **data_source** rodzaj wejścia, z którego będą brane dane, mogą to być np:
  * -f/--file => dane wejściowe brane będą z pliku (dla tego wejścia kolejnym oczekiwanym argumentem jest naturalnie ścieżka do konkretnego pliku)
  * -c/--console => dane oczekiwane będą brane z konsoli
* **filename** argument wprowadzany tylko, jeśli źródłem danych jest plik, oznacza naturalnie ścieżkę do pliku z danymi
* **data_type** typ danych wejścowych:
  * --am => macierz sąsiedztwa
  * --im => macierz incydencji
  * --al => lista sąsiedztwa
  * --gseq => ciąg graficzny
  * --plain => dane surowe, nie będą w żaden sposób przetwarzane ani transformowane, w tym przypadku funkcje resolvera odpowiadają za    wyłuskanie z nich informacji
* **--out** flaga oznaczająca jednocześnie koniec parametrów wejścia oraz początek parametrów wyjścia
* **data_destination** rodzaj wyjścia, do którego będą przekierowane dane wyjściowe, mogą to być, analogicznie jak dla data_source:
  * -f/--file => dane wyjściowe zapisane zostaną w pliku (dla tej flagi kolejnym oczekiwanym argumentem jest naturalnie ścieżka z nazwą pliku)
  * -c/--console => rezultat programu wypisany zostanie na konsoli
  * -i/--img => wyjście zaprezentowane zostanie w postaci graficznej (TODO w przyszłości) 


Dodatkowo dostępne są dwie komendy pomocnicze:
* help => listuje dostępne w programie operacje
* exit => kończy działanie programu
* help <nazwa_operacji> => listuje dostępne zródła i typy danych wejściowych oraz możliwości wyjścia dla konkretnej operacji (TODO)


> ### UWAGA
> Nie wszystkie zródła oraz typy danych są dostępne dla wszystkich operacji, dostępność jest uwarunkowana przez opcje wprowadzone w momencie instancjonowania klasy OperationStrategy i definiowana jest przez programistę w oparciu o specyfikę zadania, dostępne reprezentacje danych oraz odpowiednie readery/printery. Dostępne możliwości operacji są wypisane w dokumentacji poszczególnych funkcji w plikach README.md odpowiadających projektów.


LAB2 - [Instrukcja obsługi operacji](https://github.com/Fadikk367/Grafy-2021/blob/main/LAB2/README.md)  
LAB3 - [Instrukcja obsługi operacji](https://github.com/Fadikk367/Grafy-2021/blob/main/LAB3/README.md)  
LAB4 - [Instrukcja obsługi operacji](https://github.com/Fadikk367/Grafy-2021/blob/main/LAB4/README.md)  

Graficzną reprezentację grafów z Projektu 2 można obejrzeć za pomocą aplikacji z Projektu 1.
Graficzną reprezentację grafów z Projektów 3 i 4 na ten moment pokazaliśmy za pomocą strony [GraphOnline](graphonline.ru/en/).
