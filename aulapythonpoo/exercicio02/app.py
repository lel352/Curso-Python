from aulapythonpoo.exercicio02.classes.calcipv4 import CalcIPv4

def main():
    """ Exemplos de Uso """

    # Com prefixo
    calc_ipv4_1 = CalcIPv4(ip='192.168.0.128', prefixo=30)

    print(f'IP: {calc_ipv4_1.ip}')
    print(f'Máscara: {calc_ipv4_1.mascara}')
    print(f'Rede: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefixo: {calc_ipv4_1.prefixo}')
    print(f'Número de IPs da rede: {calc_ipv4_1.numero_ips}')

    print('#' * 80)

    # Com máscara
    calc_ipv4_2 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.192')

    print(f'IP: {calc_ipv4_2.ip}')
    print(f'Máscara: {calc_ipv4_2.mascara}')
    print(f'Rede: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefixo: {calc_ipv4_2.prefixo}')
    print(f'Número de IPs da rede: {calc_ipv4_2.numero_ips}')


# if __name__ == '__main__':
main()
