"""
  ssq: A cashier with a random service time
  
  M/M/1 Queue with Poisson arrivals, exponential service time 
     and multiple customer generation

"""

import random

import simpy


RANDOM_SEED = 33
NEW_CUSTOMERS = 5  # Total number of customers
INTERVAL_CUSTOMERS = 10.0  # Generate new customers roughly every x seconds


def source(env, number, interval, queue):
    """Source generates customers randomly"""
    for i in range(number):
        c = customer(env, 'Cli %02d' % i, queue, time_in_bank=12.0)
        env.process(c)
        
        # Poisson Arrivals
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


def customer(env, name, queue, time_in_bank):
    """Customer arrives, is served and leaves."""
    arrive = env.now
    print('%7.4f %s: Chegada' % (arrive, name))

    with queue.request() as req:
        yield req

        # Customer acquires the resource
        print('%7.4f %s: Espera: %6.3f' % (env.now, name, env.now - arrive))

        # Exponential Service Time
        start = env.now     # Service initiates
        t = random.expovariate(1.0 / time_in_bank)
        yield env.timeout(t)
        print('%7.4f %s: Termino, Em Servico=%7.4f' % (env.now, name, env.now - start))

 
# Setup and start the simulation
print('Bank')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Start processes and run
queue = simpy.Resource(env, capacity=1)
env.process(source(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, queue))
env.run()
