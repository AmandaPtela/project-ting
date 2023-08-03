from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        value = self.queue[-1]
        # print('LISTA DE VALORES ANTES', self.queue, self.queue.index(value))

        del self.queue[self.queue.index(value)]
        # print('LISTA DE VALORES DEPOIS', self.queue, self.queue[-1])
        # self.queue[-1]
        return self.queue[0]

    def search(self, index):
        # print('VÁLIDO TEM QUE SER ENTRE', range(0, len(self.queue) - 1))
        # print(index)
        if index >= len(self.queue) or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
