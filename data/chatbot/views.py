from django.http import HttpResponse

from chatbot.models import Message


def index(request):
    """
    Index page.

    :param request: request
    :return: hello page.
    """
    return HttpResponse('Welcome to ChatBotXO!')


def get_message(request):
    """
    Return a random message from database.

    :param request: request
    :return Message: message
    """
    message = Message.get_random()
    return HttpResponse(message)
