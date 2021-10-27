import time

class TrafficLight:
    _color = ['red', 'yellow', 'green']
    mode = {_color[0]: 7, _color[1]: 2, _color[2]: 5}


    def running(self):
        for key, val in self.mode.items():
            print(f'Color: {key}, Time: {val} s')
            time.sleep(val)

tl = TrafficLight()
tl.running()
