"""Email utils."""

# Python
import threading

# Django
from django.core.mail import EmailMessage


class SimpleEmailThread(threading.Thread):
	"""Simple email thread.

	Send email in another thread is not main.
	"""

	def __init__(self, subject, body, from_email, recipient_list, reply_to):
		self.subject = subject
		self.body = body
		self.recipient_list = recipient_list
		self.from_email = from_email
		self.reply_to = reply_to
		threading.Thread.__init__(self)
		
	def run(self):
		email = EmailMessage(
			self.subject, # subject
			self.body, # body
			self.recipient_list, # from_email
			self.recipient_list, # dest_email
			self.reply_to
		)
		try:
			email.send()
		except:
			pass # return redirect(reverse_lazy('contacts:contact') + '?fail')