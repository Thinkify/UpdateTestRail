# Author - Pavan Sreenivasa
from UpdateTestRail import *
from Pattern import *
import sys

if __name__ == "__main__":
    # logfile = sys.argv[1]
    # uname = sys.argv[2]
    # password = sys.argv[3]
    # suit_id = sys.argv[4]
    # logfile = sys.argv[5]
    # getPattern = Pattern(logfile)
    # passedlist, failedlist = getPattern.get_pattern()
    # print(passedlist, failedlist)
    passedlist = ['This is a sample test case']
    failedlist = ['Sample Test case 2']
    u = UpdateTestRail([], [], 851, '$testrailIP',
                       '$username', '$password')
    # a, b = u.fetch_id_worker()
    # u.update_worker_bulk()
    u.get_tests(870, True)
    #print(u.get_test_id('Sample'))
    # print(a, b)
