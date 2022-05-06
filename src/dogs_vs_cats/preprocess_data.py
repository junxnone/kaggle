import os
import cv2
import pandas as pd
import numpy as np
import h5py
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from argparse import ArgumentParser

def build_argparser():
    parser = ArgumentParser()
    parser.add_argument(
            "-i",
            "--input_dir",
            help="Input Image Dir",
            required=True,
            default='pkg/data/train',
            type=str)
    parser.add_argument(
            "-v",
            "--val_ratio",
            help="Validation image ratio",
            required=False,
            default=0.3,
            type=float)
    parser.add_argument('-h5',
                        '--create_h5',
                        help='Create h5 dataset',
                        action='store_true')
    return parser


if __name__ == '__main__':

    args = build_argparser().parse_args()
    data_train = args.input_dir
    img_list = []
    img_category = []
    for img_name in os.listdir(data_train):
        img_list.append(os.path.join(data_train, img_name))
        img_category.append('dog' in img_name)

    x_train, x_test, y_train, y_test = train_test_split(img_list, img_category, test_size=args.val_ratio, random_state=42)

    df_train = pd.DataFrame({'img_path':x_train, 'category': y_train})
    df_test = pd.DataFrame({'img_path':x_test, 'category': y_test})
    df_train.to_csv('train.csv')
    df_test.to_csv('test.csv')

    print(f'Data Total: {len(img_list)}')
    print(f'Split train/test data {len(x_train)}/{len(x_test)}')
    print(f'Dogs data(train/test):{len(df_train[df_train.category==True])}/{len(df_test[df_test.category==True])}')
    print(f'Cats data(train/test):{len(df_train[df_train.category==False])}/{len(df_test[df_test.category==False])}')

    if args.create_h5:
        IMG_SIZE = 224
        classes_list = ['dog', 'cat']

        test_image = np.zeros((len(x_test), IMG_SIZE, IMG_SIZE, 3))
        test_label = np.zeros((len(y_test), 1))
        for i in tqdm(range(len(x_test))):
            oimg = cv2.imread(x_test[i])
            rsimg = cv2.resize(oimg,(IMG_SIZE, IMG_SIZE))
            test_image[i] = np.array(rsimg)
            test_label[i] = np.array(y_test[i])

        h5_test = h5py.File("data_test.h5", "w")
        h5_test.create_dataset("x_test", data=test_image, dtype=np.uint8)
        h5_test.create_dataset("y_test", data=test_label, dtype=np.uint8)
        h5_test.create_dataset("classes_list", data=classes_list)

        h5_test.close()

        train_image = np.zeros((len(x_train), IMG_SIZE, IMG_SIZE, 3))
        train_label = np.zeros((len(y_train), 1))
        for i in tqdm(range(len(x_train))):
            oimg = cv2.imread(x_train[i])
            rsimg = cv2.resize(oimg,(IMG_SIZE, IMG_SIZE))
            train_image[i] = np.array(rsimg)
            train_label[i] = np.array(y_train[i])

        h5_train = h5py.File("data_train.h5", "w")
        h5_train.create_dataset("x_train", data=train_image, dtype=np.uint8)
        h5_train.create_dataset("y_train", data=train_label, dtype=np.uint8)
        h5_train.create_dataset("classes_list", data=classes_list)

        h5_train.close()