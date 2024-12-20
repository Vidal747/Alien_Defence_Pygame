import pygame
import sys
import random
import time

# Iniciación de Pygame
pygame.init()

# Pantalla - ventana
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Alien_Defence')
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
left_bullet = pygame.image.load('imagenes/principal/left_bullet.png')

# Imagenes de los alien
alien_imgs = [
    pygame.image.load('imagenes/principal/alien_1.png'),  # Alien para nivel 1
    pygame.image.load('imagenes/principal/alien_2.png'),  # Alien para nivel 2
    pygame.image.load('imagenes/principal/alien_3.png')   # Alien para nivel 3
]
# Variables iniciales
x = 0
px = 50
py = 200
ancho = 40
alto = 110  # altura del personaje
bullet_right_width = 300 # Ajuste de la posición de la bala
bullet_left_width = 40 # Ajuste de la posición de la bala
velocidad = 10
reloj = pygame.time.Clock()# Control de FPS
salto = False# Variables salto
cuentaSalto = 10
izquierda = False# Variables dirección
derecha = False
eliminaciones = 0  # Contador de eliminaciones
cuentaPasos = 0# Pasos
balas = []# Lista de balas
enemigos = []# Lista de enemigos
niveles = [# Niveles
    {'velocidad_enemigos': 5, 'frecuencia_enemigos': 4},  # Nivel 1
    {'velocidad_enemigos': 7, 'frecuencia_enemigos': 3},  # Nivel 2
    {'velocidad_enemigos': 10, 'frecuencia_enemigos': 2}  # Nivel 3
]
nivel_actual = 0
kills_por_nivel = 10

# Función para recargar la pantalla y dibujar elementos
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

    # Movimiento del jugador
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
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

    # Mostrar eliminaciones
    fuente = pygame.font.SysFont('Arial', 30)
    texto_eliminaciones = fuente.render(f'Eliminaciones: {eliminaciones}', True, (255, 255, 255))
    PANTALLA.blit(texto_eliminaciones, (10, 10))  # Mostrar en la esquina superior izquierda
    
    # Mostrar nivel actual
    texto_nivel = fuente.render(f'Nivel: {nivel_actual + 1}', True, (255, 255, 255))
    PANTALLA.blit(texto_nivel, (10, 50))

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
    if time.time() - ultimo_enemigo >= niveles[nivel_actual]['frecuencia_enemigos']:
        ultimo_enemigo = time.time()
        y_pos = random.randint(100, H - 80)
        enemigos.append(Enemigo(W, y_pos, niveles[nivel_actual]['velocidad_enemigos']))
# Clase de enemigos
class Enemigo:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.ancho = 40
        self.alto = 40
        self.velocidad = velocidad

    def mover(self):
        self.x -= self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(alien_imgs[nivel_actual], (self.x, self.y))

# Función para mostrar el menú inicial
def mostrar_menu_inicial():
    # Colores llamativos
    color_fondo = (0, 0, 0)  # Fondo negro
    color_texto = (255, 255, 255)  # Blanco
    color_destacado = (255, 69, 0)  # Rojo anaranjado para el título

    # Cargar fuente
    fuente_titulo = pygame.font.SysFont('Arial', 80, bold=True)
    fuente_opciones = pygame.font.SysFont('Arial', 40)

    # Renderizar textos
    texto_titulo = fuente_titulo.render('Alien Defence', True, color_destacado)
    texto_inicio = fuente_opciones.render('Presiona G para empezar', True, color_texto)
    texto_salir = fuente_opciones.render('Presiona H para salir', True, color_texto)

    # Fondo animado o interesante
    PANTALLA.fill(color_fondo)
    
    # Centrado del título
    PANTALLA.blit(texto_titulo, (W // 2 - texto_titulo.get_width() // 2, H // 4))

    # Centrado de las opciones
    PANTALLA.blit(texto_inicio, (W // 2 - texto_inicio.get_width() // 2, H // 2))
    PANTALLA.blit(texto_salir, (W // 2 - texto_salir.get_width() // 2, H // 1.5))

    # Efectos adicionales (desvanecimiento o parpadeo)
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
    global eliminaciones  

    # Verificar si la bala está completamente dentro del área del enemigo
    if (bala['x'] + bala['image'].get_width() > enemigo.x and
        bala['x'] < enemigo.x + enemigo.ancho and
        bala['y'] + bala['image'].get_height() > enemigo.y and
        bala['y'] < enemigo.y + enemigo.alto):
         eliminaciones += 1  # Incrementar el contador de eliminaciones
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

def cambiar_nivel():
    global nivel_actual
    if eliminaciones >= (nivel_actual + 1) * kills_por_nivel and nivel_actual < 2:
        nivel_actual += 1
        print(f"¡Nivel {nivel_actual + 1}!")

# Función para mostrar el menú de reiniciar o salir
def mostrar_menu():
    color_fondo = (0, 0, 0)
    color_texto = (255, 255, 255)
    color_destacado = (255, 0, 0) 
    color_oscuro = (50, 50, 50)

    # Cargar fuente
    fuente_titulo = pygame.font.SysFont('Arial', 80, bold=True)
    fuente_opciones = pygame.font.SysFont('Arial', 40)

    # Renderizar textos
    texto_titulo = fuente_titulo.render('¡Has perdido!', True, color_destacado)
    texto_opciones = fuente_opciones.render('Presiona R para reiniciar o Q para salir', True, color_texto)

    # Fondo animado o interesante
    PANTALLA.fill(color_oscuro)
    
    # Centrado del título
    PANTALLA.blit(texto_titulo, (W // 2 - texto_titulo.get_width() // 2, H // 3))

    # Centrado de las opciones
    PANTALLA.blit(texto_opciones, (W // 2 - texto_opciones.get_width() // 2, H // 2))

    # Efectos de animación o transición (ej. sombra o parpadeo en el texto)
    pygame.display.update()

    # Bucle de espera para que el jugador presione una tecla
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reiniciar el juego
                    return True
                if event.key == pygame.K_q:  # Salir del juego
                    pygame.quit()
                    sys.exit()

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
            eliminaciones = 0
            nivel_actual = 0
            enemigos.clear()
            balas.clear()

   # Cambiar de nivel
    cambiar_nivel()

    # Actualización de la ventana
    pygame.display.update()
    # Llamada a la función de actualización de la ventana
    recargaPantalla()

# Salida del juego
pygame.quit()
