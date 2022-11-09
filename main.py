#Relógio com for
import time
for hora in range(0,24):
    for minuto in range(0,60):
        for segundo in range(0,60):
            print(hora,":",minuto,":",segundo)
            time.sleep(1.0)
