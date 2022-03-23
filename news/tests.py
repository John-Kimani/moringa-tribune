from django.test import TestCase

# Create your tests here.
from .models import Editor, Article, tags


class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.kimani = Editor(first_name='Kimani', last_name='John', email='Kim@john.com')
    
    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kimani, Editor))
