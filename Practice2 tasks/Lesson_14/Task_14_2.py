def notify(username):
    print("To:", username)
    print(username, ", ваш пароль слишком простой, смените его.", sep="")


etc_passwd = {}
while True:
    line = input()
    if line == "":
        break

    count = 0
    name = ""
    password = ""
    for char in line:
        if char == ":":
            count += 1
        elif char == ",":
            break
        else:
            if count == 1:
                password += char
            elif count == 4:
                name += char
    etc_passwd[name] = password

frequent_passwords = input()
frequents = []
password = ""
for fp in frequent_passwords:
    if fp != ";":
        password += fp
    else:
        frequents.append(password)
        password = ""

for fp in frequents:
    for key in etc_passwd.keys():
        if fp == etc_passwd.get(key):
            notify(key)
