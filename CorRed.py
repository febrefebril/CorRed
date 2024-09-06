import google.generativeai as genai
import os
import PIL.Image
from os import listdir
from os.path import isfile, join

#pathToListOfFiles = './essays/'
PATH_TO_FILES = './essays/'
# pathToPrompt = './prompts/instructionPrompt'
PATH_TO_PROMPT = './prompts/instructionPrompt'
pathOfFiles = [PATH_TO_FILES + f for f in listdir(PATH_TO_FILES) if isfile(join(PATH_TO_FILES, f)) and ('.txt' not in str(f))]

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def getPromptFromFile(pathToFile):
    f = open(pathToFile)
    prompt = f.read() 
    f.close()
    return prompt

def essayCorrection(essayPathImage, correctionPrompt ):
    sample_file = PIL.Image.open(essayPathImage)
    correctedEssay = model.generate_content([correctionPrompt, sample_file])
    print(correctedEssay.text)
    return correctedEssay 

def saveTheCorrection(pathFileToSave, correctedEssay):
    saveFileAs = '.' + pathFileToSave.split('.')[1] + '.txt'
    print(saveFileAs)
    print('Abrindo arquivo para salvar a correcao em: ', saveFileAs)
    f = open(saveFileAs, 'a')
    f.write(correctedEssay.text)
    f.write('#' * 80)
    f.write('LOG: prompt gerador desta resposta')
    f.write(prompt)
    f.write('FIM LOG')
    f.write('#' * 80)
    f.close()
    print('Fim da correção')

for file in pathOfFiles:
    prompt = getPromptFromFile(PATH_TO_PROMPT)
    # pathOfText = PATH_TO_FILES + str(file)
    # print('Iniciando a correçao de ', pathOfText)
    correctedEssay = essayCorrection(file, prompt)
    saveTheCorrection(file, correctedEssay)
