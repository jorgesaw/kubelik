"""Contacts views."""

# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Models
from apps.contacts.forms import ContactForm

# Utils
from apps.utils.mail import SimpleEmailThread 


class ContactView(SuccessMessageMixin, FormView):
	"""Contact view."""

	form_class = ContactForm
	template_name = 'contacts/contact.html'
	success_url = reverse_lazy('contacts:contact')
	success_message = 'Mensaje enviado exitosamente. Pronto nos comunicaremos con usted.'


	def form_valid(self, form):
		"""This method is called when valid form data has been POSTed.
		It should return an HttpResponse.
		
		"""
		self.send_email(form.cleaned_data)
		return super().form_valid(form)
		

	def get_context_data(self, **kwargs):
		"""Add custom title page."""

		context = super().get_context_data(**kwargs)
		context['title'] = 'Contacto'
		return context

	def send_email(self, valid_data):
		subject = 'Kubelik: Nuevo mensaje de contacto'
		body = 'De {} {} <{}>\n\nEscribió:\n\n{}'.format(
				valid_data.get('first_name'), 
				valid_data.get('last_name'), 
				valid_data.get('email'),
				valid_data.get('message'),
			)
		from_email = 'no-reply@gmail.com'
		recipient_list = ['jorgesaw@gmail.com',] # dest_email
		reply_to = [valid_data.get('email'),]
		#send_mail(subject, content, from_email, recipient_list, reply_to)
		SimpleEmailThread(
        	subject, body, from_email, recipient_list, reply_to
    	).start()  	 
		"""
		email = EmailMessage(
			'Kubelik: Nuevo mensaje de contacto', # subject
			'De {} {} <{}>\n\nEscribió:\n\n{}'.format(
				valid_data.get('first_name'), 
				valid_data.get('last_name'), 
				valid_data.get('email'),
				valid_data.get('message'),
			), # body 
			'no-contestar@gmail.com', # from_email
			['jorgesaw@gmail.com',], # dest_email
			reply_to = [valid_data.get('email'),]
		)
		try:
			email.send()
		except:
			pass # return redirect(reverse_lazy('contacts:contact') + '?fail')
		"""