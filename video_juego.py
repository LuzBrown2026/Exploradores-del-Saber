import os
import sys
import time
COLORES = {
    "1": {
        "nombre": "Cian",
        "principal": "\033[96m",
        "secundario": "\033[36m",
        "exito": "\033[92m",
        "error": "\033[91m",
        "advertencia": "\033[93m",
        "titulo": "\033[96m",
    },
    "2": {
        "nombre": "Verde",
        "principal": "\033[92m",
        "secundario": "\033[32m",
        "exito": "\033[92m",
        "error": "\033[91m",
        "advertencia": "\033[93m",
        "titulo": "\033[92m",
    },
    "3": {
        "nombre": "Amarillo",
        "principal": "\033[93m",
        "secundario": "\033[33m",
        "exito": "\033[92m",
        "error": "\033[91m",
        "advertencia": "\033[93m",
        "titulo": "\033[93m",
    },
    "4": {
        "nombre": "Magenta",
        "principal": "\033[95m",
        "secundario": "\033[35m",
        "exito": "\033[92m",
        "error": "\033[91m",
        "advertencia": "\033[93m",
        "titulo": "\033[95m",
    },
}
RESET = "\033[0m"
def aplicar_color(texto, color, tipo="principal"):
    return f"{color[tipo]}{texto}{RESET}"
def imprimir(texto="", color=None, tipo="principal"):
    if color is None:
        print(texto)
    else:
        print(aplicar_color(texto, color, tipo))
def mostrar_titulo(texto, color):
    separador = "=" * 45
    imprimir(separador, color, "secundario")
    imprimir(texto.center(45), color, "titulo")
    imprimir(separador, color, "secundario")
def texto_lento(texto, color, tipo="principal", demora=0.015):
    """Efecto máquina de escribir aplicando el color seleccionado."""
    texto_coloreado = aplicar_color(texto, color, tipo)
    for caracter in texto_coloreado:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(demora)
    print()
class Pais:
    def __init__(self, nombre, cultura, niveles, ilustracion):
        self.nombre = nombre
        self.cultura = cultura
        self.niveles = niveles
        self.ilustracion = ilustracion
    def mostrar_informacion(self, color):
        mostrar_titulo(self.nombre.upper(), color)
        imprimir(f"Cultura: {self.cultura}", color, "secundario")
        imprimir(self.ilustracion, color, "principal")
    def jugar_niveles(self, color):
        imprimir(f"\nComienza la aventura por {self.nombre}...", color, "titulo")
        for numero, nivel in enumerate(self.niveles, 1):
            mostrar_titulo(f"NIVEL {numero} DE {len(self.niveles)}", color)
            texto_lento(
                f"\n[Historia]\n{nivel['cuento']}", color, "principal"
            )
            imprimir(nivel["ascii_nivel"], color, "secundario")
            pregunta, opciones, correcta, explicacion = nivel["desafio"]
            while True:
                imprimir("\nDESAFÍO", color, "titulo")
                imprimir(pregunta, color, "principal")
                for opcion in opciones:
                    imprimir(opcion, color, "secundario")

                respuesta = (
                    input(aplicar_color("\nTu respuesta (A, B o C): ", color))
                    .strip()
                    .upper()
                )
                if respuesta == correcta:
                    imprimir(
                        "\n¡Correcto! Has superado el nivel.", color, "exito"
                    )
                    break
                else:
                    imprimir("\nRespuesta incorrecta.", color, "error")
                    imprimir(
                        f"Pista / Retroalimentación: {explicacion}",
                        color,
                        "advertencia",
                    )
                    imprimir("Inténtalo de nuevo...", color, "secundario")
