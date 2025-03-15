from django.test import TestCase,Client
from . models import Question , Choice
from django.utils.timezone import now, timedelta
from . import views
# Create your tests here.

class vote_test(TestCase):
    def setUp(self):
        self.client = Client()
        self.question1 = Question.objects.create(question_text="testquestion1", pub_date=now(),private = True)
        self.question2 = Question.objects.create(question_text="testquestion2", pub_date=now(),private = False)
        
        self.choice1 = Choice.objects.create(question=self.question1, choice_text="Choice 1", votes=11)
        self.choice2 = Choice.objects.create(question=self.question2, choice_text="Choice 2", votes=51)


    def test_private(self):
        #เข้าหน้า private
        self.base_url = "/private/"
        #ดึงการตอบสนอง ของ web
        response = self.client.get(self.base_url)
        print(response)
        #ดึง context private list
        Q_ls = response.context["privatelist"]
        print("asdasd")
        ls = [e.question_text for e in Q_ls]
        #เช็คคำถามทดลองที่สร้างไว้
        self.assertIn("testquestion1",ls)
        
    def test_empty_private_list(self):
        #ลบ object ทั้งหมด
        Question.objects.all().delete()  
        response = self.client.get("/private/")
        
        self.assertEqual(response.status_code, 200)#ceheck status ของ template
        self.assertEqual(len(response.context["privatelist"]), 0)  