from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from polls.models import Question, Choice
from django.utils.timezone import now
import time

class VoteLevelTest(LiveServerTestCase):  
    def setUp(self):
        self.browser = webdriver.Chrome()  


        self.question1 = Question.objects.create(question_text="Test Question 1", pub_date=now())
        self.question2 = Question.objects.create(question_text="Test Question 2", pub_date=now())
        Choice.objects.create(question=self.question1, choice_text="Choice 1", votes=15)  # "warm"
        Choice.objects.create(question=self.question2, choice_text="Choice 2", votes=55)  # "hot"

    def tearDown(self):
        self.browser.quit()

    def test_vote_level_display(self):
        """ Test that the vote level page displays the correct vote links. """
        self.browser.get(f"{self.live_server_url}/polls/list")

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )


        page_text = self.browser.page_source
        self.assertIn("This is Vote Level", page_text)
        self.assertIn("Test Question 1", page_text)
        self.assertIn("Test Question 2", page_text)

        list_items = self.browser.find_elements(By.TAG_NAME, "li")
        warm_found = False
        hot_found = False

        for item in list_items:
            text = item.text
            if "warm" in text and "Test Question 1" in text:
                warm_found = True
            if "Hot" in text and "Test Question 2" in text:
                hot_found = True

        self.assertTrue(warm_found, "Warm link not found for Test Question 1")
        self.assertTrue(hot_found, "Hot link not found for Test Question 2")
        time.sleep(3)
       
        warm_link = self.browser.find_element(By.LINK_TEXT, "warm")
        warm_link.click()
        time.sleep()
     
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        

        self.assertIn("Vote", self.browser.page_source)
