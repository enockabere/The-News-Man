import unittest
from app.models import Articles

class news_sourceTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_source Class
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_article = Articles("Nairobi News","Kenya: DJ Shitti's Beef With TV Producers","Omosh finally receives camera, tripod & microphone from singer B-Classic (Photos)pulselive.co.ke","https://allafrica.com/stories/202107210410.html","https://cdn08.allafrica.com/static/images/structure/aa-logo-rgba-no-text-square.png","2021-07-21T10:30:32Z","Comedian Steven Oduor Dede, popularly known as DJ Shitti, has hit out at TV producers in the mainstream media, describing them as 'mediocre', while even suggesting, without backing up his claims, tha… [+1314 chars]")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
