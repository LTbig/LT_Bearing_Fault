from scipy.io import loadmat


class read_data_one_subject:
    def __init__(self, path):
        with open(path + '.mat', 'rb') as file:
            data = loadmat(file)
        self.data = data


subject = read_data_one_subject("./174")
print(subject)
