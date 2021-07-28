import pandas as pd
import numpy as np
import re
import click
import sys
import os
import urllib.request

def prefix_emojis(expr):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return re.sub(regrex_pattern, lambda x: f'emoji2vec["{x.group(0)}"]', expr)

def get_data():
    loc = os.path.join(os.path.expanduser("~"), '.emoji_embeddings')
    try:
        data = pd.read_csv(loc, skiprows=1, delimiter=' ')
    except FileNotFoundError:
        print('FIRST USE ONLY: Downloading weights and will store in', loc)
        url = 'https://raw.githubusercontent.com/uclnlp/emoji2vec/master/pre-trained/emoji2vec.txt'
        urllib.request.urlretrieve(url, loc)
        license_loc = os.path.join(os.path.expanduser("~"), '.emoji_embeddings_LICENSE')
        url = 'https://raw.githubusercontent.com/uclnlp/emoji2vec/master/LICENSE'
        urllib.request.urlretrieve(url, license_loc)
        print('Please read and cite Eisner, Ben, et al. "emoji2vec: Learning emoji representations from their description." arXiv preprint arXiv:1609.08359 (2016).')
        data = pd.read_csv(loc, skiprows=1, delimiter=' ')
    return data




@click.command()
@click.argument('expr', nargs=-1)
def app(expr):
    if len(expr) == 0:
        print('Give me some emojis please')
        return
    data = get_data()
    # normalize them
    data.iloc[:,1:-1] /= np.linalg.norm(data.iloc[:,1:-1].values, axis=0)
    my_vars = dict()
    for i in range(len(data)):
        my_vars[data.iloc[i,0]] = data.iloc[i,1:-1].values.astype(float)
    #prefix emojis because python reasons
    expr = ' '.join(expr)
    prefixed_expr = prefix_emojis(expr)
    my_locals = {}
    try:
        exec('import numpy as np; result = ' + prefixed_expr, {'emoji2vec': my_vars}, my_locals)
        result = my_locals['result']
    except Exception as e:
        print('Failed with')
        print(prefixed_expr)
        raise e
    if type(result) == np.ndarray and result.shape == (300,):
        print(expr + ' = ')
        # cosine similarity
        diff = -np.dot(data.iloc[:, 1:-1].values, result)
        si = np.argsort(diff)
        for i in range(5):
            print(i, data.iloc[si[i],0])
    else:
        print(expr + ' = ' + str(result))

if __name__ == '__main__':
    app()