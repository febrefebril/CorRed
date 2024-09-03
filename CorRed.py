import google.generativeai as genai
import os
import PIL.Image
from os import listdir
from os.path import isfile, join

pathToListOfFiles = './essays/'
pathToPrompt = './prompts/instructionPrompt'
onlyfiles = [f for f in listdir(pathToListOfFiles) if isfile(join(pathToListOfFiles, f)) and ('.txt' not in str(f))]
print(onlyfiles)

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
f = open(pathToPrompt)
prompt = f.read() 
f.close()

for text in onlyfiles:
    pathOfText = pathToListOfFiles + '/' + str(text)
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
