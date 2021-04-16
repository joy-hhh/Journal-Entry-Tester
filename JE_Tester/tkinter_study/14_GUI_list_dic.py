persons = ["홍길동", "슈퍼맨", "헐크"]
phones = ["010-0000-0000", "010-1111-1111","010-2222-2222"]

phone_books = {"홍길동":"010-0000-0000", "슈퍼맨":"010-1111-1111", "헐크":"010-2222-2222"}


print(phone_books)

print(phone_books["홍길동"])
print(phone_books.keys())

for key in sorted(phone_books.keys()):
    print(key, phone_books[key])

    
