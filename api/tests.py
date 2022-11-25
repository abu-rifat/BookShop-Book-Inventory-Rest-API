from django.test import TestCase

# Create your tests here.
import requests


def test_add_book():
    url = 'http://127.0.0.1:8000/api/book/add/'
    myobj = {
        'ISBN': '0987654321',
        'title': 'The API Journey',
        'author': 'The Group',
        'published': 1989,
        'publisher': 'Django Pub',
        'price': 200,
        'available': 5,
    }
    x = requests.post(url, json = myobj)
    print(x.text)


def test_update_book():
    url = 'http://127.0.0.1:8000/api/book/update/'
    myobj = {
        'id':5,
        'ISBN': '1234509876',
        'title': 'Yes',
        'author': 'Distructors',
        'published': 1999,
        'publisher': 'Oh, no!',
        'price': 540,
        'available': 21,
    }
    x = requests.put(url, json = myobj)
    print(x.text)

def test_delete_book():
    url = 'http://127.0.0.1:8000/api/book/delete/'
    myobj = {
        'id':3,
    }
    x = requests.delete(url, json = myobj)
    print(x.text)

test_delete_book()