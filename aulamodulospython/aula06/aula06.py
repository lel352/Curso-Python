# https://ffmpeg.org/documentation.html

# https://ffmpeg.zeranoe.com/builds/

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'
debug = ''

caminho_origem = r'C:\Users\desen\Downloads'
caminho_destino = r'C:\Users\desen\Downloads\arruma\serie2'


for root, directs, files in os.walk(caminho_origem):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mkv'):
            continue

        caminho_completo = os.path.join(root, file)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(file)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(root, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)




