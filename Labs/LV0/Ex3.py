import numpy as np


class Array:
    def __init__(self, shape):
        total = 1
        for dimension in shape:
            total *= dimension
        tmp_array = np.random.uniform(0, 5, total)
        self.array = tmp_array.reshape(shape)

    def compare_array(self, other: 'Array') -> bool:
        if self.array.shape != other.array.shape:
            return False
        all_elements = self.array.reshape(-1)
        average = sum(all_elements) / len(all_elements)
        bigger_than_average = [1 if x > average else 0 for x in other.array.reshape(-1)]
        num_elements_bigger_than_average = sum(bigger_than_average)
        return num_elements_bigger_than_average > (len(all_elements) - num_elements_bigger_than_average)

    def __str__(self):
        return self.array.__str__()




if __name__ == '__main__':
    array_1 = Array([2, 4])
    array_2 = Array([2, 4])
    print(array_1)
    print(array_2)
    print(array_1.compare_array(array_2))
