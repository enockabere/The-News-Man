import unittest
import news_source

News_source = news_source.News_Source

class news_sourceTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_source Class
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_source = News_source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general","en","au")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_source))
if __name__ == '__main__':
    unittest.main()    