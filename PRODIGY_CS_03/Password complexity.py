import re

def f1(password):
    a = len(password) >= 8
    b = bool(re.search(r'[A-Z]', password))
    c = bool(re.search(r'[a-z]', password))
    d = bool(re.search(r'[0-9]', password))
    e = bool(re.search(r'[\W_]', password))
    f = a + b + c + d + e
    g = []
    if not a:
        g.append("Password should be at least 8 characters long.")
    if not b:
        g.append("Password should include at least one uppercase letter.")
    if not c:
        g.append("Password should include at least one lowercase letter.")
    if not d:
        g.append("Password should include at least one number.")
    if not e:
        g.append("Password should include at least one special character.")
    if f == 5:
        h = "Very Strong"
    elif f == 4:
        h = "Strong"
    elif f == 3:
        h = "Medium"
    elif f == 2:
        h = "Weak"
    else:
        h = "Very Weak"
    return h, g

while True:
    password = input("Enter your password: ")
    h, g = f1(password)
    print(f"Password Strength: {h}")
    if g:
        print("Feedback:")
        for i in g:
            print(f"- {i}")
    if h == "Very Strong":
        break

