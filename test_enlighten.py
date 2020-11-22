import time
import enlighten

manager = enlighten.get_manager()
ticks = manager.counter(total=100, desc="Ticks", unit="ticks", color="red")
tocks = manager.counter(total=20, desc="Tocks", unit="tocks", color="white")

for num in range(100):
    time.sleep(0.1)  # Simulate work
    #print("The quick brown fox jumps over the lazy dog. {}".format(num))
    ticks.update()
    if not num % 5:
        tocks.update()

manager.stop()