import re

class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo


        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self.ip

    @property
    def mascara(self):
        return self.mascara

    @property
    def prefixo(self):
        return self.prefixo

    @ip.setter
    def ip(self, ip):
        if not self._valida_ip(ip):
            raise ValueError('IP inválido.')

        self.ip = ip
        self._ip_bin = self._ip_to_bin(ip)

    @mascara.setter
    def mascara(self, mascara):
        if not mascara:
            return

        if not self._valida_ip(mascara):
            raise ValueError('Máscara inválida.')

        self.mascara = mascara
        self._mascara_bin = self._ip_to_bin(mascara)
        if not  hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, prefixo):

        if not prefixo:
            return

        if not isinstance(prefixo, int):
            raise TypeError('Prefixo precisa ser inteiro')

        if prefixo > 32:
            raise TypeError('Prefixo precisa ter 32bits')


        self.prefixo = prefixo
        self._mascara_bin = (prefixo * '1').ljust(32, '0')
        if not hasattr(self, 'mascara'):
            self.mascara= self._bin_to_ip(self._mascara_bin)

    @staticmethod   # Não precisa do Self
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9{1,3}]).([0-9{1,3}]).([0-9{1,3}]).([0-9{1,3}])$ '
        )
        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [int(ip[i:n+i], 2) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast


    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)


