import asyncio
import time
import random

class Items:
    
    def __init__(self, name):
        self.name = name
        pass
    
    def __repr__(self):
        return f'Item: {self.name}'
    
    def cancel(self):
        raise asyncio.CancelledError

async def producer(queue):
    count = 0
    
    while True:
        item = Items(name = count)
        
        print(f'Producing: {item} {time.perf_counter()}')
        await queue.put(item)
        await asyncio.sleep(1)
        
        count += 1
        if count >= 10: item.cancel()
    
        
async def worker(name, queue):
    while True:
        
        # Get item from queue.
        item = await queue.get()
        
        # Do the work
        await asyncio.sleep(random.uniform(1, 3))
        print(f'Consuming: {item} {time.perf_counter()}')
        
        # Indicate that the work is done.
        queue.task_done()
        
class ScaperQueue(asyncio.Queue):
    
    _instance = None
    __lock = asyncio.Lock()
    
    @classmethod
    async def get_instance(cls):
        async with cls.__lock:
            if not cls._instance:
                cls.__instance = cls()
        
        return cls.__instance
        
    def __init__(self):     
        if ScaperQueue._instance is not None:
            raise Exception("ScraperQueue instance already instaintiated")
        
        super().__init__(self)
   
        
async def main():
    queue = asyncio.Queue()
    
    # Start Producer
    producer_task = asyncio.create_task(producer(queue))
    
    # Start multiple workers to consumer tasks
    workers = [asyncio.create_task(worker(queue))]
    
    # Wait for producter to finish 
    try:
        await producer_task
    except asyncio.CancelledError:
        print("Producer was canceled")
    
    # Wait for the queu to be fully processed
    await queue.join()
    print(f"All tasks have been processed {time.perf_counter()}")
    
    # Cancel Consumer Tasks
    consumer_task.cancel()
    
    try:
        await consumer_task
        
    except asyncio.CancelledError:
        pass
    

class Test:
    
    __test_instance = None
    
    def __init__(self):
        pass
        
    @classmethod
    async def set_instance(cls, variable):
        async with asyncio.Lock():
            Test.__test_instance = variable
            
    def print_test_instance(self):
        print(self.__test_instance)
            
async def test_main():
    i1 = Test()
    i1.print_test_instance()
    
    await i1.set_instance('blue')
    
    i2 = Test()
    i2.print_test_instance()
    
    i1.__test_instance = 'green'
    i1.print_test_instance()
       
asyncio.run(test_main())