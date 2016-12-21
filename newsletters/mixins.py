from .utils import signup_newsletter

class NewsletterSubscriberMixin(object):
    """
    View mixin which requires boolean subscribe, email id, name of user.
    """
    def signup_newsletter(self,subscribe,email,name):
        print "mixin called"
        is_subscribed=False
        if subscribe:
            signup_newsletter(email,name)
            is_subscribed=True
        return is_subscribed


