class Math:
    def __init__(self):
        pass

    def addiction(self, num_a, num_b):
        return num_a + num_b

    def substaction(self, num_a, num_b):
        return num_a - num_b

    def multiplication(self, num_a, num_b):
        return num_a * num_b

    def division(self, num_a, num_b):
        return num_a / num_b

math = Math()

add = math.addiction(num_a=223, num_b=94)
print(add)

sub = math.substaction(num_a=1092, num_b=937)
print(sub)

mult = math.multiplication(num_a=15, num_b=78)
print(mult)

div = math.division(num_a=298, num_b=156)
print(div)

