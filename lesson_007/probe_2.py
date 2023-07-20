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


class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __str__(self):
        return "Backpack: " + ", ".join(self.content)

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        if isinstance(other, Backpack):
            new_obj.content.extend(other.content)
        else:
            new_obj.content.extend(other)
        return new_obj


my_backpack = Backpack(gift="бутерброд")
my_son_backpack = Backpack(gift="банан")
new_backpack = my_backpack + ["чипсы", "кола"]
print(new_backpack)