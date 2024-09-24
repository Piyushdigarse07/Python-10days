def format_number(number):
    if number < 0:
        raise ValueError("The number must be non-negative")

    return f"{number:,}"

print(format_number(550000000))
