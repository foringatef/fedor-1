# Открываем файл students (2).csv для чтения
with open('C:/Users/Cheme/Downloads/students (1).csv', encoding='utf-8') as file:
    lines = file.readlines()

# Создаем словарь для хранения средних значений оценок по классу
class_scores = {}

# Проходим по каждой строке файла, кроме первой (заголовков)
for line in lines[1:]:
    parts = line.strip().split(',')  # Разбиваем строку по запятой

    # Извлекаем данные из строки
    student_id = int(parts[0])
    name = parts[1]
    project_id = int(parts[2])
    class_name = parts[3]
    score = int(parts[4]) if parts[4].strip() != 'None' else 0  # Обработка пустых значений

    # Считаем общую сумму оценок и количество учеников в каждом классе
    if class_name in class_scores:
        class_scores[class_name][0] += score
        class_scores[class_name][1] += 1
    else:
        class_scores[class_name] = [score, 1]

# Открываем файл для записи новых данных
with open('student_new.csv', 'w') as new_file:
    new_file.write('id,Name,titleProject_id,class,score\n')  # Записываем заголовок

    # Проходим опять по строкам и заменяем отсутствующие оценки средним значением по классу
    for line in lines[1:]:
        parts = line.strip().split(',')
        student_id = int(parts[0])
        name = parts[1]
        project_id = int(parts[2])
        class_name = parts[3]
        score = int(parts[4]) if parts[4].strip() != 'None' else 0  # Обработка пустых значений

        if score == 0:  # Если оценка отсутствует, заменяем ее средним значением по классу
            avg_score = round(class_scores[class_name][0] / class_scores[class_name][1], 3)
            new_file.write(f"{student_id},{name},{project_id},{class_name},{avg_score}\n")
        else:
            new_file.write(f"{student_id},{name},{project_id},{class_name},{score}\n")

# Выводим необходимую оценку для Владимира
vladimirs_score = None
for line in lines[1:]:
    parts = line.strip().split(',')
    name = parts[1]
    if "Хадаров Владимир" in name:
        vladimirs_score = parts[4]
        break

if vladimirs_score:
    print(f"Ты получил: {vladimirs_score}, за проект - {parts[2]}")
else:
    print("Хадаров Владимир не найден в файле.")

print("Готово! Данные обновлены и сохранены в файл student_new.csv.")