class Guatemala(Pais):
    def __init__(self):
        arte_ascii = r"""
        /\ /\
       /  \  /\  /  \
      /\/  \/  \/
        GUATEMALA
        """
        niveles = [
            {
                "cuento": (
                    "Al amanecer, una niña llamada Ixchel caminó con su abuela por un sendero cubierto de flores. "
                    "La abuela le explicó que Guatemala es conocida como el país de la eterna primavera por su "
                    "clima agradable y la variedad de plantas que crecen en sus regiones."
                ),
                "ascii_nivel": r"""
                    .-.
                  .-(   )-.
                     (.)
                    FLORES
                """,
                "desafio": (
                    "¿Por qué Guatemala es conocida como el país de la eterna primavera?",
                    (
                        "A) Por su clima agradable y sus flores",
                        "B) Porque siempre está nevando",
                        "C) Porque no tiene estaciones",
                    ),
                    "A",
                    "La expresión se relaciona con el clima templado y la variedad de flores del país.",
                ),
            },
            {
                "cuento": (
                    "Mientras Ixchel descansaba en el bosque, escuchó un sonido suave entre las hojas. Era un quetzal "
                    "atrapado entre unas ramas. La niña lo liberó y el ave voló hacia las montañas. Su abuela le contó "
                    "que el quetzal representa la libertad porque no puede vivir encerrado."
                ),
                "ascii_nivel": r"""
                   \ | /
                   \ | /
                  ---( )---
                   / | \
                   / | \
                  QUETZAL
                """,
                "desafio": (
                    "¿Qué representa el quetzal?",
                    (
                        "A) La libertad",
                        "B) El invierno",
                        "C) La riqueza mineral",
                    ),
                    "A",
                    "El quetzal se relaciona con la libertad porque no soporta vivir en cautiverio.",
                ),
            },
            {
                "cuento": (
                    "Ixchel llegó al lago de Atitlán y observó cómo el agua reflejaba las nubes. Desde la orilla pudo "
                    "ver tres grandes volcanes: San Pedro, Tolimán y Atitlán. Su abuela le dijo que esas montañas "
                    "parecían guardianes del lago."
                ),
                "ascii_nivel": r"""
                   /\   /\   /\
                  /  \ /  \ /  \
                 /\  /\  /__\
                 VOLCANES Y LAGO
                """,
                "desafio": (
                    "¿Qué rodea al lago de Atitlán?",
                    (
                        "A) Tres volcanes",
                        "B) Tres desiertos",
                        "C) Tres océanos",
                    ),
                    "A",
                    "El lago está rodeado por los volcanes San Pedro, Tolimán y Atitlán.",
                ),
            },
            {
                "cuento": (
                    "En una comunidad maya, Ixchel observó a una mujer que tejía una franja llena de colores. "
                    "La tejedora movía con cuidado los hilos usando un telar de cintura. Cada figura representaba "
                    "una parte de la historia y la identidad de su pueblo."
                ),
                "ascii_nivel": r"""
                 |#|#|#|#|#|#|
                 | TEJIDO MAYA |
                 |#|#|#|#|#|#|
                """,
                "desafio": (
                    "¿Qué instrumento se utiliza tradicionalmente para elaborar algunos textiles mayas?",
                    (
                        "A) Un telar de cintura",
                        "B) Una impresora",
                        "C) Una máquina de vapor",
                    ),
                    "A",
                    "El telar de cintura es una técnica ancestral de varios pueblos mayas.",
                ),
            },
            {
                "cuento": (
                    "Antes de regresar a casa, Ixchel encontró un libro antiguo llamado Popol Vuh. Su abuela le "
                    "explicó que este texto narra parte de la cosmovisión maya y cuenta que los seres humanos "
                    "fueron creados a partir del maíz."
                ),
                "ascii_nivel": r"""
                 +----------------+
                 |   POPOL VUH    |
                 +----------------+
                       \ | /
                       \ | /
                        \|/
                        MAÍZ
                """,
                "desafio": (
                    "Según el relato del Popol Vuh, ¿de qué fueron creados los seres humanos?",
                    ("A) De piedra", "B) De maíz", "C) De metal"),
                    "B",
                    "En la cosmovisión narrada en el Popol Vuh, el maíz tiene un papel fundamental en la creación.",
                ),
            },
        ]
        super().__init__(
            "Guatemala",
            "Cultura Maya y tradiciones vivas",
            niveles,
            arte_ascii,
        )
