import urllib.request

url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
  'train_img':'train-images-idx3-ubyte.gz',
  'train_label':'train_labels-idx1-ubyte.gz',
  'test_img':'t10k-images-idx3-ubyte.gz',
  'test_label':'t10k-labels-idx1-ubyte.gz'
}

dataset_dir = '/home/tokumoko/tokumoko.github.io/source/Documents'

