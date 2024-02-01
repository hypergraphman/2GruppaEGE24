for n in range(28, 31):
    w = '@' * n + '$' * n + '/' * n

    while '@$' in w or '/@' in w or '/$' in w:
        if '@$' in w:
            w = w.replace('@$', '$@', 1)
        if '/@' in w:
            w = w.replace('/@', '@/', 1)
        if '/$' in w:
            w = w.replace('/$', '$/', 1)
    print(w[29], len(w))