from user.models import User
from mentorship.models import Teacher, Student, Group
from study.models import Specialization, Course
from .annotations import UserAnnotation, SpecializationAnnotation, TeacherAnnotation, CourseAnnotation, StudentAnnotation, GroupAnnotation


USER_DATA: dict = {'email': 'user@email.com',
             'first_name': 'username',
             'last_name': 'user_last',
             'password': '123QWERt'
             }


def create_user()-> UserAnnotation:
    user = User.objects.create_user(email = 'user@email.com', first_name = 'username', last_name = 'user_last', password = '123QWEr')
    return user


def create_specialization() -> SpecializationAnnotation:
    specialization = Specialization.objects.create(name="Mathematics")
    return specialization

def create_teacher() -> TeacherAnnotation:
    user = create_user()
    specialization = create_specialization()
    teacher = Teacher.objects.create(user=user, specialization=specialization)
    return teacher

def create_course() -> CourseAnnotation:
    teacher = create_teacher()
    specialization = create_specialization()
    course = Course.objects.create(name = 'Course_1', description = 'IT', teacher = teacher)
    course.specialization.set([specialization])
    return course


def create_student()-> StudentAnnotation:
    user = create_user()
    students = Student.objects.create(user = user, rating = 6.0, birth_year = '2000-11-13')
    return students


def create_group() -> GroupAnnotation:
    course = create_course()
    students = create_student()
    teacher = create_teacher()
    group = Group.objects.create(name = 'Group_1', course = course, teacher = teacher, students = students)
    # group.students.set([students])
    return group