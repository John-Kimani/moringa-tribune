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
    
    # testing the save method
    def test_save_method(self):
        self.kimani.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):
    '''
    Test class for article model
    '''

    #setUp method
    def setUp(self):
        self.hello_django = Article(title='Hello Django', post='Django is backend framework for perfection developers having minimal time')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.hello_django, Article))

