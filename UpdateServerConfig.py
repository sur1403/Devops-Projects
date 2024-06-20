import os

def server_config(file_path, key, value):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
    
    with open(file_path, 'w') as fp:
        for line in lines:
            if key in line:
                fp.write(key + "=" + value + "\n")
            else:
                fp.write(line)

file_path = 'server.conf'

server_config(file_path, "MAX_CONNECTIONS", "600")


