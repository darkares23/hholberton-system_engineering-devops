# Load balancer
Let’s improve our web stack so that there is redundancy for our web servers. 
This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. 
If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work.
All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Starting 🚀

Ubuntu LTS - Operating system reqd.


### Prerequisites 📋

Must have git installed

Must have repository cloned

All your files will be interpreted on Ubuntu 16.

04 LTS

All your files should end with a new line

A README.md file, at the root of the folder of 
the project, is mandatory

All your Bash script files must be executable

Your Bash script must pass Shellcheck (version 0.3.7) without any error

The first line of all your Bash scripts should be exactly #!/usr/bin/env bash

The second line of all your Bash scripts should be a comment explaining what is the script doing

### Instalation 🔧

```
$ sudo apt-get install -y ruby
```
```
$ gem install puppet-lint -v 2.1.1
```
### Use 🔧
```
$ sudo puppet-lint apply 0-create_a_file.pp
```
```
$ sudo puppet apply 0-create_a_file.pp
```

## Builded in 🛠️

* bash
* VsCode

## Authors ✒️


* **Juan Sebastián Ocampo** -(https://github.com/darkares23)

## License 📄

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments 🎁

* Holberton School (providing guidance) 📢