class CoreaDelSur(Pais):
    """Clase Hija para Corea del Sur"""

    def __init__(self):
        arte_ascii = r"""
           .---.   .---.
          /     \ /     \
         |   O   |---|   O   |
          \     / \     /
          COREA DEL SUR
        """
        niveles = [
            {
                "cuento": (
                    "En una escuela de Seúl, una niña llamada Hana quería escribirle una carta a su abuela. "
                    "Su maestro le enseñó que el rey Sejong impulsó la creación del Hangul para que más personas "
                    "pudieran leer y escribir con facilidad."
                ),
                "ascii_nivel": r"""
                   ㄱ ㄴ ㄷ ㄹ
                   ㅁ ㅂ ㅅ ㅇ
                     HANGUL
                """,
                "desafio": (
                    "¿Quién impulsó la creación del Hangul?",
                    (
                        "A) El rey Sejong",
                        "B) Un emperador romano",
                        "C) Un explorador europeo",
                    ),
                    "A",
                    "El rey Sejong promovió el Hangul en el siglo XV para facilitar la lectura y la escritura.",
                ),
            },
            {
                "cuento": (
                    "Para una celebración familiar, Hana ayudó a su madre a preparar un Hanbok. La ropa tenía colores "
                    "brillantes y líneas suaves. Al vestirse, Hana comprendió que la ropa tradicional también puede "
                    "contar parte de la historia de un pueblo."
                ),
                "ascii_nivel": r"""
                     /\
                    /  \
                   /__\
                   HANBOK
                """,
                "desafio": (
                    "¿Cómo se llama la vestimenta tradicional coreana?",
                    ("A) Hanbok", "B) Sari", "C) Kimono"),
                    "A",
                    "El Hanbok es el traje tradicional que destaca por su elegancia y valor cultural.",
                ),
            },
            {
                "cuento": (
                    "En la cocina de su abuela, Hana vio varias vasijas cerradas. Dentro había vegetales preparados "
                    "con sal y condimentos. La abuela le explicó que el kimchi necesita fermentarse para desarrollar "
                    "su sabor característico."
                ),
                "ascii_nivel": r"""
                     _
                   .' '.
                  / KIMCHI \
                  '---------'
                """,
                "desafio": (
                    "¿Qué proceso es importante para preparar el kimchi?",
                    ("A) Fermentación", "B) Congelación", "C) Evaporación"),
                    "A",
                    "El kimchi se prepara mediante un proceso tradicional de fermentación en vasijas.",
                ),
            },
            {
                "cuento": (
                    "Durante una excursión, Hana visitó el palacio Gyeongbokgung. Caminó por sus patios y observó "
                    "sus techos tradicionales. Al salir, vio edificios modernos y comprendió cómo Corea del Sur combina "
                    "su historia con la tecnología."
                ),
                "ascii_nivel": r"""
                    /\   /\
                   /  \_/  \
                  |  PALACIO  |
                  |GYEONGBOKGUNG|
                """,
                "desafio": (
                    "¿Cuál es un palacio histórico de Seúl?",
                    ("A) Gyeongbokgung", "B) El Coliseo", "C) El Taj Mahal"),
                    "A",
                    "Gyeongbokgung es el palacio principal edificado por la dinastía Joseon.",
                ),
            },
            {
                "cuento": (
                    "Cuando llegó el Chuseok, la familia de Hana se reunió para compartir alimentos y agradecer por "
                    "la cosecha. También recordaron a sus antepasados y pasaron tiempo juntos. Para Hana, la celebración "
                    "demostró la importancia de la familia."
                ),
                "ascii_nivel": r"""
                    .-.
                  .-(   )-.
                     (.)
                   CHUSEOK
                """,
                "desafio": (
                    "¿Qué se celebra durante el Chuseok?",
                    (
                        "A) La cosecha y la unión familiar",
                        "B) El inicio de una guerra",
                        "C) La llegada del invierno",
                    ),
                    "A",
                    "El Chuseok es el gran festival de la cosecha y gratitud en familia.",
                ),
            },
        ]
        super().__init__(
            "Corea del Sur",
            "Historia, tradiciones y tecnología",
            niveles,
            arte_ascii,
        )
