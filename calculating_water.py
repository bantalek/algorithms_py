# Uses python3

data = [1, 2, 1, 3, 4, 4, 5, 1, 2, 0, 3]



class Trapping_Water:
    # save reference to the container and the high point before starting solution
    # lets also establish the right and left segments of our container as well as our boundaries
    def __init__(self, a):
        self.container = a
        self.hp = a.index(max(a))

    def solve(self):
        c = self.container
        if len(c) <= 2:
            return 0
        # if there is a positive differece between the minimum of the left and right pointers and the container unit
        # that difference is the volume of water that single container unit can hold.
        
        volume = 0
        
        # solve for right segment
        r_max = 0
        for ht in reversed(c[self.hp:]):
            if ht <= r_max:
                volume += r_max - ht
            else:
                r_max = ht
        rv = volume
        print('right volume', rv)

        # solve for left segment
        l_max = 0
        for ht in c[:self.hp]:
            if ht <= l_max:
                volume += l_max - ht
            else:
                l_max = ht
        print('left volume', volume - rv)
        return volume


# TEST CASES

if __name__ == '__main__':
    def test_water_vol(test_case, data, exp):
        tp = Trapping_Water(data)
        r = tp.solve()
        print(r, r == exp)

    D1 = [1]
    test_water_vol(test_case='D1', data=D1, exp=0)

    D2 = [1, 2, 1, 3, 4, 4, 5, 1, 2, 0, 3]
    test_water_vol(test_case='D2', data=D2, exp=7)

    D3 = [1, 2, 3, 4, 3, 2, 1]
    test_water_vol(test_case='D3', data=D3, exp=0)

    D4 = [1, 0, 1, 0, 1, 0, 1, 0]
    test_water_vol(test_case='D4', data=D4, exp=3)