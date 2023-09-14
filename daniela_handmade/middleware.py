from django.core.mail import mail_admins

class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Send an email to ADMINS when an exception occurs
        subject = f"Error on {request.path_info}"
        message = f"Error occurred in request:\n{request}\n\nException:\n{exception}"
        mail_admins(subject, message)