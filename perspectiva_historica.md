# Historia de los sistemas de cómputo
Panorama detallado por periodos con enfoque en:
- Era mecánica (antes de 1940)
- Primera generación (1940–1957)
- Segunda generación (1958–1988) [nota: esta periodización extiende lo que muchos textos dividen en segunda, tercera y parte de cuarta generación; aquí se presenta integrada como lo pides, explicando las transiciones internas]

---

## Era mecánica (antes de 1940)
Pequeña definición: Conjunto de dispositivos de cálculo y procesamiento de información que funcionan mediante mecanismos puramente manuales o electromecánicos (engranajes, levas, tarjetas perforadas, relés), sin componentes electrónicos activos como válvulas o transistores. En esta era se sientan las bases de la automatización, la representación simbólica y el control mediante programas físicos (tarjetas o cintas perforadas).

Características generales
- Tecnología dominante: mecánica de precisión y, hacia el final, relés electromecánicos.
- Representación: decimal (ruedas dentadas) y binaria temprana en algunos experimentos.
- Programación: fija por diseño (levas, engranajes), con avances hacia programación configurable (tarjetas perforadas, paneles de conexión).
- Entrada/Salida: tarjetas perforadas, cintas perforadas, teclados mecánicos, impresoras mecánicas.
- Aplicaciones: contabilidad, censos, estadística, navegación, astronomía, criptoanálisis manual/mecánico.

Intervalos clave y hitos
- Antigüedad – 1600s: precursores
  - Ábaco (desde ~s. III a. C.): cómputo manual posicional.
  - Regla de cálculo (Edmund Gunter, 1620s): cálculo analógico continuo.
  - Huesos de Napier (1617): multiplicación mecánica asistida.

- 1642–1800: primeras calculadoras mecánicas
  - Pascalina (Blaise Pascal, 1642): suma/resta por ruedas dentadas.
  - Máquina de Leibniz (1673): rueda escalonada; introduce multiplicación/división mecánica.
  - Aritmómetros (s. XVIII–XIX): comercialización de calculadoras de escritorio.

- 1801–1837: control programado por perforaciones
  - Telar de Jacquard (1801): tarjetas perforadas para patrones; antecede al “programa” externo.
  - Diferential Engine (Babbage, 1822, diseño): cálculo de polinomios/tablas.
  - Analytical Engine (Babbage, 1837, diseño): arquitectura general con unidad de “moler” (CPU), “almacén” (memoria) y control; Ada Lovelace (1843) bosqueja algoritmos, visión de propósito general.

- 1870–1900: mecanización de la estadística y contabilidad
  - Tabuladora de Hollerith (Censo EE. UU. 1890): tarjetas perforadas, clasificación/contabilización; origen de Tabulating Machine Co. (precursora de IBM, 1896).
  - Expansión de máquinas de cálculo de escritorio y sistemas de fichas.

- 1900–1939: electromecánica y transición
  - Máquinas de contabilidad e impresión (IBM) y clasificadoras/tabuladoras de tarjetas.
  - Relés: primeras computadoras de relés y proyectos de automatización.
  - Z1 (Konrad Zuse, 1938): computadora mecánica binaria de punto flotante (experimental).
  - Proyectos prebélicos (Harvard Mark I se completa en 1944, pero se gesta en los 30s).

Limitaciones
- Lentitud, fragilidad mecánica y errores por desgaste/holguras.
- Programas poco flexibles o difíciles de modificar.
- Escalabilidad muy limitada.

Impacto
- Introducción del concepto de programa externo (tarjetas).
- Bases de la arquitectura (unidad de cálculo, memoria, control).
- Industrialización del procesamiento de datos (censos, banca, seguros).

---

## Primera generación (1940–1957)
Pequeña definición: Computadoras electrónicas basadas en tubos de vacío (válvulas termiónicas), con memoria de líneas de retardo, tubos de Williams o tambores magnéticos, y E/S en tarjetas y cintas perforadas. Se consolida el programa almacenado y emergen los primeros lenguajes ensambladores y de alto nivel.

Características generales
- Tecnología dominante: válvulas de vacío; relés aún en máquinas electrome-cánicas.
- Memoria: tubos de Williams, líneas de mercurio, tambores; posteriormente núcleos magnéticos tempranos.
- Programación: código máquina y ensamblador; surgen FORTRAN (1957) y conceptos de compilación.
- Modelo computacional: arquitectura de programa almacenado (von Neumann); paralelamente diseños especializados (Colossus).
- Operación: procesamiento por lotes; sin sistemas operativos complejos; operación manual intensa.

