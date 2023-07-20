# class Backpack:
#
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __str__(self):
#         return "Backpack: " + ", ".join(self.content)
#
#     def __eq__(self, other):
#         return self.content == other.content
#
#
# my_backpack = Backpack(gift="бутерброд")
# my_son_backpack = Backpack(gift="бутерброд")
#
# if Backpack.__eq__(self=my_backpack, other=my_son_backpack):
#     print("Как мы похожи")


# class Backpack:
#
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __str__(self):
#         return "Backpack: " + ", ".join(self.content)
#
#     def __add__(self, other):
#         new_obj = Backpack()
#         new_obj.content.extend(self.content)
#         if isinstance(other, Backpack):
#             new_obj.content.extend(other.content)
#         else:
#             new_obj.content.extend(other)
#         return new_obj
#
#
# my_backpack = Backpack(gift="бутерброд")
# my_son_backpack = Backpack(gift="банан")
# new_backpack = my_backpack + ["чипсы", "кола"]
# print(new_backpack)

# class Bread:
#     def __str__(self):
#         return "Я хлеб"
#
#     def __add__(self, other):
#         return Sandwich(part1=self, part2=other)
#
#
# class Sausage:
#     def __str__(self):
#         return "Я колбаса"
#
#     def __add__(self, other):
#         return Sandwich(part1=self, part2=other)
#
#
# class Sandwich:
#
#     def __init__(self, part1, part2):
#         self.part1 = part1
#         self.part2 = part2
#
#     def __str__(self):
#         return "Я бутерброд, состою из: " + str(self.part1) + " и " + str(self.part2)
#
#
# borodinsky = Bread()
# salami = Sausage()
# result = borodinsky + salami
# print(result)


class Multyplier:

    def __init__(self, factor=2):
        self.factor = factor

    def __call__(self, *args):
        res = []
        for item in args:
            res.append(item * self.factor)
        return res


mult_by_27 = Multyplier(factor=27)
result = mult_by_27(1, 2, 3, 4)
print(result)