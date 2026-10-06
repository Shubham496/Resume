from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Skill, Experience, Education


class PortfolioViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        Skill.objects.create(name='Python', category='Backend', level=90, order=1)
        Experience.objects.create(
            title='Software Engineer',
            company='Tech Corp',
            start_date='2023-01-01',
            description='Building web applications.'
        )
        Education.objects.create(
            degree='B.S. Computer Science',
            institution='University',
            year_end=2022
        )

    def test_landing_page_status(self):
        response = self.client.get(reverse('portfolio:landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Stock Analysis')
        self.assertContains(response, 'ML Demo')

    def test_resume_page_status(self):
        response = self.client.get(reverse('portfolio:resume'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')
        self.assertContains(response, 'Software Engineer')

    def test_contact_page_status(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)

    def test_stock_analysis_pages(self):
        response = self.client.get(reverse('stock_analysis:index'))
        self.assertEqual(response.status_code, 200)

        response_detail = self.client.get(reverse('stock_analysis:detail', kwargs={'ticker': 'AAPL'}))
        self.assertEqual(response_detail.status_code, 200)

    def test_ml_demo_page(self):
        response = self.client.get(reverse('ml_demo:index'))
        self.assertEqual(response.status_code, 200)
