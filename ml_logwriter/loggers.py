import os
import sys
import random
import hashlib
import joblib
from datetime import datetime
import matplotlib.pyplot as plt
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
    logger(path):
        Return a logger and create a file at the specified path.
    """
    
    def logger(self, path):
        """
        Return a logger and create a file at the specified path.

        Parameters
        ----------
        path : str
            Directory path where the log file will be created.
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
    create(name=None) : Create a new artifacts directory with the specified name or a random name.
    load(name) : Load an existing artifacts directory.
    log_parameters(parameters) :  Log model parameters.
    log_metrics(metrics) :  Log model evaluation metrics.
    log_model(model) : Save the trained model to the artifacts directory.
    log_dataset(dataframe, name) : Save the DataFrame as a CSV file in the artifacts directory.
    log_performance_graph(self, x_values, y_values, title, x_label, y_label, filename) : Log a performance graph and save it in the artifacts directory.
    """
    
    def __init__(self, path):
        """
        Create a LogArtifacts object.

        Parameters
        ----------
        path : str
            Root directory path where other directories will be created by methods.
        """
        self.root_artifacts_path = path
     
    def create(self, name=None):
        """
        Create a new artifacts directory with the specified name or a random name.

        Parameters
        ----------
        name : str, optional
            Name of the artifacts directory. If not provided, a random name will be generated.
        """
        if name:
            if name not in os.listdir(self.root_artifacts_path):
                self.name = name
            else:
                sys.exit(f"Directory already exists: {os.path.join(self.root_artifacts_path, name)}")
        else:
            self.name = hashlib.md5(str(random.getrandbits(50)).encode('utf-8')).hexdigest()
        self.artifacts_path = os.path.join(self.root_artifacts_path, self.name)
        try:
            os.mkdir(self.artifacts_path)
        except Exception as e:
            sys.exit(e)
        
    def load(self, name):
        """
        Load an existing artifacts directory.

        Parameters
        ----------
        name : str
            Name of the existing artifacts directory to load.
        """
        self.artifacts_path = os.path.join(self.root_artifacts_path, name)
        
    def log_parameters(self, params):
        """
        Log model parameters.

        Parameters
        ----------
        params : dict
            Dictionary containing model parameters to be logged.
        """
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
        """
        Log model evaluation metrics.

        Parameters
        ----------
        metrics : dict
            Dictionary containing model evaluation metrics to be logged.
        """
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
        """
        Save the trained model to the artifacts directory.

        Parameters
        ----------
        model : object
            Trained model object to be saved.
        """
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
        Save the DataFrame as a CSV file in the artifacts directory.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            DataFrame to be saved as a CSV file.
        name : str
            Name of the CSV file to be saved.
        """
        directory = 'datasets'
        path = os.path.join(self.artifacts_path, directory)
        try:
            if not directory in os.listdir(self.artifacts_path):
                os.mkdir(path)
            dataframe.to_csv(os.path.join(path, name + '.csv'), index=False)
        except Exception as e:
            sys.exit(e)
            
    def log_performance_graph(self, x_values, y_values, title, x_label, y_label, filename):
        """
        Log a performance graph and save it in the artifacts directory.

        Parameters
        ----------
        x_values : list or array-like
            The x-axis values for the performance graph.
        y_values : list or array-like
            The y-axis values for the performance graph.
        title : str
            Title of the performance graph.
        x_label : str
            Label for the x-axis.
        y_label : str
            Label for the y-axis.
        filename : str
            Filename to save the performance graph (without the file extension).
        """
        if not isinstance(x_values, (list, tuple)) or not isinstance(y_values, (list, tuple)):
            raise ValueError("x_values and y_values must be lists or tuple.")
        
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")

        plt.figure()
        plt.plot(x_values, y_values)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)

        directory = 'performance_graphs'
        path = os.path.join(self.artifacts_path, directory)
        try:
            if not directory in os.listdir(self.artifacts_path):
                os.mkdir(path)
        except Exception as e:
            sys.exit(e)

        file_path = os.path.join(path, filename + '.png')
        plt.savefig(file_path)
        plt.close()
                       
    def _log_meta(self):
        create_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        user = os.getlogin()
        values = [f'create_date: {create_date}\n', f'created_by: {user}']
        meta_file = os.path.join(self.path_model, 'meta.yaml')
        open(meta_file, 'x+').close()
        for v in values:
            with open(meta_file, 'a') as f:
                f.write(v)
