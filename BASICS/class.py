class Car:
    runs=True

    def start(self):
        if self.runs:
            print("Car is started.Vroom Vroom!")
        else:
            print("Car is broken:(")

my_car=Car()
my_car.runs=False
print(f"My car runs: {my_car.runs}")
my_car.start()

my_other_car=Car()
my_other_car.start()