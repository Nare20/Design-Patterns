class Worker:
    def work(self):
        print("Worker is working")

    def eat(self):
        print("Worker is eating")


class HumanWorker(Worker):
    pass


class RobotWorker(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise Exception("Robot does not eat")


human = HumanWorker()
robot = RobotWorker()

human.work()
human.eat()

robot.work()
robot.eat()
