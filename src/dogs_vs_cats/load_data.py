import h5py
import numpy as np

def load_dataset(train_h5, test_h5):
    train_dataset = h5py.File(train_h5, "r")
    test_dataset = h5py.File(test_h5, "r")

    train_x = np.array(train_dataset["x_train"][:])
    train_y = np.array(train_dataset["y_train"][:])
    
    test_x = np.array(test_dataset["x_test"][:])
    test_y = np.array(test_dataset["y_test"][:])

    classes = np.array(train_dataset["classes_list"][:])

    return train_x, train_y, test_x, test_y, classes


if __name__ == '__main__':
    x_train, y_train, x_test, y_test, classes = load_dataset("data_train.h5", "data_test.h5")
    print(f'category: {classes}')
    print(f'train/test: {len(y_train)}/{len(y_test)}')
    print(f'train shape is {x_train.shape}/{y_train.shape}')
    print(f'test shape is {x_test.shape}/{y_test.shape}')