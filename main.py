import json
import iksm_proxy

def send_data():
    

def config():
    f = open('config.json', 'r')
    c = json.load(f)
    f.close()
    return c


def main():
    conf = config()
    proxy = iksm_proxy.IksmProxy(conf)
    proxy.run()

if __name__ == '__main__':
    main()
