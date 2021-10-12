def generate_file(sol_file_name, stats_file_name, length, combination, visited, processed, depth, time):
    """
    length - (liczba całkowita): długość znalezionego rozwiązania - o takiej samej wartości jak w pliku z rozwiązaniem (przy czym gdy program nie znalazł rozwiązania, wartość ta to -1);
    combination - ciąg n liter odpowiadających poszczególnym ruchom wolnego pola w ramach znalezionego rozwiązania
    visited - (liczba całkowita): liczbę stanów odwiedzonych;
    processd - (liczba całkowita): liczbę stanów przetworzonych;
    depth - (liczba całkowita): maksymalną osiągniętą głębokość rekursji;
    time - (liczba rzeczywista z dokładnością do 3 miejsc po przecinku): czas trwania procesu obliczeniowego w milisekundach.
    """
    # generuje plik z rozwiązaniem według opisu w readme.md
    sol_file = open(f'solutions/{sol_file_name}', 'w')

    sol_file.write(length)
    sol_file.write(combination)

    sol_file.close()

    # generuje plik z dodatkowymi statystykami według opisu w readme.md
    stats_file = open(f'statistics/{stats_file_name}', 'w')

    stats_file.write(length)
    stats_file.write(visited)
    stats_file.write(processed)
    stats_file.write(depth)
    stats_file.write(time)

    stats_file.close()

    return
