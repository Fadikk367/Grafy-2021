## Projekt 4

Poniżej znajduje się spis dostępnych operacji wraz z obsługiwanymi dla nich parametrami. Dodatkowo zamieszczone zostały przykładowe wywołania operacji oraz screen shoty wyników.

Do większości zadań pliki można dowolnie edytować i eksperymentować, byleby zgadzały się w nich typy wprowadzanych danych.

Wynikowe reprezentacje grafów można na ten moment obejrzeć za pomocą strony [GraphOnline](graphonline.ru/en/).

### 1. random_digraph

data_source: -f, --file

data_type: --plain

data_destination: -c, --console, -f, --file

Przykład:
```
$ random_digraph --in -f examples/random_digraph.txt --plain --out -c

 0   0   0   0   0   0
 0   0   1   1   0   0
 1   0   0   1   1   0
 0   1   0   0   0   0
 0   1   0   1   0   1
 0   0   1   0   0   0

```

gdzie examples/random_connected.txt zawiera ```6 0.3``` (ilość wierzchołków i prawdopodobieństwo wystąpienia krawędzi), otrzymamy wynik:


### 2. kosaraju

data_source: -f, --file

data_type: --dam, --dcm (literka "d" oznacza reprezentację grafu skierowanego)

data_destination: -c, --console, -f, --file

Przykład 1 (--dcm dla grafu ważonego):
```
$ kosaraju --in -f examples/kosaraju.txt --dcm --out -c

1) 6
2) 3
3) 1
4) 0 2 4
5) 7
6) 5
```

Przykład 2 (--dam dla grafu nieważonego):
```
$ kosaraju --in -f examples/kosaraju2.txt --dam --out -c

1) 3
2) 7
3) 2
4) 0 1 4 5 6 9 10 11
5) 8
```

### 3. random_strongly_connected

data_source: -f, --file

data_type: --plain

data_destination: -c, --console, -f, --file

Przykład:
```
$ random_strongly_connected --in -f examples/random_connected.txt --plain --out -c

 .   8   .   .   .   .   .   .
 .   .   .   .   6   .   5   .
 .   0   .   .   .  -4   .   7
 7   .   9   .   .   7   3   .
 .   .   9  10   .   .   .  -1
 9  -2   .  -4   9   .   .  -4
 .   7   .   .   .  -5   .   7
 7   7   .   .   .   2   .   .

```
gdzie examples/random_connected.txt zawiera ```8 0.4``` (ilość wierzchołków i prawdopodobieństwo wystąpienia krawędzi), otrzymamy wynik:


Otrzymujemy podany losowy silnie spójny digraf.

### 4. bellman_ford

data_source: -f, --file

data_type: --dcm

data_destination: -c, --console, -f, --file

Przykład 1:
```
$ bellman_ford --in -f examples/bellman_ford.txt --dcm --out -c

Tablica odległości:
[0, 0, 0, 4, 7]

Ścieżki:
0: (0)
1: (0) (1)
2: (0) (1) (3) (2)
3: (0) (1) (3)
4: (0) (4)
```

Przykład 2 (dla grafu zawierającego ujemny cykl):
```
$ bellman_ford --in -f examples/bellman_ford2.txt --dcm --out -c

There is a negative weight cycle!
```


### 5. johnson

data_source: -f, --file

data_type: --dcm

data_destination: -c, --console, -f, --file

Przykład 1:
```
$ johnson --in -f examples/bellman_ford.txt --dcm --out -c

 0   0   0   4   7
 6   0   0   4   7
 6   6   0  10  13
 2   2  -4   0   8
16  10  10  14   0
```

Przykład 2 (dla grafu zawierającego ujemny cykl):
```
$ johnson --in -f examples/bellman_ford2.txt --dcm --out -c

There is a negative weight cycle!
```