class Sudafrica(Pais):
    def __init__(self):
        arte_ascii = r"""
             _
           .' '.
          /     \
         / SUDÁFRICA\
         '-----------'
        """
        niveles = [
            {
                "cuento": (
                    "Al llegar a una plaza de Sudáfrica, Thabo escuchó a personas hablar diferentes idiomas y vio danzas "
                    "de varias comunidades. Su profesora le explicó que el país es llamado la Nación del Arcoíris por "
                    "la diversidad de sus culturas y pueblos."
                ),
                "ascii_nivel": r"""
                    \ | /
                   -- * --
                    / | \
                  NACIÓN DEL ARCOÍRIS
                """,
                "desafio": (
                    "¿Por qué Sudáfrica es llamada la Nación del Arcoíris?",
                    (
                        "A) Por su diversidad cultural",
                        "B) Porque siempre llueve",
                        "C) Por sus minas de zafiro",
                    ),
                    "A",
                    "El nombre representa la unión y diversidad de pueblos y culturas del país.",
                ),
            },
            {
                "cuento": (
                    "Thabo viajó al Parque Nacional Kruger con su familia. Durante el recorrido observó huellas y "
                    "escuchó animales a lo lejos. El guía le contó que el parque protege una gran variedad de fauna "
                    "de la sabana africana."
                ),
                "ascii_nivel": r"""
                    /  \__
                   (  .-'
                   |  |
                   /_|
                   LEÓN
                """,
                "desafio": (
                    "¿Qué parque nacional es famoso por su fauna en Sudáfrica?",
                    ("A) Kruger", "B) Yellowstone", "C) Doñana"),
                    "A",
                    "El Parque Nacional Kruger es una de las reservas más grandes y famosas de África.",
                ),
            },
            {
                "cuento": (
                    "Desde Ciudad del Cabo, Thabo miró una montaña cuya cima parecía una enorme mesa. El guía le "
                    "explicó que por esa forma recibe el nombre de Table Mountain. Desde arriba podían observar "
                    "la ciudad y el océano."
                ),
                "ascii_nivel": r"""
                     __
                    |  |
                   | TABLE MOUNTAIN |
                   |__|
                """,
                "desafio": (
                    "¿Qué forma tiene la cima de Table Mountain?",
                    (
                        "A) Plana",
                        "B) En forma de espiral",
                        "C) Completamente redonda",
                    ),
                    "A",
                    "Su cima es plana, semejante a una gran mesa.",
                ),
            },
            {
                "cuento": (
                    "En un museo, Thabo encontró fotografías de Nelson Mandela. Su guía le explicó que Mandela luchó "
                    "contra la injusticia y trabajó por la reconciliación entre las personas. Thabo comprendió que la paz "
                    "también requiere valentía."
                ),
                "ascii_nivel": r"""
                    \o/
                     |
                    / \
                   PAZ Y JUSTICIA
                """,
                "desafio": (
                    "¿Por qué es recordado Nelson Mandela?",
                    (
                        "A) Por luchar por la igualdad y la paz",
                        "B) Por descubrir un nuevo océano",
                        "C) Por inventar el ferrocarril",
                    ),
                    "A",
                    "Mandela es recordado por su incansable labor a favor de los derechos humanos y la reconciliación.",
                ),
            },
            {
                "cuento": (
                    "Antes de terminar el viaje, Thabo conoció a niños que hablaban diferentes idiomas. La maestra le "
                    "contó que Sudáfrica reconoce once idiomas oficiales. Thabo pensó que cada lengua era una forma "
                    "distinta de guardar la memoria de una comunidad."
                ),
                "ascii_nivel": r"""
                   A B C D E
                   F G H I J K
                  11 IDIOMAS OFICIALES
                """,
                "desafio": (
                    "¿Cuántos idiomas oficiales reconoce Sudáfrica?",
                    ("A) Tres", "B) Once", "C) Uno"),
                    "B",
                    "Sudáfrica reconoce 11 lenguas oficiales en su constitución.",
                ),
            },
        ]
        super().__init__(
            "Sudáfrica",
            "Diversidad cultural, naturaleza e historia",
            niveles,
            arte_ascii,
        )
