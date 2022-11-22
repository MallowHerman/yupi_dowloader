from pytube import YouTube
from tqdm import tqdm
import os
import datetime

def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completetion = round(bytes_downloaded / total_size * 100, 2)

def check_video_exist(video_path):
	video_exist = os.path(video_path)
	return video_exist


def main():
	link = str(input('Copia e cola aqui a url do link do Youtube que deseja baixar: '))
	print('Carregando informações...')
	
	yt = YouTube(link)
	stream = yt.streams.get_highest_resolution()
	print('='*60)
	print(f'Título: {yt.title}\nDuração: {datetime.timedelta(seconds = yt.length)}\nResolução: {stream.resolution}\nTamanho: {round(yt.streams.get_highest_resolution().filesize / 1000000, 2)} Mb')
	print('='*60)

	while True:
		confirmation = input(f'Deseja confirmar o download do video: {yt.title}? Digite [S/N]: ').lower()
		
		valid_confirmation_list = ['s', 'sim', 'y', 'yes']
		valid_refuse_list =['n', 'nao', 'não', 'no' ]

		if confirmation in valid_confirmation_list:
			try:
				os.mkdir('downloads')
			except:
				pass

			path = os.getcwd() + '/downloads'
			video_exist = check_video_exist(f"{path}/{yt.title}.mp4")
			print(video_exist)
			exit()
			print("Iniciando download... o download pode levar alguns minutos!")
			yt.register_on_progress_callback(on_progress)
			stream.download(path)
			print("Download finalizado!")

			break

		elif confirmation in valid_refuse_list:
			break
		else:
			print('Resposta Inválida! Por favor escolha dentre as opções "s" ou "n"')


if __name__ == "__main__":
	main()
