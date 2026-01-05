import cv2
import sys
import os
import numpy as np
from collections import Counter

classes = ['cat', 'dog']


def knn_prediction(features, labels, image_feature, k):
    distances = []
    for i in range(len(features)):
        diff = np.linalg.norm(features[i] - image_feature)
        distances.append((diff, labels[i]))
    distances.sort(key = lambda x : x[0])
    k_nears = [label for (_, label) in distances[:k]]
    return Counter(k_nears).most_common(1)[0][0]


def extract_features(file_path):
    image = cv2.imread(file_path)
    image = cv2.resize(image, (64, 64))
    image_hist = cv2.calcHist([image], [0, 1, 2], None, (8, 8, 8), (0, 256, 0, 256, 0, 256))
    return cv2.normalize(image_hist, image_hist).flatten()


def load_dataset():
    features = []
    labels = []
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
    for label,  class_name in enumerate(classes):
        folder = os.path.join(base_dir, class_name)
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            feature = extract_features(file_path)
            features.append(feature)
            labels.append(label)
    return np.array(features), np.array(labels)


def main():
    try:
        features_list, labels_list = load_dataset()
        core_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test')

        for path in os.listdir(core_dir):
            test_path = os.path.join(core_dir, path)

            if not os.path.exists(test_path):
                raise FileNotFoundError(f'{test_path} is not exists!')

            test_image = cv2.imread(test_path)

            if test_image is None:
                raise ValueError('Empty image!')

            test_feature = extract_features(test_path)
            prediction = knn_prediction(features_list, labels_list, test_feature, 5)
            test_prediction = classes[prediction]
            print(f'Prediction of image : {test_path} : {test_prediction}')
            cv2.putText(test_image, f'Prediction : {test_prediction}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow(f'{test_path}', test_image)
            while True:
                key = cv2.waitKey(3000) & 0xFF
                if key == ord('q') or key == 27:
                    print('Exiting...')
                    break

    except FileNotFoundError:
        print('Wrong path!')
    except ValueError:
        print('Image is empty!')
    except KeyboardInterrupt:
        print('Keyboard interrupted. Exiting by clicking Ctrl + C!')
    except Exception as e:
        print(f'Unexpected error occured, {e}!')
    finally:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
