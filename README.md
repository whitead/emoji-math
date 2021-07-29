# Emoji Math

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

## Google Colab

Start using emoji math with [Google Colab](https://colab.research.google.com/github/whitead/emoji-math/blob/master/colab/EmojiMath.ipynb)

## Credit

Made [@andrewwhite01](https://twitter.com/andrewwhite01)

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
