class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.list_len = len(self.list)-1

    def __iter__(self):
        self.list_cursor = 0
        self.item_cursor = -1
        return self

    def __next__(self):
        self.item_cursor += 1
        if self.item_cursor > len(self.list[self.list_cursor])-1:
            if self.list_cursor == self.list_len:
                raise StopIteration
            else:
                self.list_cursor += 1
                self.counter = 0
        item = self.list[self.list_cursor][self.counter]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()