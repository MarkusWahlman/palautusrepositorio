from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, stack=All()):
        self._class_stack = stack

    def plays_in(self, team):
        return QueryBuilder(And(self._class_stack, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._class_stack, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._class_stack, HasFewerThan(value, attr)))

    def one_of(self, *queries):
        return QueryBuilder(Or(*queries))

    def build(self):
        return self._class_stack