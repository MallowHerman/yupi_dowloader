from pytube import YouTube
import os
import datetime
from playsound import playsound

def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completetion = round(bytes_downloaded / total_size * 100, 2)
	print(f"Progresso: {percentage_of_completetion}%")

def check_video_exist(video_path: str):
	video_exist = os.path.exists(video_path)
	return video_exist

def start_download(stream, youtube_link, path):
	valid_confirmation_list = ['s', 'sim', 'y', 'yes'] # Lista de sugestões de confirmação
	valid_refuse_list =['n', 'nao', 'não', 'no' ]
	yt = youtube_link
	video_exist = check_video_exist(f"{path}/{yt.title}.mp4") # Verificar se o video já existe dentro da pasta downloads

	if video_exist:
		#Se o video existir pedir confirmação para realizar o download ou cancelar
		print("O video que deseja baixar já existe!")
	else:
		print("Iniciando download... o download pode levar alguns minutos!")
		stream.download(path)
		playsound(f"{os.getcwd()}/beep.wav")
		print("Download finalizado com sucesso!")
		print(f"O video pode ser encontrado no seguinte caminho: {path}/{yt.title}.mp4")

def main():
	link = str(input('>>>Copia e cola aqui a url do link do Youtube que deseja baixar: '))
	print('>>>Carregando informações...')
	try:
		yt = YouTube(link)
		stream = yt.streams.get_highest_resolution()
		print('='*60)
		print(f'Título: {yt.title}\nAutor: {yt.author}\nDuração: {datetime.timedelta(seconds = yt.length)}\nResolução: {stream.resolution}\nTamanho: {round(yt.streams.get_highest_resolution().filesize / 1000000, 2)} Mb')
		print('='*60)
		playsound(f"{os.getcwd()}/beep.wav")

		while True:
			# Pedir confirmação para iniciar o download
			confirmation = input(f'Deseja confirmar o download do video: {yt.title}? Digite [S/N]: ').lower()
			
			valid_confirmation_list = ['s', 'sim', 'y', 'yes'] # Lista de sugestões de confirmação
			valid_refuse_list =['n', 'nao', 'não', 'no' ] # Lista de sugestões de para cancelar

			if confirmation in valid_confirmation_list:
				try:
					os.mkdir('downloads') #Criar diretório para os downloads
				except:
					pass

				path = os.getcwd() + '/downloads' #Pegar caminho completo até a pasta Downloads
				yt.register_on_progress_callback(on_progress)
				start_download(stream, yt, path)
				break							

			elif confirmation in valid_refuse_list:
				break
			else:
				print('Resposta Inválida! Por favor escolha dentre as opções "s" ou "n"')
	except:
		print("Não foi possível realizar o download")


if __name__ == "__main__":
	main()
