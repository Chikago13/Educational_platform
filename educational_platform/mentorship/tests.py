from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from constant.costants import USER_DATA, create_user, create_specialization, create_teacher
from .serializers import TeacherSerializer




class CreateTeacherTest(APITestCase):

    def setUp(self):
        self.user = create_user()
        self.specialization = create_specialization()
        self.teacher_data = {
            'user': self.user.id,  
            'specialization': self.specialization.id,
        }


    def test_create_teacher(self):
        url = reverse('teacher-list')
        response = self.client.post(url, data=self.teacher_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTeacherTest(APITestCase):

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
      

class UpdateTeacherTest(APITestCase):

    def setUp(self):
        self.teacher = create_teacher()
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({'specialization': create_specialization().id})


    def test_update_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.put(url, data = self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class DeleteTeacherTest(APITestCase):

    def setUp(self):
        self.teacher = create_teacher()

    
    def test_delete_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



