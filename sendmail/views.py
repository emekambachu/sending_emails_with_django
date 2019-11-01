# import django settings
from django.conf import settings

# import for django mail
from django.core.mail import send_mail

# import generic class-based views
from django.views.generic import FormView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SendMailForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class SendMailView(FormView):
    template_name = 'send_mail.html'
    form_class = SendMailForm
    success_url = reverse_lazy('sendmail')

    def form_valid(self, form):

        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        # send email
        subject = subject
        html_message = render_to_string('mail_template.html', {
            'context': message,
            'email': email,
            'subject': subject
        })
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = email

        send_mail(subject, plain_message, from_email, [to, 'xeddtech@gmail.com'], html_message=html_message)

        return super(SendMailView, self).form_valid(form)

    # # display blank form
    # def get(self, request):
    #     form = self.form_class(None)
    #     return render(request, self.template_name, {'form': form})
    #
    # # process form data
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         contact_form = form.save(commit=False)
    #
    #         # if not using model forms or META, add object to form fields
    #         contact_form.subject = form.cleaned_data.get('subject')
    #         contact_form.email = form.cleaned_data.get('email')
    #         contact_form.message = form.cleaned_data.get('message')
    #
    #         # save form
    #         contact_form.save()
    #
    #         # send email
    #         subject = contact_form.subject
    #         html_message = render_to_string('mail_template.html', {
    #             'context': contact_form.message,
    #             'email': contact_form.email,
    #             'subject': subject
    #         })
    #         plain_message = strip_tags(html_message)
    #         from_email = settings.EMAIL_HOST_USER
    #         to = contact_form.email
    #
    #         send_mail(subject, plain_message, from_email, [to, 'xeddtech@gmail.com'], html_message=html_message)
    #
    #     return render(request, self.template_name, {'form': form})





