def parse_string(encoded_str):
    parts = encoded_str.split('0')
    filtered_parts = [part for part in parts if part]

    first_name = filtered_parts[0]
    last_name = filtered_parts[1]
    id = filtered_parts[2]

    return {"first_name": first_name, "last_name": last_name, "id": id}


encoded_str = "John000Doe000123"
result = parse_string(encoded_str)
print(result)
