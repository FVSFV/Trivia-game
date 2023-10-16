def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            preguntas = contenido.split('\n\n')  # Separar preguntas y respuestas
            preguntas_dict = {}
            for i in range(0, len(preguntas), 2):
                pregunta = preguntas[i]
                respuesta = preguntas[i + 1] if i + 1 < len(preguntas) else "Respuesta no disponible"
                preguntas_dict[pregunta] = respuesta
            return preguntas_dict
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")
        return {}

def quiz_history(history_file, score_list):#Esta funcion resive el archivo para leer y el score list y como salida es el socre list actualizado
    questions = leer_archivo(history_file)

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

def quiz_animals(quiz_animals_file, score_list):#Esta funcion resive el archivo para leer y el score list y como salida es el socre list actualizado
    questions = leer_archivo(quiz_animals_file)

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

def quiz_capitals(quiz_capitals_file, score_list):#Esta funcion resive el archivo para leer y el score list y como salida es el socre list actualizado
    questions = leer_archivo(quiz_capitals_file)

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

def quiz_chemistry(quiz_chemistry_file, score_list):#Esta funcion resive el archivo para leer y el score list y como salida es el socre list actualizado
    questions = leer_archivo(quiz_chemistry_file)

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

def quiz_math(quiz_math_file, score_list):#Esta funcion resive el archivo para leer y el score list y como salida es el socre list actualizado
    questions = leer_archivo(quiz_math_file)

    score = 0

    print("¡Bienvenido al quiz de conocimientos básicos de matemáticas!")
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

def main():#La funcion main es la que inicia y presenta al usuario
    print('¡Bienvenido a la aplicación de quizzes!')
    print('¡Esperamos que te diviertas!')
    print('¡Elige un cuestionario de tu tema favorito y demuestra tus conocimientos!')
    def imprimirmatriz(scores_matrix,filas,columnas):#Esta es la funcion para que fuera llendo de lista en lista dentro de la matriz para posteriormente imprimir con formato los resultados(no funciono).
        for i in range(filas):
            for j in range(columnas):
                print(matriz[i][j], end=" ")
            print()

    scores_matrix = []#Esta es la matriz donde se guardan los puntajes

    while True:
        print("\nMenu:")
        print("1. Quiz de Historia")
        print("2. Quiz de Animales")
        print("3. Quiz de Capitales")
        print("4. Quiz de Química")
        print("5. Quiz de Matemáticas")
        print("6. Exit")
        print("7. Print my current score")

        choice = input("Elige una opción (1-7): ").strip()#Aqui se elige una opcion para posteriormente llamar a la funcion requerida.

        if choice == '1':
            score_list = []
            quiz_history('historyquiz.txt', score_list)
            scores_matrix.append(score_list)
        elif choice == '2':
            score_list = []
            quiz_animals('quizanimals.txt', score_list)
            scores_matrix.append(score_list)
        elif choice == '3':
            score_list = []
            quiz_capitals('quizcapitals.txt', score_list)
            scores_matrix.append(score_list)
        elif choice == '4':
            score_list = []
            quiz_chemistry('quizquimica.txt', score_list)
            scores_matrix.append(score_list)
        elif choice == '5':
            score_list = []
            quiz_math('quizmath.txt', score_list)
            scores_matrix.append(score_list)
        elif choice == '6':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        elif choice == '7':
            print('Tu puntuación actual es', scores_matrix)
            #print('tu puntuacion en historia es de', imprimirmatriz(scores_matrix,1,1)) Este fue mi intento para darle formato al final score.
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()#Aqui se llama al main
