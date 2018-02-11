from django.test import TestCase

# Create your tests here.
from landing_page.models import Projects


class projects(TestCase):
    def setUp(self):
        Projects.objects.create(title="lion")

    def test_projects(self):
        """Animals that can speak are correctly identified"""
        lion = Projects.objects.get(title="lion")
