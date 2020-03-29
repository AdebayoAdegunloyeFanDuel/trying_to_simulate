import simpy
import random


class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, customer):
        yield self.env.timeout(random.randint(1, 3))

    def check_ticket(self, customer):
        yield self.env.timeout(3 / 60)

    def sell_food(self, customer):
        yield self.env.timeout(random.randint(1, 5))