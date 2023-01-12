ONGOING

Geocluster: using clustering to get better insights on Berlin and its social context

This is a project I created in order to enable an easier access to the data we collected for our <a href="https://github.com/Safiaaaaa/YouthInTheCity">final project<a> at Le Wagon's Data Science Bootcamp. 

The result is this <a href="https://safiaaaaa-geocluster-geoclusterapp-qr2sk7.streamlit.app/">webapp<a>, where you can plot the distribution of 100 features on Berlin's social and infrastructural landscape - and use clustering to get more insight on how they interact with each other. You'll find more information on the method employed in the description text.

The data was obtained from Berlin Open Data Platform and Openstreetmap and aggregated to the level of the 542 Berliner Plannungsräume (planning areas), the smallest statistical areas on which social data is publicly available. 6 areas were excluded of the analysis due to a too little amount of observations.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for TaxiFareModel in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/TaxiFareModel`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "TaxiFareModel"
git remote add origin git@github.com:{group}/TaxiFareModel.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
TaxiFareModel-run
```

# Install

Go to `https://github.com/{group}/TaxiFareModel` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/TaxiFareModel.git
cd TaxiFareModel
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
TaxiFareModel-run
```