def crear_perfil():
    print("\n" + "=" * 45)
    print("CREACIÓN Y PERSONALIZACIÓN DE PERFIL".center(45))
    print("=" * 45)
    nombre = input("Ingresa el nombre de tu avatar: ").strip()
    while not nombre:
        nombre = input(
            "El nombre no puede estar vacío. Inténtalo otra vez: "
        ).strip()
    print("\nElige el estilo de tu avatar:")
    print("1) Explorador con sombrero: [o_o]/^")
    print("2) Sabio con lentes: (⌐■_■)")
    print("3) Aventurero alegre: (^‿^)")
    avatar_opcion = input("Opción (1-3): ").strip()
    avatares = {
        "1": "[o_o]/^ Explorador",
        "2": "(⌐■_■) Sabio",
        "3": "(^‿^) Aventurero",
    }
    avatar = avatares.get(avatar_opcion, "(^‿^) Aventurero")
    print("\nElige el color de toda la interfaz:")
    for clave, datos in COLORES.items():
        print(f"{clave}) {datos['principal']}{datos['nombre']}{RESET}")
    color_opcion = input("Opción (1-4): ").strip()
    color = COLORES.get(color_opcion, COLORES["1"])
    perfil = {
        "nombre": nombre,
        "avatar": avatar,
        "color": color,
        "paises_completados": [],
    }
    mostrar_titulo("PERFIL CREADO", color)
    imprimir(f"Jugador: {nombre}", color, "principal")
    imprimir(f"Avatar: {avatar}", color, "secundario")
    imprimir(
        "El color seleccionado se aplicará a la interfaz completa.",
        color,
        "exito",
    )
    return perfil
def mostrar_mapa(paises, perfil):
    color = perfil["color"]
    mostrar_titulo("MAPA DE LA TIERRA", color)
    imprimir(
        r"""
       .-''''-.
     .-'  __  '-.
    / .' MUNDO '. \
   ; /          \ ;
   | ;          ; |
   ; \          / ;
    \ '.      .' /
     '. '----' .'
       '-.__.-'
    """,
        color,
        "principal",
    )
    imprimir(
        f"Explorador: {perfil['nombre']} | {perfil['avatar']}",
        color,
        "secundario",
    )
    imprimir("\nPaíses disponibles:", color, "titulo")

    for clave, pais in paises.items():
        estado = (
            "COMPLETADO"
            if pais.nombre in perfil["paises_completados"]
            else "PENDIENTE"
        )
        tipo_est = (
            "exito"
            if estado == "COMPLETADO"
            else "secundario"
        )
        imprimir(f"{clave}) {pais.nombre} [{estado}]", color, tipo_est)
