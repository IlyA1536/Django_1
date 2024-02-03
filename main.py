import django_setup

from django_orm.models import User, Task


def inserts():
    user1 = User(
        login = "Admin1",
        email = "idhbfisdhf@gmail.com",
        role = "AD"
    )
    user1.save()
    
    user2 = User(
        login = "dsiojnsdg",
        email = "fsghtdf@gmail.com",
        role = "US"
    )
    user2.save()

    task1 = Task(
        title = "Cooking",
        description = "Need a cook steak"
    )
    task1.save()


def connections():
    user1 = User.objects.get(id=1)
    task1 = Task.objects.get(id=1)
    user1.task.add(task1)

    user2 = User.objects.get(id=2)
    task2 = Task.objects.get(id=1)
    user2.task.add(task2)


def main():
    connections()

if __name__ == "__main__":
    main()
