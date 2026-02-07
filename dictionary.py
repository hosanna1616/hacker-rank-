n = int(input())
phone_book = {}

for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone

while True:
    try:
        name = input()
        print(f"{name}={phone_book[name]}" if name in phone_book else "Not found")
    except:
        break