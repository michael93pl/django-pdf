from django.test import TestCase, Client
from django.urls import reverse
from .forms import KeyForm, FileForm


# forms tests
class TestFileForm(TestCase):
    def test_fileform(self):
        form_data = {'file_name': 'superawesomefile.pdf',
                     'first_name': 'Michal',
                     'last_name': 'Two-Part-Last Name',
                     'birth': '15-12-2013',
                     'pesel': '60081917875',
                     'email': 'test@email.com',
                     'phone_no': '(+48) 601 601 999',
                     'street': 'Longest street in Poland has over 70 characters 293 m.9',
                     'city': 'Bielsko-Biala',
                     'code': '00-123'}

        form = FileForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)


class TestKeyForm(TestCase):
    def test_keyform(self):
        form_data = {'secret_key': 't3nch4r4ct'}
        form = KeyForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)


# views tests
class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_generate_page(self):
        url = reverse('generate')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pdfform.html')


    def test_list_page(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')


