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
    user: UserAnnotation.id
    specialization: SpecializationAnnotation.id


