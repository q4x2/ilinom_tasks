import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_right(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def add_left(self, data):
        new_node = Node(data)
        curr = self.head
        self.head = new_node
        self.head.next = curr

    def remove(self, data):
        curr = self.head
        if curr.data == data:
            self.head = self.head.next
            return
        prev = curr
        curr = curr.next
        while curr:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

class Balancer:
    def __init__(self, id, load, stamp):
        self.id = id
        self.current_load = 0
        self.loads = LinkedList()
        
class LoadBalancers:
    def __init__(self, balancers_list):
        self.balancers = []
        for id in balancers_list:
            self.balancers.append(Balancer(id, 0, 0))
    
    def calculate_current_load(self, ts):
        for balancer in self.balancers:
            curr = balancer.loads.head
            balancer.current_load = 0
            while curr:
                if curr.data['stamp'] < ts and curr.data['stamp'] > 0:
                    balancer.loads.remove(curr.data)
                else:
                    balancer.current_load += curr.data['load']
                curr = curr.next
    
    def get_min_load(self, ts) -> Balancer:
        self.calculate_current_load(ts)
        min = self.balancers[0].current_load
        balancer_ret = self.balancers[0]
        for balancer in self.balancers:
            if balancer.current_load < min:
                balancer_ret = balancer
                min = balancer.current_load
        return balancer_ret

    def route(self, load, duration) -> Balancer:
        ts = time.time() * 1000
        new_stamp = ts + duration
        balancer = self.get_min_load(ts)
        balancer.loads.add_left({'load': load, 'stamp': new_stamp})
        balancer.current_load += load
        return balancer

    def __str__(self):
        str_rpr = ''
        for balancer in self.balancers:
            str_rpr += str(balancer.id) + str(balancer.current_load) + '\n'
        return str_rpr
