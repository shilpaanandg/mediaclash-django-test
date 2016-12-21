from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ExpressionOfInterestForm, ImNotInterestedForm
from newsletters.mixins import NewsletterSubscriberMixin

# Create your views here.

class ExpressYourInterestView(FormView,NewsletterSubscriberMixin):
	"""
	Users interested in our company can let us know here
	"""
	template_name = 'express_interest.html'
	form_class = ExpressionOfInterestForm
	success_url = '/thanks/'
	
	def form_valid(self, form):
		print 'Sending email to the admins'
		super(ExpressYourInterestView, self).signup_newsletter(form.cleaned_data['sign_up_to_newsletter'],
															   form.cleaned_data['email'],
															   form.cleaned_data['name']) #I have to call this method here because the form fields names are
																						   #different on both the forms. Otherwise I would have used in built mixins of django.
		return super(ExpressYourInterestView, self).form_valid(form)



class NotInterestedView(FormView,NewsletterSubscriberMixin):
	"""
	Those absolutely NOT interested can let us know as well
	"""

	template_name = 'not_interested.html'
	form_class = ImNotInterestedForm
	success_url = '/thanks/?but=not_interested'

	def form_valid(self, form):
		print "Letting those admins know"
		super(ExpressYourInterestView, self).signup_newsletter(form.cleaned_data['signup_for_spam_emails'],
															   form.cleaned_data['email_address'],
															   form.cleaned_data['first_name'])
		return super(NotInterestedView, self).form_valid(form)

class ThanksView(TemplateView):
	template_name = 'thanks.html'

	def get_context_data(self, **kwargs):
	    context = super(ThanksView, self).get_context_data(**kwargs)
	    if self.request.GET.get('but', None):
	    	context['fine_then'] = True
	    return context
		
		