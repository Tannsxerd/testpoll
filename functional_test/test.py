from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from polls.models import Question , Choice
from django.utils.timezone import now, timedelta
import time 

class usertest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        

    def tearDown(self):
        self.browser.quit()

    
    # def test_vote_level(self):
    #     self.question1 = Question.objects.create(question_text="testquestion1", pub_date=now(),private = True)
    #     self.choice1 = Choice.objects.create(question=self.question1, choice_text="Choice 1", votes=11)
        
    #     self.browser.get(f"{self.live_server_url}/polls/list/")
    
    #     self.assertIn("list",self.browser.title)

    #     text_in = self.browser.find_elements(By.TAG_NAME, "h1")
         
    #     print([e.text for e in text_in])
    #     self.assertIn("This is Vote Level",[e.text for e in text_in])
         
    #     q_in =  self.browser.find_elements(By.TAG_NAME, "li")
    #     self.assertIn('warm: testquestion',[e.text[:-1] for e in q_in])

    #     print([e.text for e in q_in])

    #     #click in warm it should bring too 
    #     warm_link = self.browser.find_elements(By.LINK_TEXT, "warm")
    #     print([e for e in warm_link])
        
    #     for e in warm_link:
    #         e.click()
    #         question_text =  self.browser.find_elements(By.TAG_NAME, "h1")
    #         self.assertIn("testquestion1",[e.text for e in question_text])
    #     time.sleep(4)


    #final test
    def test_private_page(self):
        self.question1 = Question.objects.create(question_text="testquestion1", pub_date=now(),private = True)
        self.choice1 = Choice.objects.create(question=self.question1, choice_text="Choice 1", votes=11)

        #open private  private page
        self.browser.get(f"{self.live_server_url}/private")
        q_in =  self.browser.find_elements(By.TAG_NAME, "a")
        self.assertIn("testquestion1",[e.text for e in q_in])
        time.sleep(4)
        