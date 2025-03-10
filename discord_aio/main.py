import time


import my_bbca
import my_CC


#where all monitor modules run to
def main():
    my_bbca.checkResponse()
    my_CC.instore()



#inits ALL monitors
while True:
    main()
    time.sleep(30)