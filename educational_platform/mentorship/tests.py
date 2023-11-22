from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from constant.costants import USER_DATA, TEACHER_DATA, create_user, create_specialization, create_teacher
from .serializers import TeacherSerializer




class TeacherTest(APITestCase):

    def setUp(self):
        self.user = create_user()
        self.specialization = create_specialization()

    def test_create_teacher(self):
        url = reverse('teacher-list')
        teacher_data = {
            'user': self.user.id,  
            'specialization': self.specialization.id,
        }
        response = self.client.post(url, data=teacher_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTeacher(APITestCase):

    def setUp(self):
        self.teacher = create_teacher()


    def test_read_teacher_list(self):
        url = reverse('teacher-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_teacher_detail(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      

class UpdateUserTeacher(APITestCase):

    def setUp(self):
        self.teacher = create_teacher()
        # self.user = create_user()
        # self.specialization = create_specialization()
        self.data = TeacherSerializer(self.teacher).data
        # self.data.update({'specialization':'Physics'})
        self.data.update({'specialization': create_specialization().id})


    def test_update_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.put(url, data = self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_teacher(self):
    #     teacher = Teacher.objects.create(user=self.user, specialization=self.specialization)
    #     new_specialization = Specialization.objects.create(name="Physics")
    #     url = reverse('teacher-detail', args=[teacher.id])
    #     data = {"user": self.user.id, "specialization": new_specialization.id}
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)



class DeleteUserTeacher(APITestCase):

    def setUp(self):
        self.teacher = create_teacher()

    
    def test_delete_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



