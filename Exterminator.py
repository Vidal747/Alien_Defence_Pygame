import pygame
import sys
import random
import time

# Iniciación de Pygame
pygame.init()

# Pantalla - ventana
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Exterminator')
icono = pygame.image.load('icon.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('imagenes/fondos/ciudad.png')

# Música de fondo
pygame.mixer.music.load('sonido/intergalactic_odyssey.ogg')
pygame.mixer.music.play(-1)

# Personaje
quieto = pygame.image.load('imagenes/principal/idle1.png')

caminaDerecha = [pygame.image.load('imagenes/principal/run1.png'),
                 pygame.image.load('imagenes/principal/run2.png'),
                 pygame.image.load('imagenes/principal/run3.png'),
                 pygame.image.load('imagenes/principal/run4.png'),
                 pygame.image.load('imagenes/principal/run5.png'),
                 pygame.image.load('imagenes/principal/run6.png')]

caminaIzquierda = [pygame.image.load('imagenes/principal/run1-izq.png'),
                   pygame.image.load('imagenes/principal/run2-izq.png'),
                   pygame.image.load('imagenes/principal/run3-izq.png'),
                   pygame.image.load('imagenes/principal/run4-izq.png'),
                   pygame.image.load('imagenes/principal/run5-izq.png'),
                   pygame.image.load('imagenes/principal/run6-izq.png')]

salta = [pygame.image.load('imagenes/principal/jump1.png'),
         pygame.image.load('imagenes/principal/jump2.png')]

# Imagenes de las balas
bala_img = pygame.image.load('imagenes/principal/bullet.png')
left_bullet = pygame.image.load('imagenes/principal/left_bullet.png')  # Suponiendo que esta es la bala para la izquierda

# Imagen del alien
alien_img = pygame.image.load('imagenes/principal/alien.png')

# Variables iniciales
x = 0
px = 50
py = 200
ancho = 40
alto = 110  # Asignamos la altura del personaje
bullet_right_width = 300
bullet_left_width = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variables salto
salto = False
cuentaSalto = 10

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Lista de balas
balas = []

# Lista de enemigos
enemigos = []

# Movimiento
def recargaPantalla():
    global cuentaPasos
    global x

    # Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    
    # Contador de pasos
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0

    # Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 2:
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

    # Dibujar balas
    for bala in balas:
        PANTALLA.blit(bala['image'], (bala['x'], bala['y']))

    # Dibujar enemigos
    for enemigo in enemigos:
        enemigo.dibujar(PANTALLA)


# Función para disparar
def disparar():
    global balas
    posicion_bala_x = px + (bullet_right_width)  # Ajustamos la posición horizontal de la bala
    if derecha:
        balas.append({'x': posicion_bala_x, 'y': py + (alto), 'image': bala_img, 'direccion': 1})
    elif izquierda:
        balas.append({'x': px + (-bullet_left_width), 'y': py + (alto), 'image': left_bullet, 'direccion': -1})

# Función para generar enemigos
ultimo_enemigo = time.time()

def generar_enemigos():
    global ultimo_enemigo
    if time.time() - ultimo_enemigo >= 4:  # Generar un nuevo enemigo cada 1 segundo
        ultimo_enemigo = time.time()
        y_pos = random.randint(100, H - 80)  # Posición aleatoria en el eje y
        enemigos.append(Enemigo(W, y_pos))  # Añadir un enemigo a la lista

# Clase de enemigos
class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 40
        self.alto = 40
        self.velocidad = 5

    def mover(self):
        self.x -= self.velocidad  # Los enemigos se mueven hacia la izquierda

    def dibujar(self, pantalla):
        pantalla.blit(alien_img, (self.x, self.y))


# Función para mostrar el menú inicial
def mostrar_menu_inicial():
    fuente = pygame.font.SysFont('Arial', 40)
    texto_inicio = fuente.render('Presiona G para empezar', True, (255, 255, 255))
    texto_salir = fuente.render('Presiona H para salir', True, (255, 255, 255))

    # Centrado de los textos en la pantalla
    PANTALLA.blit(texto_inicio, (W // 2 - texto_inicio.get_width() // 2, H // 3))
    PANTALLA.blit(texto_salir, (W // 2 - texto_salir.get_width() // 2, H // 2))

    pygame.display.update()

    # Bucle de espera para que el jugador presione una tecla
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:  # Comenzar el juego
                    return True
                if event.key == pygame.K_h:  # Salir del juego
                    pygame.quit()
                    sys.exit()

# Función para detectar la colisión entre una bala y un enemigo
def detectar_colision(bala, enemigo):
    # Verificar si la bala está completamente dentro del área del enemigo
    if (bala['x'] + bala['image'].get_width() > enemigo.x and  # La parte derecha de la bala está más allá de la parte izquierda del enemigo
        bala['x'] < enemigo.x + enemigo.ancho and  # La parte izquierda de la bala está dentro de la parte derecha del enemigo
        bala['y'] + bala['image'].get_height() > enemigo.y and  # La parte inferior de la bala está más allá de la parte superior del enemigo
        bala['y'] < enemigo.y + enemigo.alto):  # La parte superior de la bala está dentro de la parte inferior del enemigo
        return True
    return False


# Función para detectar la colisión entre el jugador y un enemigo
def detectar_colision_jugador():
    for enemigo in enemigos:
        if (px + ancho > enemigo.x and
            px < enemigo.x + enemigo.ancho and
            py + alto > enemigo.y and
            py < enemigo.y + enemigo.alto):
            return True
    return False


# Función para mostrar el menú de reiniciar o salir
def mostrar_menu():
    fuente = pygame.font.SysFont('Arial', 40)
    texto = fuente.render('¡Has perdido! Presiona R para reiniciar o Q para salir', True, (255, 255, 255))
    PANTALLA.blit(texto, (W // 2 - texto.get_width() // 2, H // 2 - texto.get_height() // 2))
    pygame.display.update()

    # Bucle para esperar una opción
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reiniciar
                    return True
                if event.key == pygame.K_q:  # Salir
                    pygame.quit()
                    sys.exit()

# Bucle de acciones y controles
ejecuta = True

# Mostrar el menú inicial antes de iniciar el juego
if mostrar_menu_inicial():
    iniciar_juego = True

while ejecuta:
    # FPS
    reloj.tick(18)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # Opción tecla pulsada
    keys = pygame.key.get_pressed()

    # Tecla A - Movimiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    # Tecla D - Movimiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    # Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    # Tecla W - Movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    # Tecla S - Movimiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad

    # Tecla SPACE - Salto
    if not salto:
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

    # Tecla F - Disparar
    if keys[pygame.K_f]:
        disparar()

    # Mover balas
    for bala in balas[:]:
        bala['x'] += bala['direccion'] * 15  # Velocidad de la bala

        # Eliminar balas fuera de la pantalla
        if bala['x'] < 0 or bala['x'] > W:
            balas.remove(bala)

        # Verificar la colisión con enemigos
        for enemigo in enemigos[:]:
            if detectar_colision(bala, enemigo):
                enemigos.remove(enemigo)  # Eliminar el enemigo
                balas.remove(bala)        # Eliminar la bala
                break  # Romper el ciclo ya que la bala ha colisionado con un enemigo

    # Mover enemigos
    for enemigo in enemigos:
        enemigo.mover()

    # Generar nuevos enemigos
    generar_enemigos()

    # Verificar colisión con el jugador
    if detectar_colision_jugador():
        if mostrar_menu():
            # Reiniciar el juego
            px = 50
            py = 200
            enemigos.clear()
            balas.clear()

    # Actualización de la ventana
    pygame.display.update()
    # Llamada a la función de actualización de la ventana
    recargaPantalla()

# Salida del juego
pygame.quit()
