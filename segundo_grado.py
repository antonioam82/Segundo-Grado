from math import sqrt

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

while True:
    #ESTABLECEMOS LOS VALORES DE "a", "b" y "c".
    a=OK(input("Valor de a: "))
    b=OK(input("Valor de b: "))
    c=OK(input("Valor de c: "))
    try:
        if a!=0:
            x1=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
            x2=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
            if x1==0 and x2==0:
                print("Solución: x=%4.3f"%x1)
            else:
                print("Soluciones: x1=%4.3f y x2=%4.3f"%(x1,x2))
        else: #ecuación de primer grado
            if b!=0:
                x=-c/b
                print("Solución: x=%4.3f" % x)

            else:
                if c!=0:
                    print("La ecuación no tiene solución")
                else:
                    print("La ecuación tiene infinitas soluciones")
    except:
        print("Sin solución: No se pudo realizar la ecuación con los datos introducidos")
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
