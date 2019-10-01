### Register all custom bash aliases in this file. ###

# Executing utility managers as root by default
alias apt='sudo apt'  # Package Manager
alias service='sudo service'   # Service Manager

# Restart bash without exiting terminal
restart-bash () {
	clear
	exec bash
}

# Show System Memory Usage
alias show-memory='watch -n 5 free -m'

# Setting python v3 as default
alias python='python3'
alias pip='pip3'

# IDE aliases
alias pycharm='$HOME/IDE/Pycharm/bin/pycharm.sh'
alias webstorm='$HOME/IDE/Webstorm/bin/webstorm.sh'
alias phpstorm='$HOME/IDE/Phpstorm/bin/phpstorm.sh'
alias clion='$HOME/IDE/Clion/bin/clion.sh'
alias idea='$HOME/IDE/Idea/bin/idea.sh'

# Activate Virtual Env for python packages
activate-env(){
	source $PWD/venv/bin/activate
}

# Download any webpage
crwl(){
	sudo wget --tries=inf --timestamping --recursive --level=inf --convert-links --page-requisites --no-parent "$@"
}

# Proxy Switcher
proxy (){
	sh ~/.proxy.sh $1;
}

# ssh remote login scripts
ssh_login(){
	exec $HOME/.ssh/login_scripts/$1.sh
}

