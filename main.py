# https://ffmpeg.zeranoe.com/builds/

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 30'
preset = '-preset ultrafast'
codec_audio = '-c:a mp3'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:12:23'
debug = ''

caminho_origem = '/home/carlos/Vídeos/converter'
caminho_destino = '/home/carlos/Vídeos/converter/convertido'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVO.mkv'
        # nome_novo_arquivo = nome_arquivo + '_NOVO.mkv'
        # arquivo_saida = os.path.join(raiz, nome_novo_arquivo) Converte na mesma pasta

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                  f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
