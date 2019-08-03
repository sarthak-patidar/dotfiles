###README FOR VAULT


* Version 2.0.8
* Python Version : 3.6
* Author: Sarthak Patidar <sarthakpatidar15@gmail.com>


## Dependencies

* Mongodb ('pip install pymongo' to install mongodb driver for python)


## Usage

* Logging into the vault
    * vault -u {username} -p

* After Login (Available Commands)
    * Saving a credential: save {vendor_name} '{comments}'
    * Viewing a saved credential: see {vendor_name}
    * delete a credential: delete {vendor_name}
    * update a credential: update {vendor_name} -options
        * Options available: username, password & comments
    * Create a user: create -superuser (makes a superuser)
    * help : help <command>
    * Exit Vault: quit or ctrl+c