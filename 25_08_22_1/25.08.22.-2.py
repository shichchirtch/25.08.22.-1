class BookStudy:

    def __init__(self, name, author, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python2; Балакирев С.М.; 2021',
]
lst_bs = []
for x in lst_in:
    name, author, year = x.split("; ")
    s = BookStudy(name, author, int(year))
    lst_bs.append(s)

unique_books = len(set(lst_bs))

print(unique_books)