Intervalos clave y hitos
- 1939–1945: prototipos de guerra y pioneros
  - ABC – Atanasoff–Berry Computer (1939–1942): electrónica para álgebra lineal; no programable general.
  - Z3 (Zuse, 1941): computadora de relés programable (electromecánica).
  - Colossus (1943–1944): criptoanálisis británico; electrónica de válvulas.
  - ENIAC (1945): cálculo general electrónico; programación por paneles/conexiones.

- 1946–1951: programa almacenado y primeras ejecuciones
  - EDVAC (diseño 1945): introduce programa almacenado.
  - Manchester Baby (1948): primera ejecución con memoria de tubo de Williams.
  - EDSAC (1949): computador operativo de programa almacenado en Cambridge.
  - IAS/Princeton y ACE (Turing, Pilot ACE 1950).
  - Whirlwind (1951): tiempo real y pantallas CRT para visualización.

- 1951–1957: comercialización y estandarización inicial
  - UNIVAC I (1951): primera computadora comercial en EE. UU.
  - IBM 701 (1952) y IBM 650 (1954): dominancia IBM en científico/negocios.
  - Ferranti Mark I (1951): comercialización en Reino Unido.
  - Memoria de núcleos magnéticos comienza a adoptarse a mediados de los 50.
  - Lenguajes: ensambladores, FORTRAN (1957) para cómputo científico.
  - Procesamiento por lotes: tarjetas perforadas y cintas magnéticas.

Limitaciones
- Altísimo consumo y calor; MTBF bajo (fallas frecuentes).
- Tamaño físico y costo elevados; mantenimiento constante.
- Programación compleja, herramientas inmaduras.

Impacto
- Consolidación del paradigma de programa almacenado.
- Primer mercado de computadoras comerciales.
- Fundación de la ingeniería de software y compiladores.

Ejemplos representativos
- ENIAC, EDSAC, EDVAC, IAS, Whirlwind, UNIVAC I, IBM 701/704/650, Ferranti Mark I.

---

## Segunda generación (1958–1988)
Pequeña definición: Periodo en el que las computadoras migran de válvulas a transistores y, progresivamente, a circuitos integrados y microprocesadores, con mejoras radicales en fiabilidad, costo, tamaño y capacidades de software (sistemas operativos, multiprogramación, tiempos compartidos). Nota: académicamente, la “segunda generación” suele situarse ~1958–1964; aquí se extiende hasta 1988 como solicitaste, subdividiendo las transiciones internas.

Características transversales
- Tecnología: transistores (finales 50s), luego circuitos integrados SSI/MSI (60s) y VLSI (70s–80s), culminando en microprocesadores.
- Memoria: núcleos magnéticos (60s), DRAM (desde 1970).
- Software: COBOL (1959), ALGOL 60, OS/360 (1964–68), Unix (1969), CP/M (70s), MS‑DOS (1981), primeras GUIs comerciales (1981–84).
- Modos de uso: batch → multiprogramación → tiempo compartido → interactivo/personal.
- Redes: de terminales y mainframes a ARPANET (finales 60s/70s) y LANs Ethernet (80s).

Subperiodos e hitos
- 1958–1964: era del transistor
  - Tecnología: reemplazo de válvulas por transistores; fiabilidad y densidad mejoran.
  - Equipos: IBM 1401 (1959, decimal, transistorizada), IBM 7090 (1959, científico), DEC PDP‑1 (1959), UNIVAC Solid State.
  - Software: COBOL (1959), ALGOL 60 (1960); primeros sistemas de multiprogramación experimentales.
  - Interacción: lotes con avances hacia terminales; almacenamiento: cintas, tambores, discos (IBM 305 RAMAC, 1956).

- 1965–1971: integración y estandarización de arquitecturas
  - Circuitos integrados SSI/MSI y consolidación de familias.
  - IBM System/360 (1964, despliegue y ecosistema en 1965–69): unifica arquitectura para múltiples modelos; OS/360.
  - Minicomputadores: DEC PDP‑8 (1965) democratiza la computación departamental.
  - Tiempo compartido: CTSS (MIT), Multics (1965), Unix (1969).
  - Lenguajes: PL/I, BASIC (1964), Pascal (1970).

