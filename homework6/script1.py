import time

class TrafficLight:
    __color = ['red', 'yellow', 'green']
    mode = {__color[0]: 7, __color[1]: 2, __color[2]: 5}


    def running(self):
        for key, val in self.mode.items():
            print(f'Color: {key}, Time: {val} s')
            time.sleep(val)

tl = TrafficLight()
tl.running()
