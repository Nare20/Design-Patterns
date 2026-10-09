class Workable:
    def work(self):
        print("Worker is working")


class Eatable:
    def eat(self):
        print("Worker is eating")


class HumanWorker(Workable, Eatable):
    pass


class RobotWorker(Workable):
    def work(self):
        print("Robot is working")


human = HumanWorker()
robot = RobotWorker()

human.work()
human.eat()

robot.work()
