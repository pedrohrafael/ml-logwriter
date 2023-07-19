import os
import sys
import random
import hashlib
import joblib
from datetime import datetime
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
LOG_DATEFMT = '%Y-%m-%Y %I:%M:%S %p'

class _CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + LOG_FORMAT + reset,
        logging.INFO: grey + LOG_FORMAT + reset,
        logging.WARNING: yellow + LOG_FORMAT + reset,
        logging.ERROR: red + LOG_FORMAT + reset,
        logging.CRITICAL: bold_red + LOG_FORMAT + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, LOG_DATEFMT)
        return formatter.format(record)

class LogWriter:    
    """
    Logging package for Python.
        
    Methods
    -------
    logger(path) :
        Return a register and create a file at the specified path.    
    """
    
    def logger(self, path):
        """
        Return a register and create a file at the specified path.
        
        Parameters
        -------
        path : str, required
            directory path on will create the log file.
        """
        self.log_path = path
        StreamHandler = logging.StreamHandler()
        StreamHandler.setFormatter(_CustomFormatter())
        
        logging.basicConfig(level=logging.DEBUG,
                            format=LOG_FORMAT,
                            datefmt=LOG_DATEFMT,
                            handlers=[logging.FileHandler(self.log_path), StreamHandler]
                           )
        return logging

class LogArtifacts:
    """
    Logging artifacts package for Python.
        
    Methods
    -------
    create(name) :
    load(name) : 
    log_parameters(parameters) : 
    log_metrics(metrics) : 
    log_model(model) :
    log_dataset(dataframe, name) :
    """
    
    def __init__(self, path):
        """
        Logging artifacts package for Python.
        Parameters
        -------
        path : str, required
            root directory path on will create the other directories by methods.
        """
        self.root_artifacts_path=path
     
    def create(self, name=None):
        if name:
            if name not in os.listdir(self.root_artifacts_path):
                self.name = name
            else:
                sys.exit(f"Diretório já existente:{os.path.join(self.root_artifacts_path, name)}")
        else:
            self.name = hashlib.md5(str(random.getrandbits(50)).encode('utf-8')).hexdigest()
        self.artifacts_path = os.path.join(self.root_artifacts_path, self.name)
        try:
            os.mkdir(self.artifacts_path)
        except Exception as e:
            sys.exit(e)
        
    def load(self, name):
        self.artifacts_path = os.path.join(self.root_artifacts_path, name)
        
    def log_parameters(self, params):
        directory = 'parameters'
        path = os.path.join(self.artifacts_path, directory)
        try:
            if not directory in os.listdir(self.artifacts_path):
                os.mkdir(path)
        except Exception as e:
            sys.exit(e)
        for key, value in params.items():
            file = os.path.join(path, key)
            with open(file, 'x+') as f:
                f.write(str(value))
    
    def log_metrics(self, metrics):
        directory = 'metrics'
        path = os.path.join(self.artifacts_path, directory)
        try:
            if not directory in os.listdir(self.artifacts_path):
                os.mkdir(path)
        except Exception as e:
            sys.exit(e)
        for key, value in metrics.items():
            file = os.path.join(path, key)
            with open(file, 'x+') as f:
                f.write(str(value))
   
    def log_model(self, model):
        directory = 'artifacts'
        path = os.path.join(self.artifacts_path, directory)
        try:
            if not directory in os.listdir(self.artifacts_path):
                os.mkdir(path)
            self.path_model = path
        except Exception as e:
            sys.exit(e)
        joblib.dump(model, os.path.join(self.path_model, 'model.pkl'))
        self._log_meta()
    
    def log_dataset(self, dataframe, name):
            """
            Save dataframe as CSV.
            """
            directory = 'datasets'
            path = os.path.join(self.artifacts_path, directory)
            try:
                if not directory in os.listdir(self.artifacts_path):
                    os.mkdir(path)
                dataframe.to_csv(os.path.join(path, name + '.csv'), index=False)
            except Exception as e:
                sys.exit(e)            
                       
    def _log_meta(self):
        create_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        user = os.getlogin()
        values = [f'create_date: {create_date}\n', f'created_by: {user}']
        meta_file = os.path.join(self.path_model, 'meta.yaml')
        open(meta_file, 'x+').close()
        for v in values:
            with open(meta_file, 'a') as f:
                f.write(v)