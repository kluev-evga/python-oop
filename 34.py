class Point:
    title = 'title'
    odering = 'ordering'

    def __init__(self, psw):
        self.psw = psw
        self.Meta = self.Meta('asdf')

    class Meta:
        ordering = ['id']
        t = Point.title

    def __init__(self, access):
        self.access = access

Point.ordering
Point.Meta.ordering

p = Point('123')
p.ordering
p.Meta.ordering
p.__dict__
p.Meta.__dict__
