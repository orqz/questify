<p align="center">
  <img 
    src="https://i.pinimg.com/originals/b6/07/6b/b6076bb4df9a3532e01ad33b4e563643.jpg"
    style="width:1000px; height:250px; object-fit:cover;"
  >
</p>

<h1 align="center">Questify</h1>

<p align="center">
  Easily complete Quest on discord without downloading or owning any games!<br>
  (took me 30 minutes)
</p>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/github/v/release/orqz/questify?style=for-the-badge&cacheSeconds=3600">
  <img src="https://img.shields.io/github/downloads/orqz/questify/total?style=for-the-badge&cacheSeconds=86400&v=2">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge">
</p>



---

## About

Questify is a simple Python tool that generates a custom `.exe`
with a matching folder name so Discord detects it as a running game.

---

## Features

- creates an exe
- creates the folder
- what else do u expect?

---

## Installation

### Download (recommended)

Download the latest ready-to-use `.exe` from [Releases](https://github.com/orqz/questify/releases):

No setup required. Just download and run.

---

### Don’t trust the `.exe`? (fair i wouldnt either)

You can compile the source yourself using PyInstaller.

### Step 1 — Install dependencies

```bash
pip install requests pyinstaller
```

### Step 2 — Build the executable

```bash
pyinstaller --onefile questify.py
```

### Step 3 — Done

Your compiled file will be created here:

```
dist/questify.exe
```

Run it like any normal program.

---

## Warning

> **Important**
> The executable must be named `questify.exe`.
> Any other name will cause the program to not work correctly.



