import tornado.ioloop
import tornado.web
import tornado.websocket
import asyncio
import json
import functools
import uuid

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def singleton(cls):
	instances = {}
	@functools.wraps(cls)
	def get_instance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return get_instance


@singleton
class MessagesBuffer():

	def __init__(self):
		from collections import deque
		self.__messages = deque(maxlen=50)


	def add_message(self, message):
		self.__messages.append(message)


	def get_messages(self):
		return self.__messages

globalmessagebuffer = MessagesBuffer()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class EchoWebSocketHandler(tornado.websocket.WebSocketHandler): 
    def open(self):
        print('socket was open')
        if globalmessagebuffer.get_messages():
            for each in globalmessagebuffer.get_messages():
                self.write_message(f'{each["sender_name"]}: {each["sender_message"]}\n')


    def on_message(self, message):
        id = uuid.uuid4()
        msg = json.loads(message)
        msg['id'] = id.hex
        self.write_message(f'{msg["sender_name"]}: {msg["sender_message"]}\n')
        globalmessagebuffer.add_message(msg)
        # print(msg, type(msg))
        print(globalmessagebuffer.get_messages())


    def on_close(self):
        print('socket was closed')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", IndexHandler),
        (r"/websocket", EchoWebSocketHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
