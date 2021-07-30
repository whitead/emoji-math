# Emoji Math
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/whitead/emoji-math/blob/master/colab/EmojiMath.ipynb)

Because why not? I put a minimal effort into this project, so please have low expectations.


```sh
pip install emath@git+git://github.com/whitead/emoji-math.git
```

## Usage

`emoji-math` computes the given python expression and returns either the value or the nearest
5 emojis as measured by cosine similarity.

```sh
>emoji-math 👑 - 🚹 + 🚺
Best Matches:
  👑-🚹+🚺 = 👸
  👑-🚹+🚺 = 👑
  👑-🚹+🚺 = 🤴
```

```sh
>emoji-math 🚹 @ 🚺
🚹 @ 🚺 = 0.32784234338655205
```

```sh
>emoji-math np.sin(🏰)
Best Matches:
  np.sin(🏰) = 🏯
  np.sin(🏰) = 🏰
  np.sin(🏰) = 👸
```

```sh
>emoji-math 🚹 + 🚺
Best Matches:
  🚹+🚺 = 🚻
  🚹+🚺 = 🚺
  🚹+🚺 = 🚹
```

## Options

You can choose between using the Euclidean distance or cosine similarity for reporting results. Cosine works better for
multiplication/division because it only cares about direction. Default is Euclidean.

```sh
>emoji-math --cosine 🚹 + 🚺
Best Matches:
  🚹+🚺 = 👚
  🚹+🚺 = 🚺
  🚹+🚺 = 🚹


## Google Colab


Start using emoji math with [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/whitead/emoji-math/blob/master/colab/EmojiMath.ipynb)

## Credit

Made by [@andrewwhite01](https://twitter.com/andrewwhite01)

Vector embeddings from [emoji2vec](https://github.com/uclnlp/emoji2vec) as described in

```bibtex
@misc{eisner2016emoji2vec,
      title={emoji2vec: Learning Emoji Representations from their Description},
      author={Ben Eisner and Tim Rocktäschel and Isabelle Augenstein and Matko Bošnjak and Sebastian Riedel},
      year={2016},
      eprint={1609.08359},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
