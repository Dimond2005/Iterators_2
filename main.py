nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None], [56, 4, 'Over']
]


class FlatIterator:
    def __init__(self, input_list):
        self.main_list = input_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.interior_list_cursor = -1
        return self

    def __next__(self):
        self.interior_list_cursor += 1
        self.interior_list = self.main_list[self.main_list_cursor]

        if self.interior_list_cursor == len(self.interior_list):
            self.interior_list_cursor = 0
            self.main_list_cursor += 1

        if self.main_list_cursor == len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.interior_list_cursor]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def generator(imput_list):
    for value in imput_list:
        for element in value:
            yield element


print()
for element in generator(nested_list):
    print(f'Сгенерировано ', element)
