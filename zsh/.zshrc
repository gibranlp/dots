#!/usr/bin/env bash
# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
# 
#
export ZSH=$HOME/.oh-my-zsh
ZSH_THEME="agnoster"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
ZSH_THEME_RANDOM_CANDIDATES=(agnoster avit passion)

# Uncomment the following line to use case-sensitive completion.
CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
export UPDATE_ZSH_DAYS=30

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
#ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
HIST_STAMPS="yyyy/mm/dd"


plugins=(archlinux
	colored-man-pages
	zsh-autosuggestions
	zsh-syntax-highlighting
	git
	colorize
	command-not-found
	docker
	docker-compose
	hitchhiker)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
export LANG=en_US.UTF-8

## Aliases
alias ..='cd ..'
alias rr='curl -s -L https://raw.githubusercontent/keroserene/rickrollrc/master/roll.sh | bash'
alias neofetch="neofetch --jp2a logo_cli.png"
eval $(thefuck --alias)
alias lzd="lazydocker"
alias tsm="transmission-remote"
alias sshelgen="ssh -i ~/.ssh/rsa_deploy itadmin@199.85.208.94"
alias podacidez="poddl https://anchor.fm/s/a90d4be4/podcast/rss /media/Music/Podcasts/Acidez"
alias podcreepy="poddl 'https://www.patreon.com/rss/creepyenespanol?auth=g6v8v5ael8aEJm3MtDOSyuJ_NDPjJgTw' /media/Music/Podcasts/Creepy"
alias podwhy="poddl https://anchor.fm/s/89358408/podcast/rss /media/Music/Podcasts/WhyFiles"
alias podcensura="poddl http://www.poderato.com/mesembriarecords/_feed/1 /media/Music/Podcasts/Radiocensura"
export PATH=~/.local/bin:$PATH
export PATH=~/cli-tools/:$PATH
setxkbmap -layout us -variant intl
wal -R -q
echo " "$(( (`date +%s` - `date +%s -d '2003/08/1'`) / 86400)) "󱚦 "$(( (`date +%s` - `date +%s -d '2022/02/19'`) / 86400)) " "$(( (`date +%s` - `date +%s -d '2022/08/15'`) / 86400 )) " "$(( (`date +%s` - `date +%s -d '2023/08/14'`) / 86400 )) "󰞬 "$(( (`date +%s -d '2025/07/5'` - `date +%s`) / 86400))
#neofetch
hitchhiker | cowsay