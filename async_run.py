import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import threading
import sys

def save_notebook(nb, f):
    global should_continue
    if should_continue:
        threading.Timer(10.0, save_notebook).start()
    with open(sys.argv[2] + '.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

def main():
    global should_continue
    f = open(sys.argv[1])
    print('running ' + sys.argv[1])
    
    nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(kernel_name='python3')

    save_notebook(nb, f)

    ep.preprocess(nb)

    should_continue = False
    with open(sys.argv[2] + '.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
        
    print('ended')


if __name__ == '__main__':
    main()
