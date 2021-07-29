import pandas as pd
import numpy as np
import re
import click
import sys
import os
import urllib.request


def prefix_emojis(expr, emoji_list):
    expr_s = list(expr)
    for i in range(len(expr_s)):
        if expr_s[i] in emoji_list:
            expr_s[i] = f'emoji2vec["{expr_s[i]}"]'
    return ''.join(expr_s)


def get_data():
    loc = os.path.join(os.path.expanduser("~"), '.emoji_embeddings')
    try:
        data = pd.read_csv(loc, skiprows=1, delimiter=' ')
    except FileNotFoundError:
        print('FIRST USE ONLY: Downloading weights and will store in', loc)
        url = 'https://raw.githubusercontent.com/uclnlp/emoji2vec/master/pre-trained/emoji2vec.txt'
        urllib.request.urlretrieve(url, loc)
        license_loc = os.path.join(os.path.expanduser(
            "~"), '.emoji_embeddings_LICENSE')
        url = 'https://raw.githubusercontent.com/uclnlp/emoji2vec/master/LICENSE'
        urllib.request.urlretrieve(url, license_loc)
        print('Please read and cite Eisner, Ben, et al. "emoji2vec: Learning emoji representations from their description." arXiv preprint arXiv:1609.08359 (2016).')
        data = pd.read_csv(loc, skiprows=1, delimiter=' ')
    # normalize emoji vectors
    data.iloc[:, 1:-1] /= np.linalg.norm(data.iloc[:, 1:-1].values, axis=0)
    emojis = set(data.iloc[:, 0].values)
    return data, emojis


def emoji2vec_dict(data):
    emoji2vec = dict()
    for i in range(len(data)):
        emoji2vec[data.iloc[i, 0]] = data.iloc[i, 1:-1].values.astype(float)
    return emoji2vec


def topk_emojis(v, data, k=5):
    '''topk vectors via cosine'''
    v /= np.linalg.norm(v)
    diff = -np.dot(data.iloc[:, 1:-1].values, v)
    si = np.argsort(diff)
    result = [data.iloc[si[i], 0] for i in range(k)]
    return result


def exec_emojis(expr, data=None, emojis=None):
    if data is None:
        data, emojis = get_data()

    # prefix emojis because python reasons
    prefixed_expr = prefix_emojis(expr, emojis)
    my_locals = {'emoji2vec': emoji2vec_dict(data), 'np': np}
    try:
        exec('result = ' + prefixed_expr, my_locals)
        result = my_locals['result']
    except Exception as e:
        print('Failed with')
        print(prefixed_expr)
        if type(e) is SyntaxError:
            raise ValueError('Unsupported emoji in "' + prefixed_expr + '"')
        else:
            raise e
    return result


def format_result(result, data, prefix=''):
    str_result = [prefix]
    if type(result) == np.ndarray and result.shape == (300,):
        # cosine similarity
        topk = topk_emojis(result, data)
        for i, e in enumerate(topk):
            str_result.append(f'{i}. {e}')
    else:
        str_result.append(str(result))
    return '\n'.join(str_result)


@click.command()
@click.argument('expr', nargs=-1)
@click.option('--supported/', default=False, is_flag=True)
def app(expr, supported):
    if len(expr) == 0 and not supported:
        print('Give me some emojis please')
        return
    data, emojis = get_data()
    if supported:
        print('Here are all emojis supported')
        print(emojis)
        return
    expr = ''.join(expr)
    result = exec_emojis(expr, data, emojis)
    message = format_result(result, data, expr + ' = ')
    print(message)


if __name__ == '__main__':
    app()
