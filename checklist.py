from waiver import Waiver

### Checklist container
class Checklist:
    def __init__(self, items):
        self.items = items
        self.index = len(items)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.items[self.index]
    @staticmethod
    def locate(itemId, CHECKLIST_PATH):
        print CHECKLIST_PATH 


### Base class of all items
class Item:
    def __init__(self, id, name, source):
        self.id = id
        self.name = name
        self.source = source
        self.waiver = None
    def waive(self, waiver):
        self.waiver = waiver
    def unwaive(self):
        self.waiver = None
    def run(self):
        # call the source and run it
        pass
    def __str__(self):
        return "Item(%s %s %s)" % (self.id, self.name, self.source)


### SoC item
class SoCItem(Item, object):
    def __init__(self, id, name, source, milestone, dut):
        super(SoCItem, self).__init__(id, name, source)
        self.milestone = milestone
        self.dut = dut
    def __str__(self):
        _str = "SoCItem(%d %s %s %s %s)" % (self.id, self.name, self.source,
                                            self.milestone, self.dut)
        if self.waiver is not None:
            print self.waiver
        return _str


### SD item
class SDItem(Item, object):
    def __init__(self, id, name, source, milestone, dut):
        super(SDItem, self).__init__(id, name, source)
        self.milestone = milestone
        self.dut = dut
    def __str__(self):
        pass

