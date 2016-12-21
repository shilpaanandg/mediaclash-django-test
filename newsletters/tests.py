from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from newsletters.mixins import NewsletterSubscriberMixin

class NewsletterSubscriberTestCase(TestCase):
    '''
    Tests signup_newsletter mixin
    '''

    class DummyView(NewsletterSubscriberMixin):
        '''
        To test signup_newsletter we need validated form data
        '''
        pass
        
    def setUp(self):

        super(NewsletterSubscriberTestCase, self).setUp()
        self.view = self.DummyView()

    def test_with_subscription_enabled(self):

        # Prepare initial params
        subscribe = True
        email_id = 'abc@pqr.com'
        name = 'abc'
        # Launch Mixin's get_context_data
        is_subscribed = self.view.signup_newsletter(subscribe,email_id, name)
        print "Test with subscription enabled"
        # Your checkings here
        self.assertTrue(is_subscribed)

    def test_with_subscription_disabled(self):

        # Prepare initial params
        subscribe = False
        email_id = 'abc@pqr.com'
        name = 'abc'
        # Launch Mixin's get_context_data
        is_subscribed = self.view.signup_newsletter(subscribe,email_id, name)
        print "Test with subscription disabled"
        # Your checkings here
        self.assertFalse(is_subscribed)  