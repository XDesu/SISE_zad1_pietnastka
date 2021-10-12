# SISE zima 2021
## zadanie 1 - piętnastka

Przygotowany program napisany został w języku **Python** w wersji **3.10**

## Plik z układem początkowym
> Jest to plik tekstowy, w którym liczba linii zależy od rozmiaru ramki. Pierwsza linia zawiera dwie liczby całkowite w oraz k, oddzielone od siebie spacją, które określają odpowiednio pionowy (liczbę wierszy) i poziomy (liczbę kolumn) rozmiar ramki. Każda z pozostałych w linii zawiera k oddzielonych spacjami liczb całkowitych, które opisują położenie poszczególnych elementów układanki, przy czym wartość 0 oznacza wolne pole.

Pliki z układami początkowymi znajdują się w folderze `./puzzles`

## Plik z rozwiązaniem
> Jest to plik tekstowy standardowo składający się z 2 linii. Pierwsza z nich zawiera liczbę całkowitą n, określającą długość znalezionego rozwiązania (czyli długość ciągu ruchów odpowiadających przesunięciom wolnego pola, które przeprowadzą układankę z zadanego układu początkowego do układu wzorcowego). Natomiast w drugiej linii znajduje się ciąg n liter odpowiadających poszczególnym ruchom wolnego pola w ramach znalezionego rozwiązania, zgodnie z reprezentacją przedstawioną w tabeli zamieszczonej wyżej. Jeżeli dla zadanego układu początkowego program nie znalazł rozwiązania, wówczas plik składa się tylko z 1 linii, która zawiera liczbę -1.

Pliki z rozwiązaniami znajdują się w folderze `./solutions`

## Plik z dodatkowymi informacjami
> Jest to plik tekstowy składający się z 5 linii, z których każda zawiera jedną liczbę oznaczającą odpowiednio:
>- 1 linia (liczba całkowita): długość znalezionego rozwiązania - o takiej samej wartości jak w pliku z rozwiązaniem (przy czym gdy program nie znalazł rozwiązania, wartość ta to -1);
>- 2 linia (liczba całkowita): liczbę stanów odwiedzonych;
>- 3 linia (liczba całkowita): liczbę stanów przetworzonych;
>- 4 linia (liczba całkowita): maksymalną osiągniętą głębokość rekursji;
>- 5 linia (liczba rzeczywista z dokładnością do 3 miejsc po przecinku): czas trwania procesu obliczeniowego w milisekundach.

Pliki z dodatkowymi informacjami znajdują się w folderze `./statistics`