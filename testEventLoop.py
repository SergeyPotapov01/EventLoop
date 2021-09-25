import threading


class EventLoop:
    def __init__(self):
        self.events = []

    def sendEvent(self, Event):
        self.events.append(Event)

    def check(self):
        if self.events:
            x = self.events
            self.events = []
            return x
        return []

    def listen(self):
        while True:
            for event in self.check():
                yield event


eventLoop = EventLoop()


def spam():
    for event in eventLoop.listen():
        print('\n', event, 'тут можно написать ветвление для обработки команды поступившей от функции sendComand')


threading.Thread(target=spam).start()


while 1:
    eventLoop.sendEvent(input('тут вводится какая нить команда'))