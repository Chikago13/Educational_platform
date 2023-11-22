from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserAnnotation:
    email: str
    first_name: str
    last_name: str
    password: str


@dataclass(frozen=True, slots=True)
class SpecializationAnnotation:
    name: str


@dataclass(frozen=True, slots=True)
class TeacherAnnotation:
    user: UserAnnotation
    specialization: SpecializationAnnotation


