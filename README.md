# 🌟 My Neovim Configuration  

This repository contains my personal Neovim setup, including plugins, keybindings, and custom configurations.  

## 👅 Installation  

### **1. Install Neovim**  
Ensure Neovim is installed on your system:  

- **Linux (Debian/Ubuntu-based)**  
  ```bash
  sudo apt install neovim
  ```  
- **Arch Linux**  
  ```bash
  sudo pacman -S neovim
  ```  
- **macOS (Homebrew)**  
  ```bash
  brew install neovim
  ```  
- **Windows (Scoop)**  
  ```powershell
  scoop install neovim
  ```  

### **2. Clone This Repo**  
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git ~/.config/nvim
```

### **3. Install Plugin Manager (If Needed)**  

#### **Lazy.nvim (Recommended)**  
```bash
mkdir -p ~/.local/share/nvim/lazy
git clone --filter=blob:none https://github.com/folke/lazy.nvim.git ~/.local/share/nvim/lazy/lazy.nvim
```

#### **Packer.nvim (Alternative)**  
```bash
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

### **4. Open Neovim and Install Plugins**  

- **Lazy.nvim**  
  ```vim
  :Lazy sync
  ```
- **Packer.nvim**  
  ```vim
  :PackerSync
  ```
- **Vim-Plug**  
  ```vim
  :PlugInstall
  ```

### **5. Restart Neovim**  
Close and reopen Neovim to apply the changes.  

---

## 🛠 Features  
- Custom keybindings  
- Theme and UI enhancements  
- Plugin manager support (Lazy.nvim/Packer.nvim)  
- LSP and autocomplete setup  
- Syntax highlighting  

---

## 📌 To-Do  
- [ ] Improve documentation  
- [ ] Optimize startup time  
- [ ] Add more keybindings  

---

## 💚 License  
This configuration is free to use and modify. Happy coding! 🚀  