- 1971–1977: nacimiento del microprocesador y microcomputadoras
  - Microprocesadores: Intel 4004 (1971), 8008 (1972), 8080 (1974); Motorola 6800 (1974); MOS 6502 (1975); Zilog Z80 (1976).
  - Sistemas: Altair 8800 (1975), IMSAI 8080, Apple I (1976), Apple II/Commodore PET/TRS‑80 (1977).
  - Software: CP/M (Gary Kildall), BASIC popularizado; primeras comunidades “hobbyist”.
  - Memoria/almacenamiento: DRAM Intel 1103 (1970); disquete 8" (1971), 5.25" (1976).

- 1978–1984: 16 bits, PCs y GUIs iniciales
  - CPUs: Intel 8086 (1978), 8088 (IBM PC 5150, 1981), Motorola 68000 (1979).
  - Plataformas: IBM PC (1981), compatibles; Xerox Star (1981), Apple Lisa (1983), Apple Macintosh (1984).
  - Sistemas operativos: MS‑DOS (1981), Xenix/Unix comerciales; redes: expansión de ARPANET; Ethernet estandarizándose (10BASE5/10BASE2).
  - Software: hojas de cálculo (VisiCalc 1979, Lotus 1‑2‑3 1983), editores, compiladores C en microcomputadoras.

- 1985–1988: 32 bits, estaciones de trabajo y expansión de redes
  - CPUs: Intel 80386 (1985), MIPS R2000 (1985), SPARC (1987), ARM1 (1985).
  - Plataformas: estaciones de trabajo Sun/SGI; PCs 386 con memoria extendida; Amiga (1985), Atari ST (1985).
  - Sistemas: UNIX System V/BSD, X11 (1984/1987), MS Windows 1.0 (1985) y 2.0 (1987).
  - Redes: TCP/IP adoptado en ARPANET (1983, consolidado en adelante); LANs Ethernet en empresas; Novell NetWare.
  - Gráficos y GUI: aceleración 2D temprana; DTP (Desktop Publishing) con Mac + LaserWriter (1985).

Evolución de capacidades
- Rendimiento: de MIPS fraccionales a decenas/centenas de MIPS en estaciones de trabajo a fines de los 80.
- Fiabilidad: órdenes de magnitud mejor que válvulas; MTBF eleva, mantenimiento baja.
- Accesibilidad: de centros de cómputo a computación personal y departamental.
- Software: surge la ingeniería del software moderna, sistemas de archivos avanzados, compiladores portables (C), y ecosistemas de desarrollo.

Limitaciones persistentes por subperiodo
- 1958–1964: costos aún altos, escasez de software maduro.
- 1965–1971: complejidad de proyectos (OS/360), costos de integración.
- 1971–1977: recursos muy limitados en micros; fragmentación de hardware/software.
- 1978–1984: compatibilidad y estandarización aún inestables; GUIs costosas.
- 1985–1988: gestión de memoria y multitarea en PCs limitada; interoperabilidad de redes en evolución.

Ejemplos representativos
- Mainframes/minis: IBM System/360, IBM 370 (inicio 1970), DEC PDP‑8/PDP‑11, VAX (1977).
- Micros/PCs: Altair 8800, Apple II, Commodore PET, TRS‑80, IBM PC, Macintosh, Amiga, compatibles 286/386.
- Estaciones: Sun-3/Sun-4, SGI IRIS, Apollo Domain.

---

## Glosario breve
- Programa almacenado: instrucción y datos residen en la misma memoria, ejecutados por una unidad de control.
- Multiprogramación: ejecución intercalada de múltiples programas en memoria.
- Tiempo compartido (time-sharing): múltiples usuarios interactivos conectados a un sistema central.
- Circuito integrado (IC): encapsula múltiples transistores en un chip; SSI/MSI/LSI/VLSI según densidad.
- Microprocesador: CPU completa en un solo chip.

## Notas y observaciones
- Clasificación por “generaciones” varía por autor: a menudo 2ª gen (1958–1964), 3ª (1964–1971), 4ª (desde 1971). Aquí se integró 1958–1988 como “segunda” para cubrir la transición completa de transistores a microprocesadores, destacando subperiodos para preservar precisión histórica.
