from django.test import TestCase
import datetime as dt

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
        '''
        Defines a new editor and tag instance
        '''
        self.kimani = Editor(first_name='Kimani', last_name='John', email='Kim@john.com')
        self.kimani.save_editor()


        # creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        
        self.new_article = Article(title='Hello Django', post='Django is backend framework for perfection developers having minimal time', editor= self.kimani)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        '''
        Test case for a news article
        '''
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)> 0)

    def test_get_news_by_date(self):
        '''
        Test case for date filer
        '''
        test_date = '2019-03-23'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
