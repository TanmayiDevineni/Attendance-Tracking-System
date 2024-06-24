import os
import face_recognition


def getPathsForStudents(path, section):
    students_list = []
    students = {}
    section_path = os.path.join(path, section)
    students_list = os.listdir(section_path)

    # print(students_list)

    for student_name in students_list:
        student_path = os.path.join(section_path, student_name)
        # print(student_path)
        student_images_paths = os.listdir(student_path)
        if len(student_images_paths) == 0:
            print(f"No Images found for student {student_name}")
        else:
            students[student_name] = os.path.join(student_path, student_images_paths[0])
    return students


def getEncodingsAndNames(students: dict):
    known_face_encodings = []
    known_face_names = []
    for name, path in students.items():
        image = face_recognition.load_image_file(path)
        student_encoding = None
        try:
            student_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(student_encoding)
            known_face_names.append(name)
        except:
            print(f"Failed to recognize face for student {name}")
    return [known_face_encodings, known_face_names]
