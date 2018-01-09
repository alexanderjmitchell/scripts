class Category(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


food_shopping = Category("Food Shopping")


class SubCategory(object):
    def __init__(self, description_regex, category):
        self.description_regex = description_regex
        self.category = category


waitrose = SubCategory(r'waitrose', food_shopping)

all_subcategories = [
    waitrose
]
