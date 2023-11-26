from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserAnnotation:
    id: int
    email: str
    first_name: str
    last_name: str
    password: str


@dataclass(frozen=True, slots=True)
class SpecializationAnnotation:
    id: int
    name: str


@dataclass(frozen=True, slots=True)
class TeacherAnnotation:
    id: int
    user: UserAnnotation.id
    specialization: SpecializationAnnotation.id


@dataclass(frozen=True, slots=True)
class CourseAnnotation:
    id: int
    name: str
    description: str
    teacher: TeacherAnnotation.id
    specialization: SpecializationAnnotation.id


@dataclass(frozen=True, slots=True)
class StudentAnnotation:
    id: int
    user: UserAnnotation.id
    rating: float
    birth_year: int


@dataclass(frozen=True, slots=True)
class GroupAnnotation:
    id: int
    name: str
    course: CourseAnnotation.id
    students: StudentAnnotation.id
    teacher: TeacherAnnotation.id