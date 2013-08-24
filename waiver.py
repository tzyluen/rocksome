from datetime import date

class Waiver:
    def __init__(self, item, owner, justification="", date = date.today()):
        self.item  = item
        self.owner = owner
        self.justification = justification
        self.date = date
        self.approved = False
    def __str__(self):
        return "Waiver(%s %s %s %s)" % (self.owner, self.justification,
                                        self.date, self.approved)
