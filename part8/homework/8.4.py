# coding:utf-8


def card_generator():
    nums = 52
    flowers = ('♠', '♥', '♣', '♦')
    values = ('2', '3', '4', '5',
              '6', '7', '8', '9',
              '10', 'J', 'Q', 'K', 'A')
    for i in range(nums):
        yield flowers[i // 13] + values[i % 13]


if __name__ == '__main__':
    cg = card_generator()
    print(next(cg))
    print(next(cg))
    for el in cg:
        print(el, end=' ')

