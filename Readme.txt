******Author - Pavan Sreenivasa *************
Automating updating of test result to testrail

Required data - 
clientID - This is your serverid in testrail. Example (https://<your-name>.testrail.com) or (https://<your-org>.testrail.com)
username - This is the email used to login to testrail. Example (your-name@your-org.com) or (your-name@server.com)
password - Password used to login to testrail
suit-id - This is the suit id given by testrail whenever a TESTPLAN and TESTRUN is created. Please go through the testrail documentation for TESTPLAN and TESTRUN
Result file - This file should contain the test results after running the tests on a cluster or local machine.

Required software -
Python 2.7 and above
sudo pip install requests

Methods you can use -
    get_Pattern from Pattern class
        arguments -  log file #preferebly .txt file
        eg:- pattern = Pattern(logfile path)
             pattern.getPattern()  ->  returns 2 lists for failed and passed cases
             pattern.getPattern(True)  -> #takes boolean parameter to print the passed and failed test cases list

    get_tests from UpdateTestRail class
        arguments -  suitId, flag ->(boolean value for printing just id and test case name)
        eg:- tests = UpdateTestRail([],[],suit_id, client_id, username,password)
             tests.get_tests(suit_id , flag) #both are optional parameters -> returns raw data from api for all test cases for the specified suit

    get_test_id() from UpdateTestRail class
        arguments -  failed_test_list , passed_test_list ,clientID, username, password
        eg:- get_id = UpdateTestRail([],[],suit_id, client_id,username,password) #lists can be empty as in the example if this method is called explicitly from main
             id = get_test_cases("Pattern for a test case")





Executing the script
    python2 main_module.py arg1 arg2 arg3 arg4 arg5

    where arg1 - clientID
          arg2 - username
          arg3 - password
          arg4 - suitId
          arg5 - results file path
