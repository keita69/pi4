# CO2濃度測定
# https://dev.classmethod.jp/articles/raspberry-pi-4-b-mh-z19b-co2/

import mh_z19
import time

def getCo2():
    out = mh_z19.read()

    if not "co2" in out:
       print("Initializing mh_z19.......")
       print(out)
       time.sleep(10)

    co2 = out['co2']
    return co2


if __name__ == '__main__':
    getCo2()
