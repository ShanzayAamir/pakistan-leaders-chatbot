---
title: Pakistan Leaders Chat
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
---

# 🇵🇰 Pakistan Political Leaders AI

An interactive chat demo powered by a **fine-tuned TinyLlama** model trained on Wikipedia data about Pakistani political leaders...

## 🧠 Model Details

| Detail | Info |
|---|---|
| **Base Model** | TinyLlama-1.1B-Chat-v1.0 |
| **Fine-tuning Method** | LoRA (PEFT) |
| **Dataset** | ~2,500 samples scraped from Wikipedia (Pakistani political leaders) |
| **Format** | ChatML |
| **Model Repo** | [Hamzasajjad38/pakistan-leaders-tinyllama-peft-merged](https://huggingface.co/Hamzasajjad38/pakistan-leaders-tinyllama-peft-merged) |

## 💬 What You Can Ask

- Biographies of Pakistani political leaders (Imran Khan, Benazir Bhutto, Nawaz Sharif, etc.)
- Political careers, parties, and tenures
- Historical contributions and controversies
- General Pakistani political history

## ⚙️ Tech Stack

- **Framework**: Gradio
- **Inference**: 🤗 Transformers + PyTorch
- **Fine-tuning**: PEFT / LoRA

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

---

Built by **Muhammad Hamza Sajjad** | MPhil Data Science, Punjab University