from user.models import User
from mentorship.models import Teacher
from study.models import Specialization
from .annotations import UserAnnotation, SpecializationAnnotation, TeacherAnnotation


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