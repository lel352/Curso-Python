# from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone


# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_success('qualquer coisa')

# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_success('qualquer coisa')


from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()
