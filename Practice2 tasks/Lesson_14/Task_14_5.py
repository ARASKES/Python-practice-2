url = input()
url = url[url.find("?") + 1: len(url):]

get_dictionary = {}
new_key = ""
new_value = ""
is_reading_key = True
for char in url:
    if char == "&":
        get_dictionary[new_key] = new_value
        new_key = ""
        new_value = ""
        is_reading_key = True
        continue
    elif char == "=":
        is_reading_key = False
        continue

    if is_reading_key:
        new_key += char
    else:
        new_value += char
get_dictionary[new_key] = new_value

key = input()
print(get_dictionary.get(key))
