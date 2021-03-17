from time import sleep


class TrafficLight:
    def __init__(self):
        self.color = 'красный'

    def running(self):
        ord= [('красный', 7),
              ('желтый', 2),
              ('зеленый', 15),
              ('желтый', 2)
        ]
        for i in ord:
            print(i[0])
            sleep(i[1])


tr = TrafficLight()

tr.running()