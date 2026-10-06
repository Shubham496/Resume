from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Skill, Experience, Education, Certification, Project


class PortfolioViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        Skill.objects.create(name='Power BI', category='Business Tools', order=1)
        Experience.objects.create(
            title='Data Analyst',
            company='LNP Infotech',
            start_date='2025-12-01',
            description='Financial analytics and reporting.'
        )
        Education.objects.create(
            degree='B.Tech in Electronics and Communication',
            institution='Rustamji Institute of Technology',
            year_end=2023
        )
        Certification.objects.create(
            title='Power BI Masterclass',
            issuer='Udemy',
            year=2024
        )
        self.project = Project.objects.create(
            title='Adidas Retail Dashboard',
            slug='adidas-retail-dashboard',
            project_type='powerbi',
            summary='Retail performance analytics',
            key_highlights='Integrated POS and ERP systems\nDAX YoY measures',
            order=1,
            is_featured=True
        )

    def test_landing_page_status(self):
        response = self.client.get(reverse('portfolio:landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Shubham Singh')
        self.assertContains(response, 'Adidas Retail Dashboard')

    def test_resume_page_status(self):
        response = self.client.get(reverse('portfolio:resume'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Power BI')
        self.assertContains(response, 'LNP Infotech')
        self.assertContains(response, 'Rustamji Institute of Technology')

    def test_projects_list_page(self):
        response = self.client.get(reverse('portfolio:projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Adidas Retail Dashboard')

        # Filter check
        response_filtered = self.client.get(reverse('portfolio:projects_list') + '?type=powerbi')
        self.assertEqual(response_filtered.status_code, 200)
        self.assertContains(response_filtered, 'Adidas Retail Dashboard')

    def test_project_detail_page(self):
        response = self.client.get(reverse('portfolio:project_detail', kwargs={'slug': self.project.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Adidas Retail Dashboard')
        self.assertContains(response, 'DAX YoY measures')

    def test_tableau_embed_snippet_is_converted_to_iframe_src(self):
        self.project.project_type = 'tableau'
        self.project.embed_url = """
        <div class='tableauPlaceholder'>
          <object class='tableauViz'>
            <param name='name' value='graphs_17913129898030&#47;rowchart' />
          </object>
        </div>
        """
        self.project.save()

        response = self.client.get(reverse('portfolio:project_detail', kwargs={'slug': self.project.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'src="https://public.tableau.com/views/graphs_17913129898030/rowchart?:showVizHome=no&amp;:embed=true"',
        )

    def test_iframe_embed_snippet_uses_its_src(self):
        self.project.embed_url = '<iframe src="https://example.com/embed/report"></iframe>'
        self.project.save()

        response = self.client.get(reverse('portfolio:project_detail', kwargs={'slug': self.project.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'src="https://example.com/embed/report"')

    def test_contact_page_status(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '9520132466')
