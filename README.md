# Blogging Website using Django Framework

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. <!-- See deployment for notes on how to deploy the project on a live system.-->

### Prerequisites
Clone the repository to get a copy for yourself
```
$ git clone https://github.com/mohapeameya/django-blogpost-app.git
```
Change current directory to ```django-blopost-app```
```
$ cd django-blogpost-app
```
Install the following dependencies if not already installed
```
$ sudo apt install python3 python3-pip python3-dev python3-venv python3-distutils -y
```


### Installing

Create a virtual environment for this project
```
$ python3 -m venv env
```
Activate the virtual environment
```
$ source env/bin/activate
```
Upgrade ```pip``` for the virtual environment
```
$ python3 -m pip install --upgrade pip
```
Install requirements using pip from ```requirements.txt``` file
```
$ python3 -m pip install -r requirements.txt
```
Create a Gmail account to manage password recovery system of the website.   
The email and its app password will be used as ```EMAIL_HOST_USER``` and ```EMAIL_HOST_PASSWORD``` respectively.  
Enable app password for this account
````
Gmail > Account > Security > App passwords
````

Create ```.env``` file to configure environment variables for ```settings.py```
```
$ vim blogpost/.env
```
Set the following environment variables in the ```.env``` file as ```VAR=value```  
General: ```DEBUG```, ```SECRET_KEY```  
Email: ```EMAIL_HOST_USER```, ```EMAIL_HOST_PASSWORD```  
Don't forget to add this file to ```.gitignore```  

Create the necessary database tables
```
$ python3 manage.py migrate
```
Create super user for the website
```
$ python3 manage.py createsuperuser
```
Goto http://127.0.0.1:8000/admin/ to access site administration using credentials created with the above command.  
  
Run development server
```
$ python3 manage.py runserver
```
Goto http://127.0.0.1:8000 to check it out


<!--## Running the test-->

<!--Explain how to run the automated tests for this system-->

<!--### Break down into end to end tests-->

<!--Explain what these tests test and why-->

<!--### And coding style tests-->

<!--Explain what these tests test and why-->

<!-- ## Deployment-->

<!--Add additional notes about how to deploy this on a live system-->

## Built With

* [django](https://www.djangoproject.com) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

<!--## Contributing-->

<!--Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.-->

<!--## Versioning-->

<!--We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). -->

<!--## Authors-->

<!--* **Ameya Mohape** - *Initial work* - [mohapeameya](https://github.com/mohapeameya)-->

<!--See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.-->

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE](LICENSE) file for details

<!--## Acknowledgments
* Hat tip to anyone whose code was used
* Inspiration
* etc-->
