# Author: Pavan Sreenivasa
from UpdateCalls import *
import re


class UpdateTestRail:
    def __init__(self, failed_test, passed_test, suit_id, client_id, user, password):
        self.failed_test = failed_test
        self.passed_test = passed_test
        self.manage_cases = UpdateCalls(client_id, user, password)
        self.suit_id = suit_id
        self.passed_test_id = []
        self.failed_test_id = []
        self.test_cases = []

    def get_tests(self, suit_id=None, flag=False,):
        if suit_id is None:
            suit_id = self.suit_id
        print("Getting test cases for the suite.....")
        self.test_cases = self.manage_cases.get_test_cases(
            suit_id)  # suite ID
        print("Done")
        if flag:
            for dict in self.test_cases:
                print(dict["id"], dict["title"])
        return self.test_cases

    def get_test_id(self, pattern, result=[]):

        if len(result) == 0:
            result = self.get_tests()
        for dict in result:
            if re.search(pattern, dict["title"], re.IGNORECASE):
                print(dict["id"], dict["title"])
                return dict["id"]

    def fetch_id_worker(self, passed_list=[], failed_list=[]):
        self.get_tests()
        if len(passed_list) == 0 and len(failed_list) == 0:
            passed_list = self.passed_test
            failed_list = self.failed_test
        self.passed_test_id = [self.get_test_id(
            str(i), self.test_cases) for i in passed_list]
        self.failed_test_id = [self.get_test_id(
            str(j), self.test_cases) for j in failed_list]
        return "Passed = "+str(self.passed_test_id), "Failed = "+str(self.failed_test_id)

    def update_worker(self):
        self.fetch_id_worker()
        for i in self.passed_test_id:
            self.manage_cases.update_test_result(i, True)
        for i in self.failed_test_id:
            self.manage_cases.update_test_result(i, False)

    def update_worker_bulk(self):
        print("Adding test results......")
        self.fetch_id_worker()
        results = []
        for i in self.passed_test_id:
            results.append({
                "test_id": i,
                "status_id": 1,
                "comment": "This test case worked fine"
            })
        for i in self.failed_test_id:
            results.append({
                "test_id": i,
                "status_id": 5,
                "comment": "This test case failed"
            })
        resultDict = {"results": results}
        self.manage_cases.update_test_results_bulk(self.suit_id, resultDict)
        print("Done")
