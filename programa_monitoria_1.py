import MYTOOLS as mt

aura = int(input("""Qual váriavel?
      1 - Pi
      2 - Euler\n"""))


if aura == 1:
    n = int(input("Quantas casas após a vírgula? \n"))
    print(mt.pi_real(n))
else:
    if aura == 2:
        n = int(input("Quantas casas após a vírgula? \n"))
        print(mt.e_real(n))
    else:
        print("Esta não é uma opção.")