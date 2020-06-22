
print("¡Hola, bienvenido a AlBuNuFi v2.0!")
print("Acciones disponibles:")
print("Para imprimir una cantidad precisa de términos, escribre A y presiona ENTER")
print("Para imprimir un término determinado, escribe B y presiona ENTER")
eleccion = input("¿Qué desea hacer? ")
if eleccion == "A":
	num = int(input("¿Cuántos números de la secuencia deseas obtener? "))
	n1 = 0
	n2 = 1
	print(n1)
	print(n2)
	for i in range(num):
		n3 = n1 + n2
		print(n3)
		n1 = n2
		n2 = n3

elif eleccion == "B":
	det = int(input("¿Qué término desea obtener? "))
	fib = [0, 1]
	n1 = 0
	n2 = 1
	for i in range(det-1):
		n3 = n1 + n2
		fib.append(n3)
		n1 = n2
		n2 = n3
	print("El valor del término " + str(det) + " es igual a: " + str(fib[det-1]))
