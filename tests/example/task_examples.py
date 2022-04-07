#################
# Example Tasks #
#################
from prefect import Task


class Extract(Task):
    def run(self):
        return 10


class Transform(Task):
    def run(self, x):
        return x + 10


class Load(Task):
    def run(self, y):
        print(y)
