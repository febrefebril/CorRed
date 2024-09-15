import google.generativeai as genai
import os
import PIL.Image
import logging
import sys
import ComandParser 
from os import listdir
from os.path import isfile, join

ComandParser.printaOla()

PATH_TO_FILES = './essays/'
PATH_TO_PROMPT = './prompts/instructionPrompt'
PATH_TO_LOG_FILE = './log/corred.log'

pathOfFiles = [PATH_TO_FILES + f for f in listdir(PATH_TO_FILES) if isfile(join(PATH_TO_FILES, f)) and ('.txt' not in str(f))]
isSingleFileCorrection = True if (len(sys.argv)) != 1 else False
logFile = PATH_TO_LOG_FILE 
genai.configure(api_key=os.environ["API_KEY"])
# model = genai.GenerativeModel(model_name="gemini-1.5-flash")
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

logger = logging.getLogger(__name__)
logging.basicConfig(filename=logFile, level=logging.INFO)

def getPromptFromFile(pathToFile):
    f = open(pathToFile)
    prompt = f.read() 
    f.close()
    return prompt

def doEssayCorrection(essayPathImage, correctionPrompt ):
    sample_file = PIL.Image.open(essayPathImage)
    correctedEssay = model.generate_content([correctionPrompt, sample_file])
    print('Conteudo de correctedEssay: %s', correctedEssay.text)
    logger.info('Conteudo de correctedEssay: %s', correctedEssay.text)
    return correctedEssay 

def saveTheCorrection(pathFileToSave, correctedEssay, prompt):
    saveFileAs = '.' + pathFileToSave.split('.')[1] + '.txt'
    logger.info('conteudo de saveFileAs: %s :', saveFileAs)
    print('conteudo de saveFileAs: %s :', saveFileAs)
    f = open(saveFileAs, 'a')
    f.write(correctedEssay.text)
    f.close()
    logger.info('Prompt gerador da resposta: %s', prompt)
    logger.info('correcao da redacao: %s', correctedEssay.text)
    logger.info('fim do log')
    print('Prompt gerador da resposta: %s', prompt)
    print('correcao da redacao: %s', correctedEssay.text)
    print('fim do log')

def correctionOfAllEssayFromFolder(pathToFolderOfTheEssays, promptOfCorrection):
    for file in pathToFolderOfTheEssays:
        correctedEssay = doEssayCorrection(file, promptOfCorrection)
        saveTheCorrection(file, correctedEssay, promptOfCorrection)

if isSingleFileCorrection:
    prompt = sys.argv[2] 
    enssay = sys.argv[4]
    print(f'prompt:{prompt} \nenssay:{enssay}')
    doEssayCorrection(enssay, prompt)
    print('Modo correcao unica')
    pass
else:
    print('Modo correcao em bloco')
    prompt = getPromptFromFile(PATH_TO_PROMPT)
    correctionOfAllEssayFromFolder(pathOfFiles, prompt)

