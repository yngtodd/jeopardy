import os
import numpy as np

from .utils import download_url, makedir_exist_ok


class JeopardyData:
    """Jeopardy Dataset.

    Parameters
    ----------
    root str :
        Root directory of dataset where ``processed/training.npy`` lives.

    download : bool, optional
        If true, downloads the dataset from the internet and
        puts it in root directory. If dataset is already downloaded, it is not
        downloaded again.
    """
    urls = [
      'https://raw.githubusercontent.com/utkML/data/master/jeopardy/x_train.npy',
      'https://raw.githubusercontent.com/utkML/data/master/jeopardy/y_train.npy',
    ]

    data_file = 'data.npy'
    label_file = 'labels.npy'

    def __init__(self, root, download=False):
        self.root = os.path.expanduser(root)

        if download:
            self.download()

        if not self._check_exists():
            raise RuntimeError('Dataset not found.' +
                               ' You can use download=True to download it')

        data_file = self.data_file
        label_file = self.label_file

        self.data = np.load(os.path.join(self.processed_folder, data_file))
        self.targets = np.load(os.path.join(self.processed_folder, label_file))

    def __len__(self):
        return len(self.data)

    def load_data(self):
        return self.data, self.targets

    @property
    def raw_folder(self):
        return os.path.join(self.root, self.__class__.__name__, 'raw')

    @property
    def processed_folder(self):
        return os.path.join(self.root, self.__class__.__name__, 'processed')

    def _check_exists(self):
        return os.path.exists(os.path.join(self.processed_folder, self.data_file)) and \
               os.path.exists(os.path.join(self.processed_folder, self.label_file))

    @staticmethod
    def extract_array(path, remove_finished=False):
        print('Extracting {}'.format(path))
        arry = np.load(path)
        if remove_finished:
            os.unlink(path)

    def download(self):
        """Download the jeopardy data if it doesn't exist in processed_folder already."""

        if self._check_exists():
            return

        makedir_exist_ok(self.raw_folder)
        makedir_exist_ok(self.processed_folder)

        # download files
        for url in self.urls:
            filename = url.rpartition('/')[2]
            file_path = os.path.join(self.raw_folder, filename)
            download_url(url, root=self.raw_folder, filename=filename, md5=None)
            self.extract_array(path=file_path, remove_finished=False)

        # process and save as numpy files
        print('Processing...')

        training_set = (
            np.load(os.path.join(self.raw_folder, 'x_train.npy')),
            np.load(os.path.join(self.raw_folder, 'y_train.npy'))
        )

        # Save processed training data
        train_data_path = os.path.join(self.processed_folder, self.data_file)
        np.save(train_data_path, training_set[0])
        train_label_path = os.path.join(self.processed_folder, self.label_file)
        np.save(train_label_path, training_set[1])

        print('Done!')

    def __repr__(self):
        fmt_str = 'Dataset ' + self.__class__.__name__ + '\n'
        fmt_str += '    Number of datapoints: {}\n'.format(self.__len__())
        fmt_str += '    Root Location: {}\n'.format(self.root)
        return fmt_str
