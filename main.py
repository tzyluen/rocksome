from core.checklist import *
from core.waiver import *
from ext import *
from utils import *

########################################################################
### initialization:
### (1)read rocksome configuration
###
from ConfigParser import SafeConfigParser
import glob

parser = SafeConfigParser()
parser.read("rocksome.cnf")
CHECKLIST_PATH = parser.get("rocksome_cnf", "checklist_path")
DBHOST = parser.get("rocksome_cnf", "dbhost")
DATABASE = parser.get("rocksome_cnf", "database")
USERNAME = parser.get("rocksome_cnf", "username")
PASSWORD = parser.get("rocksome_cnf", "password")
########################################################################

print "-I- CONFIGURATION"
print "-I-", CHECKLIST_PATH, DBHOST, DATABASE, USERNAME, PASSWORD
print "-I-"

socItem = SoCItem(1.1, "Rule name 1.1", "/path/to/src", "sd0p7", "csme")
print socItem

waiver = Waiver(socItem, "tng8", "justification...")
socItem.waive(waiver)
print socItem

socItem.unwaive()
print socItem

Checklist.locate(1.1, CHECKLIST_PATH)

# scenario 1:


# scenario 2:
# check entire milestone
# + (1) project
# + (2) IP/Partition
# + (3) List of items to check
# + (4_ With the exception on waived items
#automator = Automator()
