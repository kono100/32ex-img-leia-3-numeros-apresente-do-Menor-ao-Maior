
#32. Leia 3 números inteiros, em seguida, apresente-os de forma ordenada (crescente), ou seja,do menor para o maior
a = int(input('Escreva 1° número: '))
b = int(input('Escreva 2° número: '))
c = int(input('Escreva 3° número: '))

if a <= b and a <= c and b <= c:
    print(f'\nA ordem decrescente é {a} , {b} e {c}\n')
elif a <= b and a <=c and c <= b:
    print(f'\nA ordem decrescente é {a} , {c} e {b}\n')
elif b <= a and b <= c and a <= c:
    print(f'\nA ordem decrescente é {b} , {a} e {c}\n')
elif b <= a and b <= c and c <= a:
    print(f'\nA ordem decrescente é {b} , {c} e {a}\n')
elif c <= a and c <= b and a <=b:
    print(f'\nA ordem decrescente é {c} , {a} e {b}\n')
elif c <= a and c <= b and b <= a:
    print(f'\nA ordem decrescente é {c} , {b} e {a}\n')