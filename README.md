#The easiest way to customize the project

1. Install last version of pipenv: pip install pipenv

2. Create new env: pipenv --three

3. Activate particular environment: pipenv shell

4. If you use Pycharm, set path to the Project Interpreter on Settings -> Project -> Project Interpreter -> ..Add -> existing environment/..way for your Python.exe (C:/Users/{User}/.virtualenvs/{created_virtualenv}/Scripts/Python.exe) 

5. Next command will install all packages from Pipfile file (should be executed only once) pipenv install --dev

6. Add permission for sh file (for only Linux system): chmod +x run.sh

7. Run tests ./run.sh