from random import randint


#Posibles movimientos a elegir en el juego 
movimientos = ["Piedra","Papel","Tijera", "Spock","Lagarto"]

class Jugador:
	def __init__(self):
		self.eleccion = "None"
		self.marcadorJugador = 0
		self.marcadorMaquina = 0
		self.ganador = "None"
		self.ronda = 0
	#Este metodo realiza la validación del input
	def obtenerMovimiento(self, eleccion, ejecutar):
		z = 0 #Puede ser un bool?
		if eleccion == "exit":
			ejecutar=False
			return ejecutar
		for x in range(5):
			if eleccion == movimientos[x]:
				z = 1 #Puede ser un bool?
		if z == 0:
				print("¡Movimiento invalido! Ingrese un movimiento: ")
				return ejecutar
		if z == 1:
				self.eleccion = eleccion
				return ejecutar
	#Este metodo arroja el resultado y modifica los atributos de la clase Jugador definidos en el constructor.
	def comprobacion(self, eleccionMaquina):
		if (self.eleccion != "None") and (eleccionMaquina != self.eleccion) :
			self.ronda += 1
			print(f"\nRonda {self.ronda}")
			#Cada posible resultado puede ganar dos veces y perder dos veces contra 4 oponentes 5 x 4 = 20 posibles resultados 
			if self.eleccion == "Piedra" and eleccionMaquina == "Tijera":
				self.marcadorJugador += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} rompe {eleccionMaquina}")
			elif self.eleccion == "Piedra" and eleccionMaquina == "Lagarto":
				self.marcadorJugador += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} aplasta a {eleccionMaquina}")
			elif self.eleccion == "Piedra" and eleccionMaquina == "Papel":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} envuelve a {self.eleccion}")
			elif self.eleccion == "Piedra" and eleccionMaquina == "Spock":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} vaporiza la {self.eleccion}")


			elif self.eleccion == "Papel" and eleccionMaquina == "Piedra":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} envuelve a {eleccionMaquina}")
			elif self.eleccion == "Papel" and eleccionMaquina == "Spock":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} desautoriza a {eleccionMaquina}")
			elif self.eleccion == "Papel" and eleccionMaquina == "Tijera":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} rompe {self.eleccion}")
			elif self.eleccion == "Papel" and eleccionMaquina == "Lagarto":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} se come a {self.eleccion}")

				
			elif self.eleccion == "Tijera" and eleccionMaquina == "Papel":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} rompe {eleccionMaquina}")
			elif self.eleccion == "Tijera" and eleccionMaquina == "Lagarto":
				self.marcadorMaquina += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} decapita al {eleccionMaquina}")
			elif self.eleccion == "Tijera" and eleccionMaquina == "Piedra":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} rompe {self.eleccion}")
			elif self.eleccion == "Tijera" and eleccionMaquina == "Spock":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} rompe {self.eleccion}")


			elif self.eleccion == "Spock" and eleccionMaquina == "Tijera":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} rompe {eleccionMaquina}")
			elif self.eleccion == "Spock" and eleccionMaquina == "Piedra":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} vaporiza {eleccionMaquina}")
			elif self.eleccion == "Spock" and eleccionMaquina == "Papel":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} desautoriza a {self.eleccion}")
			elif self.eleccion == "Spock" and eleccionMaquina == "Lagarto":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} envenena a {self.eleccion}")


			elif self.eleccion == "Lagarto" and eleccionMaquina == "Spock":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} envenena {eleccionMaquina}")
			elif self.eleccion == "Lagarto" and eleccionMaquina == "Papel":
				self.marcadorJugador  += 1
				self.ganador = self.eleccion
				print(f"\n{self.ganador} se come al {eleccionMaquina}")
			elif self.eleccion == "Lagarto" and eleccionMaquina == "Piedra":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} aplasta al {self.eleccion}")
			elif self.eleccion == "Lagarto" and eleccionMaquina == "Tijera":
				self.marcadorMaquina += 1
				self.ganador = eleccionMaquina
				print(f"\n{eleccionMaquina} decapita el {self.eleccion}")

		else:
			self.ganador = "Empate"


				


	#Este metodo retorna la elección del jugador
	def retornarEleccion(self):
		return self.eleccion


	#Este metodo retorna el marcador 
	def retornarMarcador(self):
		return self.marcador


#Se crea la instancia de jugador y se invicializa la variable ejecutar
Jugador = Jugador()
ejecutar =  True

#Loop Principal del juego
while ejecutar:
	ejecutar = Jugador.obtenerMovimiento(input("""\nIngrese su siguiente movimiento o escriba 'exit' para salir: ¡El primero en llegar a 3! 1,2,3...1,2,3...Piedra,Papel,Tijera,Spock o Lagarto: """),ejecutar)
	if ejecutar == True:
		eleccionMaquina = movimientos[randint(0,4)]
		print(f"\nLa eleccion de la maquina es {eleccionMaquina}")
		Jugador.comprobacion(eleccionMaquina)
	print(f"\nGana: {Jugador.ganador}")
	print(f"\nMarcador Jugador:{Jugador.marcadorJugador}")
	print(f"\nMarcador maquina:{Jugador.marcadorMaquina}")

	if Jugador.marcadorJugador == 3:
		ejecutar = False
		print("\n¡Ganador Jugador!")
	elif Jugador.marcadorMaquina == 3:
		ejecutar = False
		print("\n¡Ganador Maquina!")








