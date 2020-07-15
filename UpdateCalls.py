# Author: Pavan Sreenivasa
from testrail import *
import os


class UpdateCalls:
    def __init__(self, client_id, user, password):
        self.client = APIClient(str(client_id))
        self.client.user = str(user)
        self.client.password = str(password)

    def get_test_cases(self, test_run):
        case = []
        try:
            case = self.client.send_get('get_tests/'+str(test_run))
        except Exception as e:
            print(
                "Cannot fetch test cases under the specified suit!   " + str(test_run) +
                "    Causes - " + str(e))
            os._exit(1)
        finally:
            return case

    def update_test_result(self, test_id, flag):
        case = []
        if flag:
            status_id = 1
            comment = "This test worked fine!"
        else:
            status_id = 4
            comment = "This test Failed!"

        try:
            case = self.client.send_post(
                'add_result/'+str(test_id), {'status_id': status_id, 'comment': comment})
        except Exception,e:
            print("Improper data to update, Causes - " + str(e))
            os._exit(1)
        finally:
            return case

    def update_test_results_bulk(self, test_id, data):
        case = []
        try:
            case = self.client.send_post('add_results/'+str(test_id), data)
        except Exception, e:
            print(
                "Cannot bulk update data! Causes - " + str(e))
            os._exit(1)
        finally:
            return case

