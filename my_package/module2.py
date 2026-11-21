import random

def fill_file(filename, count, start=-100, end=100):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(count):
            f.write(str(random.randint(start, end)) + '\n')

def read_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(line.strip()) for line in f if line.strip()]

def remove_duplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

def write_numbers(filename, numbers):
    with open(filename, 'w', encoding='utf-8') as f:
        for num in numbers:
            f.write(str(num) + '\n')

def main():
    f_name = "f.txt"
    g_name = "g.txt"
    count = 30

    fill_file(f_name, count)
    print(f"Файл '{f_name}' заполнен {count} случайными числами.")

    numbers = read_numbers(f_name)
    print(f"\nИсходные числа ({len(numbers)}):")
    print(numbers)

    unique_numbers = remove_duplicates(numbers)
    print(f"\nЧисла без повторов ({len(unique_numbers)}):")
    print(unique_numbers)

    write_numbers(g_name, unique_numbers)
    print(f"\nРезультат записан в файл '{g_name}'.")

    print(f"\nУдалено повторных вхождений: {len(numbers) - len(unique_numbers)}")
if __name__ == "__main__":
    main()
