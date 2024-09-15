import sys
from os import listdir
from os.path import isfile, join

PATH_TO_FILES = './essays/'
PATH_TO_PROMPT = './prompts/instructionPrompt'
PATH_TO_LOG_FILE = './log/corred.log'

pathOfFiles = [PATH_TO_FILES + f for f in listdir(PATH_TO_FILES) if isfile(join(PATH_TO_FILES, f)) and ('.txt' not in str(f))]
isSingleFileCorrection = True if (len(sys.argv)) != 1 else False
logFile = PATH_TO_LOG_FILE 

class CommandParser:

    def __init__(self,
                 pathToFileOfEssay=None,
                 pathToFolderOfEssay=PATH_TO_FILES,
                 pathToCorrectionPrompt=PATH_TO_PROMPT,
                 isSigleCorrection=False,
                 isMultipleCorrection=False
                 ):
        self.pathToFolderOfEssay = pathToFolderOfEssay
        self.pathToFileOfEssay = pathToFileOfEssay
        self.pathToCorrectionPrompt = pathToCorrectionPrompt
        self.isSigleCorrection = isSigleCorrection
        self.isMultipleCorrection = isMultipleCorrection

    # def checkSingleOrMultipleCorrection(parametersList):
    #     if len(parametersList) = 2:
    #         isMultipleCorrection = True
    #     else:
    #         isMultipleCorrection = True

    # def checkComandLineParameters(parametersList):
    #     if isMultipleCorrection = True:
    #         else:
    #         checkInconcistentParameter(parametersList)
