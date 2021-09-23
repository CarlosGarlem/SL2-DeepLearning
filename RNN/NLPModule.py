class TextCleaner:

	import os
	import re
	import csv
	import emoji
	import numpy as np
	import pandas as pd
	from random import choices
	from nltk.corpus import stopwords


	def __init__(self, outpath, datasetpath):
		self.mappings_original = {'feliz': ['😀','😃','😄','😁']
           ,'risa': ['🤣','😂']
           ,'amor': ['😍','😘','🥰','❤️','🖤']
           ,'burla': ['😛','😜','🤪','😝']
           ,'serio': ['😐','😑','😶','🙄']
           ,'disgusto': ['😒','🙃','😔','🙁','☹️']
           ,'sorpresa': ['😮','😯','😲']        
           ,'miedo': ['😨','😰','😱','😖']
           ,'tristeza': ['😥','😢','😭']
           ,'enojo': ['😡','😠']
           ,'desafio': ['😎','😏']
           ,'vacuna': ['💉']
           ,'enfermedad': ['💀','☠️','🦠']
           ,'oov': ['']
        }

		self.emoji_dictionary_original = {'feliz': '😃'
                   ,'risa': '😂'
                   ,'amor': '🥰'
                   ,'burla': '😜'
                   ,'serio': '😐'
                   ,'disgusto': '😒'
                   ,'sorpresa': '😮'
                   ,'miedo': '😰'
                   ,'tristeza': '😭'
                   ,'enojo': '😠'
                   ,'desafio': '😎'
                   ,'vacuna': '💉'
                   ,'enfermedad': '🦠'
                   ,'oov': ''
                }

		self.mappings = {'alerta': ['🚨','🔴','⭕','🛑', '❗', '❌', '📌']
           ,'risa': ['🤣','😂']
           ,'notica': ['📢','📺','📰', '👇', '☝', '👀']
           ,'cuidado': ['🚿','💦','😷', '🗣']
           ,'disgusto': ['😒','🙃','😔','🙁','☹️', '😐','😑','😶','🙄', '🤔']    
           ,'miedo': ['😨','😰','😱','😖', '😮','😯','😲']
           ,'tristeza': ['😥','😢','😭', '💔']
           ,'enojo': ['😡','😠']
           ,'desafio': ['😎','😏']
           ,'vacuna': ['💉', '💪']
           ,'enfermedad': ['💀','☠️','🦠', '🤒', '🤧', '🔬']
           ,'oov': ['']
        }


		self.emoji_dictionary = {'alerta': '🚨'
			,'risa': '😂'
			,'notica': '📢'
			,'cuidado': '😷'
			,'disgusto': '😒'
			,'miedo': '😨'
			,'tristeza': '😭'
			,'enojo': '😠'
			,'desafio': '😎'
			,'vacuna': '💉'
			,'enfermedad': '🤒'
			,'oov': ''
		}

		self.all_stopwords = self.stopwords.words('spanish')
		self.output_path = outpath
		self.dataset_path = datasetpath

	
	def createDirectory(self, path):
		if not self.os.path.exists(path):
			self.os.makedirs(path)       
		return


	def createDataset(self, path):		
		self.createDirectory(self.output_path)
		files = self.os.listdir(path)
		filename = self.os.path.join(path, files[0])
		
		data = self.pd.read_csv(filename, encoding = 'utf-8', sep = '\t', nrows = 3)
		header = list(data.columns) 
		header.append('file_source')

		with open(self.dataset_path, 'w', encoding = 'UTF8') as f:
			writer = self.csv.writer(f)
			writer.writerow(header)
		
		return


	def appendData(self, data):
		data.to_csv(self.dataset_path, mode = 'a', encoding = 'utf-8', header = False, index = False)
		print('File data saved succesfully')
		return 

	
	def populateDataset(self, directory):
		for filename in self.os.listdir(directory):
			file = self.os.path.join(directory, filename)
			if 'BR' not in filename and self.os.path.isfile(file):
				data = self.pd.read_csv(file, encoding = 'utf-8', sep = '\t') 
				data['file_source'] = filename
				self.appendData(data)
				
		return


	def emojizeText(self, data):
		mappings_vals = list(self.mappings.values())
		emoji_list = [emoji_icon for sublist in mappings_vals for emoji_icon in sublist]
		example_emojis = self.choices(emoji_list, k = len(data))

		data['emojis'] = example_emojis
		data['comments'] = data[['text', 'emojis']].agg(' '.join, axis = 1)
		return data[['comments']]

	
	def map_emojis(self, emoji_input):
		emotion = 'oov'
		emoji_icon = ''
		for key, sublist in self.mappings.items():
			if emoji_input in sublist:
				emotion = key
				emoji_icon = self.emoji_dictionary[key]
		return emotion, emoji_icon


	def extract_emojis(self, text):
		emoji_list = [c for c in text if c in self.emoji.UNICODE_EMOJI['es']]
		first_emoji = emoji_list[0] if len(emoji_list) > 0 else ''
		emotion, emoji_icon = self.map_emojis(first_emoji)
		return len(emoji_list), emotion, emoji_icon


	def getEmojiData(self, data):
		#data[['emoji_count', 'emotion', 'emoji_icon']] = data.apply(lambda row: self.extract_emojis(row['comments']), axis = 1, result_type = 'expand')
		vfunc = self.np.vectorize(self.extract_emojis)
		count, emotions, icons = vfunc(data['comments'])
		data['emoji_count'] = count
		data['emotion'] = emotions
		data['emoji_icon'] = icons
		data = data[['comments', 'emoji_count', 'emotion', 'emoji_icon']]
		return data


	def normalizar(self, doc):
		txt = self.re.sub(r'[^A-z0-9\s{1}áéíóúüñÁÉÍÓÚÜ]', '', doc).lower().strip().rstrip('\n').rstrip('\r\n')
		return txt


	def removeStopWords(self, text):
		output = ' '.join([token for token in text.split(' ') if not token in self.all_stopwords])
		return output

	
	def clean_data(self, data):
		data['comments'] = list(map(self.normalizar, data['comments']))
		data['comments'] = list(map(self.removeStopWords, data['comments']))
		data.dropna(subset = ['comments'], inplace = True, axis = 0)
		return data
