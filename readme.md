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

## Uruchamianie
- `runprog.ps1` - to jest skrypt z WIKAMPa, należy tam ustawić poprawne wywołanie twojego programu
- `runprog_mc.ps1` - skrypt który uruchamia `runprog.ps1` w łącznie 18 instanacjach na raz, dzięki temu przetwarzanie jest nieco szybsze
- `runval.ps1` - waliduje solucje. Solucje muszą znajdować się w folderze `./solutions`. Należy także tam skonfigurować poprawne uruchamianie programu `puzzleval.jar` (z WIKAMPu)(linie 21-24 powinny wszystko wyjaśniać).

## Generowanie wykresów
0. Należy przejść w terminaly do folderu `./chart_generator`. Skrypty w nim się znajdujące wykorzystują pliki oraz tworzą nowe i robią to względem ścieżki na jakiej zostały wywołane. Nie przebywanie w odpowiednim folderze może doprowadzić do nieprawidłowego działania programu i/lub zaśmiecenia folderów
1. Należy przerzucić folder `./statistics` do folderu `./chart_generator`
2. Uruchamiamy dumper wyników poprzez uruchomienie pliku `./chart_generator/dumpy.py` (`py dumpy.py`). Skrypt ten wygeneruje nam plik `data.puzz` który zawiera słownik zawierający wszystkie wyniki. Zmniejsza to 10 krotnie zajmowaną ilość miejsca na dysku (5MB->500KB) oraz przyspiesza ładowanie danych, więc jeżeli chce się powtórzyć generowanie wykresów, nie trzeba się ponownie iterować po plikach.
3. Uruchamiamy generator wykresów poprzez uruchomienie pliku `./chart_generator/main.py`
4. Wykresy generowane są do folderu `./chart_generator/charts`
