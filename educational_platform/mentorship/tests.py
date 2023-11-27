from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from constant.costants import USER_DATA, create_user, create_specialization, create_teacher, create_course, create_student, create_group
from .serializers import TeacherSerializer, GroupSerializer
from .models import Teacher, Student, Group
from user.models import User
from datetime import datetime, timedelta, timezone



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
        user = create_user()
        self.teacher = create_teacher(user)


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
        user = create_user()
        self.teacher = create_teacher(user)
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({'specialization': create_specialization().id})


    def test_update_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.put(url, data = self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class DeleteTeacherTest(APITestCase):

    def setUp(self):
        user = create_user()
        self.teacher = create_teacher(user)

    
    def test_delete_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class CreateGroupTest(APITestCase):

    def setUp(self):
        user = create_user()
        self.course = create_course(user)
        self.student = create_student(user)
        self.teacher = create_teacher(user)
        self.group_data = {
            'name': 'Test Group',
            'course': self.course.id,
            'students': [self.student.id],
            'teacher': self.teacher.id,
        }

    def test_create_group(self):
        url = reverse('group-list')
        response = self.client.post(url, data=self.group_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class ReadGroupTest(APITestCase):

    def setUp(self):
        self.group_id = create_group()

    def test_read_group_list(self):
        url = reverse('group-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_group_detail(self):
        url = reverse('group-detail', args=[self.group_id.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      

class UpdateGroupTest(APITestCase):

    def setUp(self):
        self.group = create_group()
        self.data = GroupSerializer(self.group).data
        self.data.update({'name': 'Group'})

    
    def test_update_group(self):
        url = reverse('group-detail', args=[self.group.id])
        response = self.client.put(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(Group.objects.get(id=self.group.id).date_updated, self.group.date_updated)
        

class DeleteGroupTest(APITestCase):

    def setUp(self):
        self.group_id = create_group()

    def test_delete_group(self):
        url = reverse('group-detail', args=[self.group_id.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)