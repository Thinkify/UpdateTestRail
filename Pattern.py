# coding: utf-8
# Author: Pavan Sreenivasa
# takes result file as input and returns 2 lists for failed and passed test cases.
import sys
import re


class Pattern:
    def __init__(self):
        self.failed = []
        self.passed = []
        self.filename = '$testresultfilepath'  #give your test result file path here.

    def get_pattern(self, flag=False):
        print("Getting patterns from result file......")
        with open(self.filename) as fp:
            lines = fp.readlines()
            ansi_escape = re.compile(
                r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            self.failed = [ansi_escape.sub('', line.partition("✗")[2].lstrip(
            ).rstrip()) for line in lines if re.search("✗", line)]
            self.passed = [ansi_escape.sub('', line.partition("✓")[2].lstrip(
            ).rstrip()) for line in lines if re.search("✓", line)]
        if flag:
            print("Failed cases = ", self.failed)
            print("Passed cases = ", self.passed)
            print("Failed cases count = ", len(self.failed))
            print("Passed cases count = ", len(self.passed))
        print("Done")
        return self.failed, self.passed


p = Pattern()
p.get_pattern(True)
