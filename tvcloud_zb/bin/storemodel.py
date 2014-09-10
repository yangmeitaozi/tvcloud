import cPickle as pickle
import ConfigParser
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

config = ConfigParser.ConfigParser()
config.read("%s/storagepath.ini" % (BASE_DIR))

CHANNEL_PATH = "channel.pickle"
CATALOG_PATH = "catalog.pickle"
PROGRAM_PATH = "program.pickle"

def get_filepath(filename):
    if fileaname=='channel':
        return CHANNEL_PATH
    elif filename=='catalog':
        return CATALOG_PATH
    else:
        return PROGRAM_PATH

def put_to_store(data,filename):
    file =  get_filepath(filename)   
    filepath = "%s/%s" % (BASE_DIR,file)
    try:
        with open(filepath,'wb') as fp:
            pickle.dump(data,fp,True)
    except PickleError as error:
        print('File error:' + str(error))
        

def get_data_from_store(filename):
    file =  get_filepath(filename)
    filepath = "%s/%s" % (BASE_DIR,file)
    try:
        with open(filepath,'rb') as fp:
            response = pickle.load(fp)
            return response
    except PickleError as error:
        print('File error:' + str(error))
