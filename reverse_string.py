def reverse(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print(reverse("Hello World!")) # prints: !dlroW olleH
