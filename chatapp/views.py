from django.shortcuts import render


def index(request):
    """
    Index view
    :param request:
    :return:
    """
    return render(request, "chatapp/index.html")


def room(request, room_name):
    """
    Enter in room
    :param request:
    :param room_name:
    :return:
    """
    return render(request, 'chatapp/room.html', {
        'room_name': room_name
    })
