import commands
from mitmproxy import flow, controller, options
from mitmproxy.proxy import ProxyServer, ProxyConfig
import iksm_extract

 
class IksmProxy(flow.FlowMaster):
    def __init__(self, conf):
        opts = options.Options(cadir="~/.mitmproxy/")
        config = ProxyConfig(opts)
        state = flow.State()
        server = ProxyServer(config)
        super(IksmProxy, self).__init__(opts, server, state)

        self.conf = conf
        self.info = iksm_extract.IksmInfo(conf)

    def run(self):    
        try:
            flow.FlowMaster.run(self)
        except KeyboardInterrupt:
            self.shutdown()


    @controller.handler
    def log(self, l):
        if "iksm_session" in l.msg and "/?lang=ja-JP" in l.msg:
            #print("log", l.msg)
            self.info.set_rawstring(l.msg)
            if self.info.extract_iksm_session():
                res = commands.getoutput('/bin/systemctl restart splatnet2statink')


    def set_config(self, conf):
        self.conf = conf
