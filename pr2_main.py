"""
Funciones Lambda
Mario de Leon 19019
Teoria de la Computacion

a)  cero(f,n) 
b)  uno(f,n) 
c)  dos(f,n) 
d)  tres(f,n) 
e)  sucesor(x,f,n) 
f)  suma(a,b,f,n) 
g)  multiplicacion(a,b,f,n) 
h)  potencia(a,b,f,n) 
"""
# Funcion n = 0. No hay necesidad de f.
cero = lambda n: n # 0
# Funcion n = 1
# uno = lambda f, n: f(n)
uno = lambda f: lambda n: f(n) # 0+1
# Funcion n = 2
# dos = lambda f, n: f(f(n))
dos = lambda f: lambda n: f(f(n)) # 0+1+1
# Funcion n = 3
# tres = lambda f, n: f(f(f(n)))
tres = lambda f: lambda n: f(f(f(n))) # 0+1+1+1
# Funcion n = 4
# cuatro = lambda f, n: f(f(f(f(n))))
cuatro = lambda f: lambda n: f(f(f(f(n)))) # 0+1+1+1+1
# Funcion n = 5
# cinco = lambda f, n: f(f(f(f(f(n)))))
cinco = lambda f: lambda n: f(f(f(f(f(n))))) # 0+1+1+1+1+1

##################################################

# Funcion alpha
alpha = lambda n: n+1

# Funcion beta
beta = lambda n: n*2

##################################################

# Funcion sucesor(x,f,n): x (numero lambda), funcion, n (numero). Funcion n+1.
# suc = lambda x, f: lambda n: f(x(f), 0)
suc = lambda x: lambda f: lambda n: f(x(f)(n))
# Funcion suma(a,b,f,n): a (numero lambda 1), b (lambda 2), funcion, n (numero)
# suma = lambda a, b, f: lambda n: f(a(f)b(f), 0)
suma = lambda a: lambda b: lambda f: lambda n: a(f)(b(f)(n))
# Funcion multiplicacion(a,b,f,n): a (numero lambda 1), b (lambda 2), funcion, n (numero)
# En este caso es una suma anidada "a" numero de veces a "b" si es alpha. Si es beta, es una multiplicacion *2 "a" numero de veces a "b".
# mult = lambda a, b, f: lambda n: f(a(b(f))(0))
mult = lambda a: lambda b: lambda f: lambda n: a(b(f))(n)
# Funcion potencia(a,b,f,n): a (numero lambda 1), b (lambda 2), funcion, n (numero)
# En este caso vamos a elevar a "b" con exponente "a".
# pot = lambda a, b, f: a(xs)(f)(0)
pot = lambda a: lambda b: lambda f: lambda n: a(b)(f)(n)

##################################################

# Funciones alpha
objCero = cero(0)
objUno = uno(alpha)(0)
objDos = dos(alpha)(0)
objTres = tres(alpha)(0)
objCuatro = cuatro(alpha)(0)
objCinco = cinco(alpha)(0)
objSuc = suc(uno)(alpha)(0)
objSum = suma(uno)(dos)(alpha)(0)
objMult = mult(dos)(tres)(alpha)(0)
objPot = pot(tres)(dos)(alpha)(0)

# Resultados
print("---------- FUNCIONES LAMBDA ----------")
print("Alpha: n+1")
print("Alpha cero: ", objCero)
print("Alpha uno: ", objUno)
print("Alpha dos: ", objDos)
print("Alpha tres: ", objTres)
print("Alpha cuatro: ", objCuatro)
print("Alpha cinco: ", objCinco)
print("Alpha sucesor de Uno: ", objSuc)
print("Alpha suma de Uno + Dos: ", objSum)
print("Alpha multiplicacion de Dos * Tres: ", objMult)
print("Alpha potencia de Dos ^ Tres: ", objPot)
print("")

##################################################

# Funciones beta
# Me di cuenta que usando n=0, beta da todo 0. Hay que usar otro numero. Por lo tanto, la funcion 0 tendra un 1 como default.
objCero = cero(1)
objUno = uno(beta)(1)
objDos = dos(beta)(1)
objTres = tres(beta)(1)
objCuatro = cuatro(beta)(1)
objCinco = cinco(beta)(1)
objSuc = suc(uno)(beta)(1)
objSum = suma(uno)(dos)(beta)(1)
objMult = mult(dos)(tres)(beta)(1)
objPot = pot(tres)(dos)(beta)(1)

# Resultados
print("Beta: n*2")
print("Beta cero, en realidad uno, ya que no es posible trabajar con cero: ", objCero)
print("Beta uno, en este caso 1*2: ", objUno)
print("Beta dos, 2*2: ", objDos)
print("Beta tres, 4*2: ", objTres)
print("Beta cuatro: ", objCuatro)
print("Beta cinco: ", objCinco)
print("Beta sucesor, es decir Uno (2) * 2: ", objSuc)
print("Beta suma de Uno + Dos, es decir, 2 * 4 debido a que beta es n*2: ", objSum)
print("Beta multiplicacion de Dos * Tres, es decir (4 * 8) * 2: ", objMult)
print("Beta potencia de Dos ^ Tres: ", objPot)