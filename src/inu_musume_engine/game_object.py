import abc


class GameObject(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def ready(self) -> None:
        pass

    @abc.abstractmethod
    def process(self, dt: float) -> None:
        pass
