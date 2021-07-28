# Emoji Math

Because why not?


```sh
pip install emath@git+git://github.com/whitead/emoji-math.git
```

## Usage

```sh
$ emoji-math 👑 - 🚹 + 🚺
👑 - 🚹 + 🚺 =
0 👑
1 👸
2 🏰
3 🎎
4 💂
```

```sh
$ emoji-math 🚹 @ 🚺
🚹 @ 🚺 = 0.32784234338655205
```

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