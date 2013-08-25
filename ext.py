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
