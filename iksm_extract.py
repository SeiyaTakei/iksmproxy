import os
import sys
import json

class IksmInfo:

    def __init__(self, conf):
        self.set_config(conf)
        self.iksm_session = ""


    def set_rawstring(self, raw):
        self.raw = raw


    def extract_iksm_session(self):
        # extract set-cookie from raw data
        head = self.raw.find("iksm_session")
        tmpstr = self.raw[head:]
        end = tmpstr.find("'")
        tmpstr = tmpstr[0:end]
        
        # extract iksm_session and expire from cookie
        datalist = tmpstr.split("; ")
        for data in datalist:
            if "iksm_session" in data:
                self.iksm_session_new = data.split("=")[1]
        if self.iksm_session != self.iksm_session_new:
            self.iksm_session = self.iksm_session_new
            self.write_data()


    def write_data(self):
        if os.path.exists(self.path):
            print("config file is exists!")
            f = open(self.path, 'r')
            c = json.load(f)
            f.close()
            c['cookie'] = self.iksm_session
            f = open(self.path, 'w')
            after = json.dump(c, f, indent=4)
            f.close()
        else:
            print("config file is not exists...")
            sys.exit(1)


    def set_config(self, conf):
        self.conf = conf
        self.path = self.conf['splatnet2statink'] + "/config.txt"
              

    def get_iksm_session(self):
        return self.iksm_session


    def get_iksm_expire(self):
        return self.iksm_expire
