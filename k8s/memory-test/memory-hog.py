def allocate_memory():
    # Создаем большой список, который сразу потребляет много памяти
    large_list = [' ' * 10**6] * 2000  # 500 миллионов символов (около 500 МБ)
    print(f"Память используется: {len(large_list) * len(large_list[0]) / 10**6} МБ")
    input("Нажмите Enter, чтобы завершить программу...")

if __name__ == "__main__":
    allocate_memory()
