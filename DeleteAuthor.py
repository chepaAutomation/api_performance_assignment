import random

from locust import TaskSet, HttpUser, task, between


class DeleteAuthorAPICall(TaskSet):
    @task(1)
    def delete_author(self):
        print("--> Performing an API Call to delete the author")
        headers = {
            "accept": "*/*"
        }
        inputnum = random.randint(1, 10000)
        with self.client.delete(
                url="/api/v1/Authors/"+str(inputnum),
                headers=headers,
                catch_response=True,
                name="Delete_Author"
        ) as response:
            if response.status_code != 200:
                response.failure(
                    "Return status code:" + str(response.status_code) + "Return response : " + str(response.content))
            else:
                response.success()


class AuthorsAPI(HttpUser):
    host = "https://fakerestapi.azurewebsites.net"
    tasks = [DeleteAuthorAPICall]
    wait_time = between(0.00001, 0.0004)
