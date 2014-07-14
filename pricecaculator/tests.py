from django.test import TestCase
from pricecaculator.models import Usage, Use

# Create your tests here.


class UsageTestCase(TestCase):
    def test__str(self):

        usage = Usage(name="Newspaper")

        self.assertEquals(str(usage), 'Newspaper')


class UseTestCase(TestCase):
    def test__str(self):

        use = Use(name="Newspaper")

        self.assertEquals(str(use), 'Newspaper')







