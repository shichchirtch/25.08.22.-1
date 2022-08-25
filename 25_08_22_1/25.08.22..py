import sys
class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if isinstance(record, Record):
            self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        # r  = ( x  for row in self.dict_db.values() for x in row)
        # obj = tuple(filter(lambda x: x.pk==pk, r))
        # return obj[0] if len(obj)>0 else None

        for x in self.dict_db.values():
            for y in x:
                if pk == y.pk :
                    return y
        return None

class Record:

    PK = 0
    def __init__(self, fio, descr, old: int):
        Record.PK += 1
        pk = Record.PK
        self.pk = pk
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return True if hash(self) == hash(other) else False


lst_in = list(map(str.strip, sys.stdin.readlines()))

db  = DataBase("way")
for x in lst_in:
    fio, descr, old = x.split(";")
    old = int(old)
    x = Record(fio, descr, old)
    db.write(x)




# Балакирев С.М.; программист; 33
# Кузнецов А.В.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 37
