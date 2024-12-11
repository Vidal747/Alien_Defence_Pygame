import pygame
import sys

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

# Imagen de la bala
bala_img = pygame.image.load('imagenes/principal/bullet.png')

# Variables iniciales
x = 0
px = 50
py = 200
alto = 170
ancho = 40
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

# Función para disparar
def disparar():
    global balas
    # 60% de la altura del jugador
    altura_bala = py + (0.6 * alto)  # Ajustamos la altura de la bala
    if derecha:
        balas.append({'x': px + ancho, 'y': altura_bala, 'image': bala_img, 'direccion': 1})
    elif izquierda:
        balas.append({'x': px, 'y': altura_bala, 'image': bala_img, 'direccion': -1})

# Bucle de acciones y controles
ejecuta = True
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
    for bala in balas:
        bala['x'] += bala['direccion'] * 15  # Velocidad de la bala

    # Eliminar balas fuera de la pantalla
    balas = [bala for bala in balas if 0 <= bala['x'] <= W]

    # Actualización de la ventana
    pygame.display.update()
    # Llamada a la función de actualización de la ventana
    recargaPantalla()

# Salida del juego
pygame.quit()
