# USE kotoba-whisper-v2.2

![apache-2.0-license](https://img.shields.io/github/license/RyosukeDTomita/use-kotoba-whisper-v2.2)

## INDEX

- [ABOUT](#about)
- [ENVIRONMENT](#environment)
- [PREPARING](#preparing)
- [HOW TO USE](#how-to-use)

---

## ABOUT

Setting up [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) can be challenging, especially for those without IT experience.
To address this, I created this repository to provide a step-by-step guide for setting it up.

The documentation and code in this repository are licensed under the Apache License 2.0.
Please refer to the LICENSE file for details.

Note that this repository only provides usage instructions for the [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) model.
For the model’s own license is apache-2.0, please refer to its [Hugging Face page](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2).

kotoba-whisper-v2.2をセットアップするにあたって、IT経験者でない場合難しいと思う。
そのため、セットアップ手順をまとめたリポジトリを作成した。

本リポジトリのドキュメントおよびコードは Apache License 2.0 の下で公開されています（LICENSEファイル参照）。

なお、このリポジトリは [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) モデルの使用手順をまとめたものであり、モデル自体のライセンスはapache-2.0で公開されています。

---

## ENVIRONMENT

- python 3.10
- Ubuntu 22.04

---

## PREPARING

### install uv

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### install python 3.10

```shell
uv python install 3.10
uv python find
/home/sigma/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/bin/python3.10
uv python pin 3.10.18
cat .python-version
3.10.18
uv run python
Python 3.10.18 (main, Jul 23 2025, 00:36:45) [Clang 20.1.4 ] on linux
```

### set up projecct

```shell
uv init workspace
cd workspace
uv run main.py # test
```

### install dependencies

```shell
cd workspace
uv pip install --upgrade pip
uv pip install --upgrade transformers accelerate torchaudio
uv pip install "punctuators==0.0.5"
uv pip install "pyannote.audio"
uv pip install git+https://github.com/huggingface/diarizers.git
```

### HuggingFace

- create or sign in account from browser. <https://huggingface.com>

- accept the terms-of-use

> accept the terms-of-use for the following two models:
> [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)
> [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)

[!fill out form](./assets/filloutform.png)

- create a token from <https://huggingface.co/settings/tokens>

- Log in from cli

```shell
uv pip install -U "huggingface_hub[cli]"
git config --global credential.helper store
./.venv/bin/huggingface-cli login
```

### Additional libraries

```shell
sudo apt install ffmpeg
```

---

## HOW TO USE

copy and paste the [sample code](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) into sample_test.py

```shell
cd workspace
wget https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2/resolve/main/sample_audio/sample_diarization_japanese.mp3
uv run sample_test.py
```

