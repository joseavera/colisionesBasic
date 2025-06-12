import pygame
#importar pygame.mixer
import pygame.mixer


# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 500, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con Colisiones")

BLANCO = (255, 255, 255)
#reproducir golpe.wav al colisionar

# Cargar imagen de los personajes
imagen_personaje1 = pygame.image.load("personaje1.png")
imagen_personaje1 = pygame.transform.scale(imagen_personaje1, (50, 50))

imagen_personaje2 = pygame.image.load("personaje2.png")
imagen_personaje2 = pygame.transform.scale(imagen_personaje2, (50, 50))

# Clase para los jugadores
class Jugador:
    def __init__(self, x, y, imagen, controles):
        """Inicializa al jugador con su imagen, posición y controles personalizados."""
        self.x = x
        self.y = y
        self.velocidad = 5
        self.imagen = imagen
        self.controles = controles  # Diccionario con las teclas asignadas

        self.rect = pygame.Rect(self.x, self.y, 50, 50)  # Rectángulo para colisión
        

    def mover(self, teclas):
        """Mueve al jugador según sus teclas asignadas."""
        if teclas[self.controles["izquierda"]] and self.x > 0:
            self.x -= self.velocidad
        if teclas[self.controles["derecha"]] and self.x < ANCHO - 50:
            self.x += self.velocidad
        if teclas[self.controles["arriba"]] and self.y > 0:
            self.y -= self.velocidad
        if teclas[self.controles["abajo"]] and self.y < ALTO - 50:
            self.y += self.velocidad

        # Actualizar el rectángulo de colisión
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, pantalla):
        """Dibuja al jugador en la pantalla."""
        pantalla.blit(self.imagen, (self.x, self.y))

     #definir un metodo que reproduzca golpe.wav al colisionar
    def reproducir_golpe(self):
        pygame.mixer.music.load("golpe.wav")
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.5)
       

# Configuración de jugadores con diferentes controles
jugador1 = Jugador(ANCHO // 4, ALTO // 2, imagen_personaje1, {
    "izquierda": pygame.K_LEFT,
    "derecha": pygame.K_RIGHT,
    "arriba": pygame.K_UP,
    "abajo": pygame.K_DOWN
})

jugador2 = Jugador(3 * ANCHO // 4, ALTO // 2, imagen_personaje2, {
    "izquierda": pygame.K_a,
    "derecha": pygame.K_d,
    "arriba": pygame.K_w,
    "abajo": pygame.K_s
})

def manejar_colisiones(jugador1, jugador2):
    """Verifica si los jugadores colisionan y los empuja en direcciones opuestas."""
    if jugador1.rect.colliderect(jugador2.rect):
        # Determinar dirección del empuje
        if jugador1.x < jugador2.x:  # Jugador 1 está a la izquierda
            jugador1.x -= 5
            jugador2.x += 5
        else:  # Jugador 1 está a la derecha
            jugador1.x += 5
            jugador2.x -= 5

        if jugador1.y < jugador2.y:  # Jugador 1 está arriba
            jugador1.y -= 5
            jugador2.y += 5
        else:  # Jugador 1 está abajo
            jugador1.y += 5
            jugador2.y -= 5

        # Actualizar rectángulos después de la colisión
        jugador1.rect.topleft = (jugador1.x, jugador1.y)
        jugador2.rect.topleft = (jugador2.x, jugador2.y)

  
        

# Bucle principal del juego
ejecutando = True
while ejecutando:
    pygame.time.delay(30)  # Control de velocidad del juego

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()
    jugador1.mover(teclas)
    jugador2.mover(teclas)

    # Manejar colisiones
    manejar_colisiones(jugador1, jugador2)
    #reproducir golpe.wav al colisionar
    if jugador1.rect.colliderect(jugador2.rect):
        jugador1.reproducir_golpe()
        jugador2.reproducir_golpe()
        #reproducir golpe.wav al colisionar

    

    # Dibujar elementos en pantalla
    pantalla.fill(BLANCO)  # Limpiar pantalla


    jugador1.dibujar(pantalla)
    jugador2.dibujar(pantalla)
    pygame.display.update()  # Actualizar pantalla

# Cerrar Pygame
pygame.quit()


