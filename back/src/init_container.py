from dependency_injector import containers, providers

from back.src.services.message_service import MessageService


def init_container(settings):
    class Container(containers.DeclarativeContainer):
        @staticmethod
        def init_service(service_type):
            service = providers.Factory(
                service_type,
            )
            return service

        message_service = init_service(service_type=MessageService)

    return Container()