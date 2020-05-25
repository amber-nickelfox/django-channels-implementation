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
    It is good practice to use a common path prefix
    like /ws/ to distinguish WebSocket connections
    from ordinary HTTP connections because it will
    make deploying Channels to a production environment
    in certain configurations easier.It is good practice
    to use a common path prefix like /ws/ to distinguish
     WebSocket connections from ordinary HTTP connections
     because it will make deploying Channels to a production
     environment in certain configurations easier.
    :param request:
    :param room_name:
    :return:
    """
    return render(request, 'chatapp/room.html', {
        'room_name': room_name
    })
