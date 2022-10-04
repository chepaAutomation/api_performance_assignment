import random

from locust import TaskSet, HttpUser, task, between


class GetAuthorByIdAPICall(TaskSet):
    @task(1)
    def get_authors_by_authorId(self):
        print("--> Performing an API Call to get author details by Author Id")
        headers = {
            "accept": "text/plain; v=1.0"
        }
        inputnum = random.randint(1, 100)
        with self.client.get(
                url="/api/v1/Authors/"+str(inputnum),
                headers=headers,
                catch_response=True,
                name="Get_Authors_By_Author_Id"
        ) as response:
            if response.status_code != 200:
                response.failure(
                    "Return status code:" + str(response.status_code) + "Return response : " + str(response.content))
            else:
                response.success()


class AuthorsAPI(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = [GetAuthorByIdAPICall]
    wait_time = between(0.00001, 0.0004)
