from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (http -> django views added by default)
})

