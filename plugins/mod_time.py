from datetime import datetime

class Time:
    def gettime(t_format = r"%H:%M:%S"):
        return str(datetime.now().strftime(t_format))
    
    def getdate(d_format = r'%d.%m.%Y'):
        return str(datetime.now().strftime(d_format))