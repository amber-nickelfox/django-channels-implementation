from django.shortcuts import render


def index(request):
    """
    Index view
    :param request:
    :return:
    """
    return render(request, "chatapp/index.html")
