import json
import random

from locust import TaskSet, HttpUser, task, between


class CreateAuthorsAPICall(TaskSet):
    @task(1)
    def create_authors(self):
        print("--> Performing an API Call to Post Authors")
        headers = {
            "accept": "text/plain; v=1.0",
            "Content-Type": "application/json; v=1.0"
        }
        inputnum = random.randint(1000, 10000)
        print("   ===> Creating author with Id : ", inputnum)
        payload = {"id": inputnum, "idBook": inputnum, "firstName": "FirstName " + str(inputnum), "lastName": "LastName " + str(inputnum)}
        print('input payload is : ', payload)
        with self.client.post(
                url="/api/v1/Authors",
                headers=headers,
                data=json.dumps(payload),
                catch_response=True,
                name="Post_Authors_Detail"
        ) as response:
            if response.status_code != 200:
                response.failure(
                    "Return status code:" + str(response.status_code) + "Return response : " + str(response.content))
            else:
                response.success()


class AuthorsAPI(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = [CreateAuthorsAPICall]
    wait_time = between(0.00001, 0.0004)
