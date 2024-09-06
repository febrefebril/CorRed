import google.generativeai as genai
import os
import PIL.Image
from os import listdir
from os.path import isfile, join

#pathToListOfFiles = './essays/'
PATH_TO_FILES = './essays/'
# pathToPrompt = './prompts/instructionPrompt'
PATH_TO_PROMPT = './prompts/instructionPrompt'
onlyfiles = [PATH_TO_FILES + f for f in listdir(PATH_TO_FILES) if isfile(join(PATH_TO_FILES, f)) and ('.txt' not in str(f))]

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def promptFromFile(pathToFile):
    f = open(pathToFile)
    prompt = f.read() 
    f.close()
    return prompt

for text in onlyfiles:
    pathOfText = PATH_TO_FILES + str(text)
    print('Iniciando a correçao de ', pathOfText)
    sample_file = PIL.Image.open(pathOfText)
    response = model.generate_content([prompt, sample_file])
    print(response.text)
    saveFileAs = '.' + pathOfText.split('.')[1] + '.txt'
    print('Abrindo arquivo: ', saveFileAs)
    f = open(saveFileAs, 'a')
    f.write(response.text)
    f.write('#' * 80)
    f.write('LOG: prompt gerador desta resposta')
    f.write(prompt)
    f.write('FIM LOG')
    f.write('#' * 80)
    f.close()
    print('Fim da correção')
