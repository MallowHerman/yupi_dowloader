from pytube import YouTube
from tqdm import tqdm
import os
import datetime

def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completetion = round(bytes_downloaded / total_size * 100, 2)
	print(f'Downloading: {percentage_of_completetion}%')


def get_link():
	link = str(input('Copia e cola aqui a url do link do Youtube que deseja baixar: '))
	print('Carregando informações...')
	
	yt = YouTube(link)

	status = yt.check_availability()
	print('Status: ',status)
	yt.register_on_progress_callback(on_progress)

	stream = yt.streams.get_highest_resolution()
	print('='*60)
	print(f'''Título: {yt.title}
Duração: {datetime.timedelta(seconds = yt.length)}
Visualizações: {yt.views}
Resolução: {stream.resolution}
Tamanho: {round(yt.streams.get_highest_resolution().filesize / 1000000, 2)} Mb''')
	print('='*60)
	while True:
		confirmation = input(f'Deseja confirmar o download do video: {yt.title}? Digite [S/N]: ').lower()

		if confirmation == 's':
			try:
				os.mkdir('downloads')
			except:
				pass
			path = os.getcwd() + '\downloads'
			print("Iniciando download... o download pode levar alguns minutos!")
			stream.download(path)
			print("Download finalizado!")
			get_link()
		if confirmation == 'n':
			break
		else:
			print('Resposta Inválida')

get_link()
