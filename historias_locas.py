# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con _________ .

organizacion = "Laboratoria"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") #f-string

# Mad Libs(Historias Locas)

# Mad Libs (Historias Locas)

adj = input("Adjetivo: ") # asombroso
verbo1 = input("Verbo: ") # resolver
verbo2 = input("Verbo: ") # programar
sustantivo_plural = input("Sustantivo (plural): ") # metas, objetivos

madlib = f"¡Programar es {adj}! Siempre me emociona porque me encanta {verbo1} problemas. \
¡Aprende a {verbo2} con Laboratoria y alcanza tus {sustantivo_plural}!"

print(madlib)