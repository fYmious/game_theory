def f(s, c, m):
    if s >= 129:
        return c % 2 == m % 2
    if c == m:
        return False
    h = (f(s + 1, c + 1, m), f(s * 2, c + 1, m))
    if (c + 1) % 2 == m % 2:
        return any(h)
    else:
        return all(h)


for s in range(1, 129):
    for m in range(1, 10):
        if f(s, 0, m):
            print(s, m)
            break
