import abc

class IHandler(abc.ABC):
    @abc.abstractmethod
    def setNext(handler):
        pass
    @abc.abstractmethod
    def handle(request):
        pass

class BaseHandler(IHandler):
    def __init__(self):
        self._task:IHandler = None

    def setNext(self, handler):
        if self._task is None:
            self._task = handler
        else:
            self._task.setNext(handler)
        return self

class WakeUp(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self):
        print("Wstaje")
        if self._task is None:
            return None
        return self._task

class WashUp(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self):
        print("Myje sie")
        if self._task is None:
            return None
        return self._task

class Eat(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self):
        print("Jem")
        if self._task is None:
            return None
        return self._task

class DressUp(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self):
        print("Ubieram się")
        if self._task is None:
            return None
        return self._task

class PackUp(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self):
        print("Pakuje się")
        if self._task is None:
            return None
        return self._task

class Iron(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self):
        print("Prasuje")
        if self._task is None:
            return None
        return self._task

if __name__ == "__main__":
    h1 = WakeUp().setNext(WashUp()).setNext(Eat()).setNext(DressUp().setNext(Iron())).setNext(PackUp())

    while h1:
        h1 = h1.handle()