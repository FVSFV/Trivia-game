def quizhistory(score_list):
    questions = {
        "¿Cuál fue la primera capital de Estados Unidos?": "Nueva York",
        "¿Quién fue el primer presidente de Estados Unidos?": "George Washington",
        "¿En qué año comenzó la Primera Guerra Mundial?": "1914",
        "¿Cuál es el río más largo del mundo?": "Nilo",
        "¿Quién pintó la Mona Lisa?": "Leonardo da Vinci",
        "¿En qué año se firmó la Declaración de Independencia de Estados Unidos?": "1776",
        "¿Quién fue el líder de la Revolución Cubana en 1959?": "Fidel Castro",
        "¿Dónde se celebraron los primeros Juegos Olímpicos modernos en 1896?": "Atenas",
        "¿En qué año cayó el Muro de Berlín?": "1989",
        "¿Cuál es la capital de Francia?": "París"
    }

    score = 0

    print("¡Bienvenido al quiz de historia!")
    print("Responde a las siguientes 10 preguntas:")

    for question, answer in questions.items():
        user_answer = input(f"\n{question} ").strip()

        if user_answer.lower() == answer.lower():
            print("¡Respuesta correcta!")
            score += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {answer}")

    score_list.append(score)  # Agregar el puntaje a la lista
    print(f"\nPuntuación final: {score}/10")

def quizanimals(score_list):
    questions = {
        "¿Qué animal es conocido como el 'Rey de la selva'?": "León",
        "¿Qué mamífero vuela y es conocido por dormir boca abajo?": "Murciélago",
        "¿Qué animal es el más grande del mundo?": "Ballena azul",
        "¿Cuál es el animal nacional de Australia que es conocido por saltar alto?": "Canguro",
        "¿Qué ave es conocida por su canto melodioso y es símbolo de la paz?": "Paloma",
        "¿Cuál es el animal terrestre más rápido del mundo?": "Guepardo",
        "¿Qué animal es conocido como el 'Hombre de la jungla'?": "Chimpancé",
        "¿Cuál es el animal que puede cambiar de color para camuflarse en su entorno?": "Camaleón",
        "¿Qué reptil es conocido por ser venenoso y tiene una cola en forma de látigo?": "Escorpión",
        "¿Cuál es el animal marino que tiene tres corazones y ocho brazos?": "Pulpo"
    }

    score = 0

    print("¡Bienvenido al quiz de conocimiento sobre animales!")
    print("Responde a las siguientes 10 preguntas:")

    for question, answer in questions.items():
        user_answer = input(f"\n{question} ").strip()

        if user_answer.lower() == answer.lower():
            print("¡Respuesta correcta!")
            score += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {answer}")

    score_list.append(score)  # Agregar el puntaje a la lista
    print(f"\nPuntuación final: {score}/10")

def quizcapitals(score_list):
    questions = {
        "¿Cuál es la capital de Francia?": "París",
        "¿Cuál es la capital de Japón?": "Tokio",
        "¿Cuál es la capital de Italia?": "Roma",
        "¿Cuál es la capital de España?": "Madrid",
        "¿Cuál es la capital de Alemania?": "Berlín",
        "¿Cuál es la capital de Canadá?": "Ottawa",
        "¿Cuál es la capital de Australia?": "Canberra",
        "¿Cuál es la capital de Brasil?": "Brasilia",
        "¿Cuál es la capital de Rusia?": "Moscú",
        "¿Cuál es la capital de Sudáfrica?": "Pretoria"
    }

    score = 0

    print("¡Bienvenido al quiz de capitales del mundo!")
    print("Responde a las siguientes 10 preguntas:")

    for question, answer in questions.items():
        user_answer = input(f"\n{question} ").strip()

        if user_answer.lower() == answer.lower():
            print("¡Respuesta correcta!")
            score += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {answer}")

    score_list.append(score)  # Agregar el puntaje a la lista
    print(f"\nPuntuación final: {score}/10")


