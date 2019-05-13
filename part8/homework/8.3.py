# coding: utf-8


class Sums:
    def __init__(self, len):
        self.current_index = 1
        self.current_value = 0
        self.__len = len

    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        self.current_value += self.current_index
        self.current_index += 1
        self.__len -= 1
        return self.current_value

    def __iter__(self):
        return self


if __name__ == '__main__':
    sum = Sums(10)
    print(next(sum))
    for el in sum:
        print(el, end=' ')