def planeta_creativo(perfil):
    carpeta = "miplanetacreativo"
    os.makedirs(carpeta, exist_ok=True)
    apartados = {
        "1": ("historia.txt", "Historia del planeta"),
        "2": ("leyes.txt", "Leyes y normas"),
        "3": ("relieve.txt", "Relieve y naturaleza"),
        "4": ("habitantes.txt", "Habitantes y criaturas"),
        "5": ("lugares.txt", "Lugares importantes"),
        "6": ("leyendas.txt", "Mitos y leyendas"),
        "7": ("apuntes.txt", "Apuntes libres"),
    }
    color = perfil["color"]
    mostrar_titulo("PLANETA CREATIVO DESBLOQUEADO", color)
    imprimir(
        "Aquí podrás escribir y organizar tu propio universo.",
        color,
        "principal",
    )
    while True:
        mostrar_titulo("MENÚ DEL PLANETA CREATIVO", color)
        for clave, datos in apartados.items():
            imprimir(f"{clave}. {datos[1]}", color, "secundario")
        imprimir("8. Ver un apartado", color, "principal")
        imprimir("9. Guardar y finalizar", color, "exito")
        opcion = input(
            aplicar_color("\nSelecciona una opción: ", color)
        ).strip()
        if opcion in apartados:
            nombre_archivo, titulo = apartados[opcion]
            ruta = os.path.join(carpeta, nombre_archivo)
            mostrar_titulo(titulo.upper(), color)
            if os.path.exists(ruta):
                with open(ruta, "r", encoding="utf-8") as archivo:
                    contenido_anterior = archivo.read()
                imprimir("Este apartado ya tiene contenido:", color, "advertencia")
                imprimir(contenido_anterior, color, "secundario")
                editar = (
                    input(
                        aplicar_color("\n¿Deseas reemplazarlo? (si/no): ", color)
                    )
                    .strip()
                    .lower()
                )
                if editar != "si":
                    continue
            imprimir(
                "Escribe tu texto. Escribe FIN en una línea sola para terminar:",
                color,
                "secundario",
            )
            lineas = []
            while True:
                linea = input()
                if linea.strip().upper() == "FIN":
                    break
                lineas.append(linea)
            contenido = "\n".join(lineas)
            try:
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(contenido)
                imprimir(
                    "Apartado guardado correctamente.", color, "exito"
                )
            except OSError:
                imprimir("No se pudo guardar el apartado.", color, "error")
        elif opcion == "8":
            mostrar_titulo("CONSULTAR APARTADO", color)
            for clave, datos in apartados.items():
                imprimir(f"{clave}. {datos[1]}", color, "secundario")
            apartado = input(
                aplicar_color("\nSelecciona un apartado: ", color)
            ).strip()
            if apartado not in apartados:
                imprimir("Opción no válida.", color, "error")
                continue
            nombre_archivo, titulo = apartados[apartado]
            ruta = os.path.join(carpeta, nombre_archivo)
            if not os.path.exists(ruta):
                imprimir(
                    "Este apartado todavía está vacío.", color, "advertencia"
                )
                continue
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            mostrar_titulo(titulo.upper(), color)
            imprimir(contenido, color, "principal")
        elif opcion == "9":
            mostrar_titulo("PROYECTO GUARDADO", color)
            imprimir(
                f"Tus archivos están en la carpeta: '{carpeta}'",
                color,
                "exito",
            )
            imprimir(
                "¡Gracias por crear tu propio universo!", color, "principal"
            )
            break
        else:
            imprimir("Opción no válida. Intenta de nuevo.", color, "error")
def main():
    print(
        "\033[94m"
        + r""" =============================================
          BIENVENIDO AL VIDEOJUEGO 
           EXPLORADORES DEL SABER 
=============================================
"""
        + RESET
    )
    perfil = crear_perfil()
    color = perfil["color"]

    paises_disponibles = {
        "1": Guatemala(),
        "2": CoreaDelSur(),
        "3": Sudafrica(),
    }
    while len(perfil["paises_completados"]) < len(paises_disponibles):
        mostrar_mapa(paises_disponibles, perfil)
        seleccion = input(
            aplicar_color("\nSelecciona el número del país: ", color)
        ).strip()
        if seleccion not in paises_disponibles:
            imprimir("Selección no válida.", color, "error")
            continue
        pais_actual = paises_disponibles[seleccion]
        if pais_actual.nombre in perfil["paises_completados"]:
            imprimir(
                "Ya completaste este país. Elige otro.", color, "advertencia"
            )
            continue
        pais_actual.mostrar_informacion(color)
        pais_actual.jugar_niveles(color)
        perfil["paises_completados"].append(pais_actual.nombre)
        imprimir(
            f"\n¡Has completado todos los niveles de {pais_actual.nombre}!",
            color,
            "exito",
        )
    planeta_creativo(perfil)

    mostrar_titulo("FINALIZACIÓN DEL PROYECTO", color)
    imprimir("Has completado el recorrido educativo con éxito.", color, "exito")
if __name__ == "__main__":
    main()