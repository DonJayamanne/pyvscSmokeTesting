# Add a minor delay for tests to confirm debugger has started
import time


time.sleep(2)
print("Hello World")
open("log.log", "w").write("Hello")
