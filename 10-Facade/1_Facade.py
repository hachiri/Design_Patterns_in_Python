class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * self.width * self.height

    def __getitem__(self, index):
        return self.buffer.__getitem__(index)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_chat_at(self, index):
        return self.buffer[self.offset + index]

    def append(self, text):
        self.buffer.write(text)


class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.append(text)

    def get_chat_at(self, index):
        return self.current_viewport.get_chat_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('hello')
    print(c.get_chat_at(-1))