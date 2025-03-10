from django.test import TestCase,Client
from . models import Question , Choice
from django.utils.timezone import now, timedelta
# Create your tests here.

class vote_test(TestCase):
    def setUp(self):
        self.client = Client()
        self.question1 = Question.objects.create(question_text="testquestion1", pub_date=now())
        self.question2 = Question.objects.create(question_text="testquestion2", pub_date=now())
        
        self.choice1 = Choice.objects.create(question=self.question1, choice_text="Choice 1", votes=11)
        self.choice2 = Choice.objects.create(question=self.question2, choice_text="Choice 2", votes=51)

    def test_show_level(self):
        base_url = "/polls/list/"
        levels = []
        
        response = self.client.get(base_url)
        vote_ls = response.context["vote_ls"]
        question_ls = response.context["question_ls"]

        for question in question_ls:
            # print(question)
            # print('--------')
            total_votes = sum(choice.votes for choice in Choice.objects.filter(question=question))
            # print(total_votes)

            if 10 < total_votes < 50:
                levels.append({question.question_text: "warm"})
            elif total_votes > 50:
                levels.append({question.question_text: "hot"})

            # print(levels)

        for item in vote_ls:
            for key_res, value_res in item.items():  
                print(key_res, value_res)

                level_dict = {k: v for d in levels for k, v in d.items()} 
                print(level_dict) 

                self.assertIn(key_res, level_dict)
                self.assertEqual(value_res, level_dict[key_res])
