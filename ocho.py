cadena = "holasmundos1234"
c = 0
C = 0
for h in cadena:
	if h in '0123456789':
		c += 1
	else:
		C += 1
print "Letras : ", C
print "Numeros : ", c