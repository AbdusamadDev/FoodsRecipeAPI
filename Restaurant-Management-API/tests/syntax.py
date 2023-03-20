# def _zip(lst: list):
#     small = []
#     big = []
#     for i in range(len(lst[0])):
#         for j in lst:
#             small.append(j[i])
#         big.append(tuple(small))
#         small.clear()
#     return big

# def is_different(zipped_list: list):
#     for i in zipped_list:
#         if len(tuple(i)) != len(set(i)):
#             print(len(tuple(i)), len(set(i)))
#             return True
#     return False

# # golden function


# def cycle():
#     while True:
#         print(inner_function()[0], "\n")
#         print("zip :", str(_zip(inner_function()[0])))
#         print(is_different(_zip(inner_function()[0])))
#         if is_different(_zip(inner_function()[0])):
#             return inner_function()[1]


# # d = {"asd": "Asd", "sd": "wewer"}
# # # del d["asd"]
# # for i in d:
# #     print(i)

# ls = ["sd", "Asd", "wer"]

# ls.remove("sd")
# print(ls)

# temp = 0
# for i in range(3):
#     print(i)
#     print("____________")
#     while temp != 3:
#         temp += 1
#         print(temp)
#     temp = 0

# for i in "asd":
#     print(i)

# print(["asd", "asdd", "qwr"] == ["qwr", "asd", "asdd"])
# tpl = ("asd", "asd", "asd")
# print(tpl)

# def frenquent(lst: list):
#     z = zip(lst)
#     return list(z)


# def zip(lst: list):
#     small = []
#     big = []
#     for i in range(len(lst[0])):
#         for j in lst:
#             small.append(j[i])
#         big.append(tuple(small))
#         small.clear()
#     return big

# def is_different(zipped_list: list):
#     for i in zipped_list:
#         for j in i:
#             if len(j) != len(set(j)):
#                 return False
#     return True

# print(len(("asd", "qwe"))==len({"asd", "qwe"}))
# print(is_different(zip([["asd", "qwe", "asd"], ["qwe", "asd", "qwe"]])))

# ls = ["asd", "QWe", "df"]
# ls.append(["qwe"])
# print(ls)

# tpl = ("asd", "QW", "asd")
# tpl = set(tpl)
# print(len(tpl))
# import random, time, sqlite3

# db = sqlite3.connect("db.db")
# cursor = db.cursor()

# class_5 = ["ona tili", "matematika", "geografiya", "ingliz tili", "jismon", "fan"]
# class_6 = ["astronomiya", "biologiya"] + class_5
# class_7 = ["anatomiya", "fizika"] + class_6

# table_names = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""").fetchall()

# lessons = [class_5, class_6, class_7]

# def _zip(ls: list):
#     zipped = list()
#     inner_list = list()
#     for i in range(len(ls[0])):
#         for j in ls:
#             inner_list.append(j[i])
#         zipped.append(tuple(inner_list))
#         inner_list.clear()
#     return zipped

# def is_different(zipped_list):
#     for k in zipped_list:
#         if len(tuple(k)) != len(set(k)):
#             return False
#     return True

# def get_lesson_data():
#     lesson = ""
#     ls = []
#     chosen_lessons_list = []
#     counter = 0
#     for i in lessons:
#         while counter != 6:
#             chosen = random.choice(i)
#             if chosen not in ls:
#                 lesson += str(counter + 1) + " " + chosen + "\n"
#                 ls.append(chosen)
#                 counter += 1
#         chosen_lessons_list.append(tuple(ls))
#         ls.clear()
#         counter = 0
#         lesson += "\n"
#     return chosen_lessons_list, lesson 

# def loop():
#     while True:
#         time.sleep(.5)
#         print(get_lesson_data()[1])
#         if is_different(zipped_list=_zip(get_lesson_data()[0])):
#             return get_lesson_data()[1]
    

# print(loop())

# def parallel(journal: list, lesson: str):
#     lesson_list = [d.strip() for d in lesson.split("\n")][:-1]
#     for i in journal:
#         for j in i.split("\n"):
#             try:
#                 if j == lesson_list[int(i.split("\n").index(j))]:
#                     return True
#             except IndexError:
#                 break
#     return False

# def get_lessons(ls):
#     whole_lesson = ""
#     t = 0
#     chosens = []
#     while t != 6:
#         lesson = random.choice(ls)
#         if lesson not in chosens:
#             whole_lesson += lesson + "\n"
#             chosens.append(lesson)
#             t += 1 
#     chosens.clear()
#     t = 0
#     return whole_lesson

# def safely_get_lessons():
#     journal = []
#     for i in lessons:
#         while True:
#             lesson = get_lessons(i)
#             if not parallel(journal=journal, lesson=lesson):
#                 journal.append(lesson)
#                 break
#     return journal



# s = [
#     """1 fizika
#     2 anatomiya
#     3 biologiya
#     4 jismon
#     5 astronomiya
#     6 matematika""", 

#     """1 matematika
#     2 biologiya
#     3 anatomiya
#     4 tarboya
#     5 ingliz tili
#     6 uqish""",
# ]

# print(
#     parallel(
#         s, 
#         """1 fizikas
#         2 asd
#         3 qwe
#         4 erf
#         5 ert
#         6 trhgb"""
#     )
# )
# import sqlite3

# connection = sqlite3.connect("data.db")
# cursor = connection.cursor()

# def get_table_names():
#     fetch = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""").fetchall()
#     table_names = [i[0] for i in fetch]
#     return table_names

# def create_classroom(class_degree: str, class_letter: str):
#     alphabet = [chr(i) for i in range(97, 123)]
#     if class_letter.lower() in alphabet:
#         if class_degree in [str(i) for i in range(1, 12)]:
#             cursor.execute(
#                 """CREATE TABLE IF NOT EXISTS '%s' 
#                 ("id" INTEGER, "lesson_name" TEXT NOT NULL UNIQUE, PRIMARY KEY ("id"))""" 
#                 % str(class_degree + class_letter.capitalize())
#             )
#             connection.commit()

# create_classroom("11", "D")
# def add_lessons(class_name: str, lesson_name: str):
#     try:
#         cursor.execute(
#             """INSERT INTO '%s' (lesson_name) VALUES (?)""" % class_name, 
#             (lesson_name,)
#         )
#         connection.commit()
#     except sqlite3.IntegrityError:
#         return "[ERROR] Bu dars nomi jadvalga allaqachon qo'shib bo'lingan."
# def get_lessons_from_db() -> list:
#     lessons = []
#     for i in get_table_names():
#         lesson_in_table = tuple(cursor.execute("""SELECT * FROM '%s';""" % i).fetchall())
#         lessons.append(lesson_in_table)
#     return lessons
# print(get_lessons_from_db())

print(len("jismoniy madaniyattt"))