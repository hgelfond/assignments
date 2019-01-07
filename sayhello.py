#this script reads from STDIN and greets the person whose name it gets passed in.
#!/usr/bin/env python3
import sys
name = sys.stdin.read()
print("Hello " + name + "!")