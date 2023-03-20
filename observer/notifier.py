'''
    Observer pattern is used to observe for any messages from the publishers 
    and notify the subscribers regarding the message.
    
    Alternatively it is also called as pub/sub pattern.
'''

from abc import ABC, abstractmethod


class Channel:
    '''
        publisher class, maintains list of subscribers, 
        notifies subscribers when a new article is published
    '''
    
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = []
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.notify(self.name, message)


class Subscriber(ABC):
    '''Subscriber base class'''
    @abstractmethod
    def notify(self, message):
        pass


class PaidSubscriber(Subscriber):
    def __init__(self, name) -> None:
        self.name = name
    
    def notify(self, channel, message):
        print(f'Hi {self.name}, a new message from {channel}: {message}')
    

def main():
    data_science_channel = Channel('DataScience')
    
    sub_1 = PaidSubscriber('sub_1')
    sub_2 = PaidSubscriber('sub_2')
    sub_3 = PaidSubscriber('sub_3')

    data_science_channel.subscribe(sub_1)
    data_science_channel.subscribe(sub_2)
    data_science_channel.subscribe(sub_3)

    data_science_channel.notify('New video released on PCA!')


if __name__ == '__main__':
    main()
