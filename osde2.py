import platform
import sys

# Give only OS (Windows, Darwin, linux, linux2)
#res = platform.system()

# Give more details
#res = platform.platform()

# print (res)

# Give all

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s
dist: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
""" % (
sys.version.split('\n'),
str(platform.dist()),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
))


