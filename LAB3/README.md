## Projekt 3

Poniżej znajduje się spis dostępnych operacji wraz z obsługiwanymi dla nich parametrami. Dodatkowo zamieszczone zostały przykładowe wywołania operacji oraz screen shoty wyników.

Do większości zadań pliki można dowolnie edytować i eksperymentować, byleby zgadzały się w nich typy wprowadzanych danych.

Wynikowe reprezentacje grafów można na ten moment obejrzeć za pomocą strony [GraphOnline](graphonline.ru/en/).

### 1. random_connected_graph

data_source: -f, --file

data_type: --plain

data_destination: -c, --console, -f, --file

Przykład użycia:
```
$ random_connected_graph --in -f examples/random_connected.txt --plain --out -c

 .   6   .   .   7   .   .  10
 6   .   .   .   6   .   .   6
 .   .   .   6   .   .   4   .
 .   .   6   .   4   .   9   8
 7   6   .   4   .   9   .   4
 .   .   .   .   9   .   .   .
 .   .   4   9   .   .   .  10
10   6   .   8   4   .  10   .

```
gdzie examples/random_connected.txt zawiera ```8 0.4``` (ilość wierzchołków i prawdopodobieństwo wystąpienia krawędzi).


Na potrzeby kolejnych zadań (2-5) wynik można zapisac do pliku w przedstawiony poniżej sposób:
```
random_connected_graph --in -f examples/random_connected.txt --plain --out -f examples/<nazwa>.txt
```

### 2. dijkstra

data_source: -f, --file

data_type: --cm

data_destination: -c, --console, -f, --file

Przykład:
```
$ dijkstra --in -f examples/dijkstra.txt --cm --out -c

d(0) = 0, path: [0]
d(1) = 3, path: [0 - 1]
d(2) = 8, path: [0 - 3 - 2]
d(3) = 2, path: [0 - 3]
d(4) = 3, path: [0 - 3 - 4]
d(5) = 9, path: [0 - 3 - 2 - 5]
d(6) = 17, path: [0 - 3 - 2 - 5 - 6]
d(7) = 7, path: [0 - 1 - 7]
d(8) = 4, path: [0 - 8]

```
Zgodnie z zaproponowanym przykładowym wyjściem programu z pdf, Wypisujemy kolejno: wierzchołek, długość najdłuższej ścieżki oraz path, czyli kolejno wierzchołki, przez które przechodzimy.


### 3. distance_matrix

data_source: -f, --file

data_type: --cm

data_destination: -c, --console, -f, --file

Przykład:
```
$ distance_matrix --in -f examples/dijkstra.txt --cm --out -c

 0   3   8   2   3   9  17   7   4
 3   0   6   5   6   7  15   4   7
 8   6   0   6   7   1   9   2  12
 2   5   6   0   1   7  15   8   6
 3   6   7   1   0   8  16   9   7
 9   7   1   7   8   0   8   3  13
17  15   9  15  16   8   0  11  21
 7   4   2   8   9   3  11   0  11
 4   7  12   6   7  13  21  11   0

```
### 4. center

data_source: -f, --file

data_type: --cm

data_destination: -c, --console, -f, --file

Przykład:
```
$ center --in -f examples/dijkstra.txt --cm --out -c

center node id: 3 with sum of 50
minimax center node id: 7 with minimax distance of 11

```

mamy wypisane centrum grafu ```center node id``` oraz centrum minimax ```minimax center node id```.


### 5. kruskal

data_source: -f, --file

data_type: --cm

data_destination: -c, --console, -f, --file

Przykład:
```
$ kruskal --in -f examples/dijkstra.txt --cm --out -c

 0   3   0   2   0   0   0   0   4
 3   0   0   0   0   0   0   4   0
 0   0   0   0   0   1   0   2   0
 2   0   0   0   1   0   0   0   0
 0   0   0   1   0   0   0   0   0
 0   0   1   0   0   0   8   0   0
 0   0   0   0   0   8   0   0   0
 0   4   2   0   0   0   0   0   0
 4   0   0   0   0   0   0   0   0

```

otrzymujemy minimalne drzewo rozpinające przy pomocy algorytmu Kruskala.


Pomimio przyjęcia konwencji kropek jako sygnału braku krawędzi zdecydowaliśmy się w tym przypadku wypisać zera aby ułatwić wizualizację drzewa w zewnętrznych programach
