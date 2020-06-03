class TestMul():
    def test_99mul(self):
        for i in range(1,10):
            for j in  range(1, i+1):
                result = i * j
                print('{} * {} = {}\t'.format(j, i, result), end='')
            print()