#!/usr/bin/env python3
import os
import subprocess
import shutil
import sys

HOME = os.path.expanduser("~")
NVIM_CONFIG = f"{HOME}/.config/nvim"
TMUX_CONF = f"{HOME}/.tmux.conf"
DOTFILES_REPO = "https://github.com/yourname/dotfiles.git"

def run(cmd):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def command_exists(cmd):
    return shutil.which(cmd) is not None

# ---------------------------
# Install Neovim
# ---------------------------
def install_nvim():
    if command_exists("nvim"):
        print("✔ Neovim already installed")
        return

    print("⏳ Installing Neovim...")
    if sys.platform.startswith("linux"):
        run("sudo apt update && sudo apt install -y neovim")
    elif sys.platform == "darwin":
        run("brew install neovim")
    else:
        print("❌ Unsupported OS")
        sys.exit(1)

# ---------------------------
# Install tmux
# ---------------------------
def install_tmux():
    if command_exists("tmux"):
        print("✔ tmux already installed")
        return

    print("⏳ Installing tmux...")
    if sys.platform.startswith("linux"):
        run("sudo apt install -y tmux")
    elif sys.platform == "darwin":
        run("brew install tmux")

# ---------------------------
# Clone configs
# ---------------------------
def setup_configs():
    if os.path.exists(f"{HOME}/dotfiles"):
        run(f"rm -rf {HOME}/dotfiles")

    run(f"git clone {DOTFILES_REPO} {HOME}/dotfiles")

    os.makedirs(f"{HOME}/.config", exist_ok=True)

    run(f"ln -sfn {HOME}/dotfiles/nvim {NVIM_CONFIG}")
    run(f"ln -sfn {HOME}/dotfiles/tmux/.tmux.conf {TMUX_CONF}")

# ---------------------------
# Alias vim -> nvim
# ---------------------------
def setup_alias():
    shell_rc = f"{HOME}/.bashrc"
    alias_line = "alias vim='nvim'"

    with open(shell_rc, "a+") as f:
        f.seek(0)
        if alias_line not in f.read():
            f.write(f"\n{alias_line}\n")

    print("✔ vim → nvim alias added")

# ---------------------------
# Main
# ---------------------------
def main():
    install_nvim()
    install_tmux()
    setup_configs()
    setup_alias()

    print("\n✅ Setup completed!")
    print("➡ Restart your shell and open nvim")

if __name__ == "__main__":
    main()

