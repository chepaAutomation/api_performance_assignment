import json
import random

from locust import TaskSet, HttpUser, task, between


class UpdateAuthorsAPICall(TaskSet):
    @task(1)
    def update_authors(self):
        print("--> Performing an API Call to Update Authors")
        headers = {
            "accept": "text/plain; v=1.0",
            "Content-Type": "application/json; v=1.0"
        }
        inputnum = random.randint(1, 100)
        newnum = inputnum+1
        payload = {"id": inputnum, "idBook": newnum, "firstName": "FirstName " + str(newnum), "lastName": "LastName " + str(newnum)}
        print('input payload is : ', payload)
        with self.client.put(
                url="/api/v1/Authors/"+str(inputnum),
                headers=headers,
                data=json.dumps(payload),
                catch_response=True,
                name="Update_Authors_Detail"
        ) as response:
            if response.status_code != 200:
                response.failure(
                    "Return status code:" + str(response.status_code) + "Return response : " + str(response.content))
            else:
                response.success()


class AuthorsAPI(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = [UpdateAuthorsAPICall]
    wait_time = between(0.00001, 0.0004)