def quizchemistry(score_list):
    questions = {
        "¿Cuál es el símbolo químico del hidrógeno?": "H",
        "¿Cuál es el número atómico del oxígeno?": "8",
        "¿Qué gas constituye la mayor parte de la atmósfera terrestre?": "Nitrógeno",
        "¿Cuál es el proceso por el cual un sólido se convierte en gas sin pasar por el estado líquido?": "Sublimación",
        "¿Cuál es el pH de una solución neutral?": "7",
        "¿Qué elemento químico es esencial para la vida y se encuentra en todas las proteínas?": "Nitrógeno",
        "¿Cuál es el proceso químico por el cual las plantas convierten la luz solar en energía química?": "Fotosíntesis",
        "¿Cuál es el símbolo químico del carbono?": "C",
        "¿Cuál es el gas que las plantas absorben de la atmósfera durante la fotosíntesis?": "Dióxido de carbono",
        "¿Cuál es el proceso químico por el cual el oxígeno se combina con la glucosa para producir energía en las células?": "Respiración celular"
    }

    score = 0

    print("¡Bienvenido al quiz de conocimientos básicos de química!")
    print("Responde a las siguientes 10 preguntas:")

    for question, answer in questions.items():
        user_answer = input(f"\n{question} ").strip()

        if user_answer.lower() == answer.lower():
            print("¡Respuesta correcta!")
            score += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {answer}")

    score_list.append(score)  # Agregar el puntaje a la lista
    print(f"\nPuntuación final: {score}/10")

def quizmath(score_list):
    questions = {
        "¿Cuánto es 2 + 2?": "4",
        "¿Cuál es el resultado de 5 x 3?": "15",
        "¿Cuál es el número anterior a 10?": "9",
        "¿Cuál es el número siguiente a 20?": "21",
        "¿Cuál es el resultado de 10 - 7?": "3",
        "¿Cuál es el doble de 6?": "12",
        "¿Cuál es el triple de 3?": "9",
        "¿Cuánto es 8 dividido por 4?": "2",
        "¿Cuál es el número mayor entre 15 y 8?": "15",
        "¿Cuántos lados tiene un triángulo?": "3"
    }

    score = 0

    print("¡Bienvenido al quiz de conocimientos básicos de matemáticas!")
    print("Responde a las siguientes 10 preguntas:")

    for question, answer in questions.items():
        user_answer = input(f"\n{question} ").strip()

        if user_answer == answer:
            print("¡Respuesta correcta!")
            score += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {answer}")

    score_list.append(score)  # Agregar el puntaje a la lista
    print(f"\nPuntuación final: {score}/10")


def main():
    Intro = '¡Bienvenido a la aplicación de quizzes!'
    Intro2 = '!Esperamos que te diviertas!'
    Intro3 = '!Elige un cuestionario de tu tema favorito y demuesta tus conocimientos!'
    print(Intro)
    print(Intro2)
    print(Intro3)

    scores_matrix = []

    while True:
        print("\nMenu:")
        print("1. Quiz de Historia")
        print("2. Quiz de Animales")
        print("3. Quiz de Capitales")
        print("4. Quiz de Química")
        print("5. Quiz de Matemáticas")
        print("6. Exit")

        choice = input("Elige una opción (1-6): ").strip()

        if choice == '1':
            score_list = []
            quizhistory(score_list)
            scores_matrix.append(score_list)
        elif choice == '2':
            score_list = []
            quizanimals(score_list)
            scores_matrix.append(score_list)
        elif choice == '3':
            score_list = []
            quizcapitals(score_list)
            scores_matrix.append(score_list)
        elif choice == '4':
            score_list = []
            quizchemistry(score_list)
            scores_matrix.append(score_list)
        elif choice == '5':
            score_list = []
            quizmath(score_list)
            scores_matrix.append(score_list)
        elif choice == '6':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()