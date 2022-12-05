def f(boole):
    if boole > 3:
        return(f(boole-3)+3)
    if boole == 3:
        return((2*boole)+1)
    if boole < 3:
        return(boole*boole + 2)

out = f(f(f(f(f(4)))))
print(out)