# 🧰 Portable Neovim + tmux Setup

This repository allows me to reproduce **exactly the same development environment** (Neovim + tmux) on **any machine** using a single Python script.

The setup is **clean, reproducible, and safe**:
- Installs **Neovim** if missing
- Installs **tmux** if missing
- Sets `vim` → `nvim` alias
- Downloads and applies my configs automatically
- Works on Linux (Ubuntu/Debian) and macOS

---

## 📁 Repository Structure

```text
dotfiles/
├── nvim/
│   ├── init.lua
│   └── lua/
│       └── ...
├── tmux/
│   └── .tmux.conf
├── setup_env.py
└── README.md

git clone https://github.com/aelasefa/config-nvim.git
cd config-nvim


