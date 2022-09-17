import pickle

class DataBase:
    def __init__(self, file_path : str, objects = None):
        self.file_path = file_path
        self.data = objects
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)


    def add(self, obj):
        self.data.append(obj)
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)

    def get(self):
        with open(self.file_path, 'rb') as f:
            self.data = pickle.load(f)
        return self.data


