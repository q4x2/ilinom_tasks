from collections import defaultdict
import string
import time


class LoadBalancers:
    
    def __init__(self, balancers_list):
        self.balancers_dict = defaultdict(lambda: defaultdict(int))
        for balancer in balancers_list:
            self.balancers_dict[balancer]['stamp'] = 0
            self.balancers_dict[balancer]['load'] = 0
    
    def route(self, load, duration) -> string:
        ts = time.time() * 1000
        new_stamp = ts + duration
        sorted_balancers = sorted(self.balancers_dict.items(), key=lambda y: y[1]['stamp'])
        for balancer in sorted_balancers:
            if balancer[1]['stamp'] < ts:
                self.balancers_dict[balancer[0]]['load'] = load
                self.balancers_dict[balancer[0]]['stamp'] = new_stamp
                return balancer[0]
        sorted_balancers = sorted(self.balancers_dict.items(), key=lambda y: y[1]['load'])
        self.balancers_dict[sorted_balancers[0][0]]['load'] += load
        self.balancers_dict[sorted_balancers[0][0]]['stamp'] = new_stamp
        return sorted_balancers[0][0]
    
    def __str__(self):
        str_dict = ''
        for balancer in self.balancers_dict.items():
            str_dict += str(balancer) + '\n'
        return str_dict
