def reverse_string(s: str) -> str:
    return s[::-1]

text = input("Введіть рядок: ")
print("Обернений рядок:", reverse_string(text))