# music-popularity-prediction
ML project about the prediction of the popularity of a song

![](images.jpg)

## 1 - Problem description



---
## 2 - The Goal

The target of this project is to predict the popularity of a song.

--- 

## 3 - Data




I uploaded the entire dataset to the repository. File: *spotify.csv* in the data directory.
This data is processed using the ``train.py`` file archive in the main folder.

After EDA, i decided to delete some columns based on the redundant value already present in the dataset. I cut:
- 

---

## 4 - Structure of the repository

### DATASET
- **player_data.csv**: contains the full dataset, it is in folder named 'data'

### Files
- **Proj1.ipynb**: contains the notebook to explore the data and choose the model with the best results
- **Pipfile and Pipfile.lock**: contains the dependencies to run the repo
- **predict.py**: contains the prediction using flask
- **test.py**: contains some values to test the model
- **player_model.bin**: this is the model got from the train.py using Pickle
- **train.py**: contains the model with the best performance in the testing set, obtained using the notebook
- **Dockerfile**: contains the image for the docker

### Folder '**Proof of working**'
- **docker running.png**: screenshot of the docker built running
- **docker_running.mp4**: video of the docker built running and the prediction
- **flask running.png**: screenshot of the flask app running in local
- **flask_running.mp4**: video of the flask built running and the prediction
- **gunicorn running.mp4**: video of the gunicorn built running and the prediction

---
## 5 - Loading final model into a service:

#### pipenv 

The script *train.py* load the model : *player_model.bin* and it can run in a separate virtual environment across its dependency files *Pipenv* and *Pipenv.lock*.
*flask* was used for the local deployment in *train.py* script.

- Install pipenv :
```
pip install pipenv
```
- Get a copy of project and dependencies, or clone the repository :
```
git clone https://github.com/bergimax/footballer-value/
```
- From the project's folder, run :
``` 
pipenv install
```
- All the dependencies should be automatically soddisfied, just verify.
- Run the local service using gunicorn inside the virtual environment:
```
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```

#### Docker
There is also the file: *Dockerfile* in the repository, through this you can run the service in a completely separate container. To run the Docker, be sure your docker service is running. If you are using wsl2 on Windows, to run the build command you need to make sure your docker dekstop is running, otherwise you will get an error. 
For the docker, you have to:

- From the project directory, create the docker image :
```
docker build -t player_prediction .
```
- Run the docker image created:
```
docker run -it --rm -p 9696:9696 player_prediction:latest
```
The build command can take several minutes to run. Just give it time.

#### Test the local service:

- To test the local service, you can run the test script in another terminal:
```
python test.py
```
- If you edit the market values to analize some data, you should modify the parameters in the file test.py, maybe you cane take them from the smaller dataset present in this repo of each market:
```
vi test.py
```
P.S: The current values in test.py are taken from the dataset, raw number 2075.

---

#### Video of the service running :
I loaded a small video where you can see how the service works, everything it's in the 'Proof of working' folder.

The video show the local service starting in Docker and how it respond to the test.py
I also attached the screenshot of the service running with flask and gunicorn.
