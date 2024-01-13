# music-popularity-prediction
ML project about the prediction of the popularity of a song

![](images.jpg)

## 1 - Problem description

These days, digital music offers endless opportunities for access, dissemination and sharing. In addition to being an excellent tool for the user, it can also be an excellent tool for the artist and the record company, who can exploit the data received from the user, analyzing it to create models to adapt the music to the user, as well as being able predict whether the developed text will be successful.

---
## 2 - The Goal

The target of this project is to create a model to predict the popularity of a song.

--- 

## 3 - Data

This repository is based on the following kaggle dataset: https://www.kaggle.com/datasets/thedevastator/spotify-tracks-genre-dataset/
This dataset provides comprehensive information about Spotify tracks encompassing a diverse collection of 125 genres. It has been compiled and cleaned using Spotify's Web API and Python. Presented in CSV format, this dataset is easily accessible and amenable to analysis. The dataset comprises multiple columns, each representing distinctive audio features associated with individual tracks. 
The file spotify.csv contains the data to build a machine learning models based on the Spotify Tracks Genre Dataset

artists: The name(s) of the artist(s) associated with the track. (String)
album_name: The name of the album that the track belongs to. (String)
track_name: The name of the track. (String)
popularity: The popularity score of the track on Spotify, ranging from 0 to 100. (Integer)
duration_ms: The duration of the track in milliseconds. (Integer)
explicit: A boolean value indicating whether the track contains explicit content. (Boolean)
danceability: A score ranging from 0 to 1 that represents how suitable a track is for dancing based on various musical elements. (Float)
energy: A measure of the intensity and activity of a track, ranging from 0 to 1. (Float)
key: The key of the track represented by an integer value. (Integer)
loudness: The loudness of the track in decibels (dB). (Float)
mode: The tonal mode of the track, represented by an integer value (0 for minor, 1 for major). (Integer)
speechiness: A score ranging from 0 to 1 that represents the presence of spoken words in a track. (Float)
acousticness: A score ranging from 0 to 1 that represents the extent to which a track possesses an acoustic quality. (Float)
instrumentalness: A score ranging from 0 to 1 that represents the likelihood of a track being instrumental. (Float)
liveness: A score ranging from 0 to 1 that represents the presence of an audience during the recording or performance of a track. (Float)
valence: A score ranging from 0 to 1 that represents the musical positiveness conveyed by a track. (Float)
tempo: The tempo of the track in beats per minute (BPM). (Float)
time_signature: The number of beats within each bar of the track. (Integer)
track_genre: The genre of the track. (String)

I uploaded the entire dataset to the repository. File: *spotify.csv* in the data folder.
This data is processed using the ``train.py`` file archive in the main folder.

After EDA, i decided to delete some columns based on the redundant value already present in the dataset. I cut:
- Unnamed: 0, index not named, not useful
- track_id, id of the song for spotify. Not useful

---

## 4 - Structure of the repository

### DATASET
- **spotify.csv**: contains the full dataset, it is in the folder 'data'

### Files
- **Proj2.ipynb**: contains the notebook to explore the data and choose the model with the best results
- **Pipfile and Pipfile.lock**: contains the dependencies to run the repo
- **predict.py**: contains the prediction using flask
- **test.py**: contains some values to test the model
- **song_model.bin**: this is the model got from the train.py using Pickle
- **train.py**: contains the model with the best performance in the testing set, obtained using the notebook
- **Dockerfile**: contains the image for the docker

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
git clone https://github.com/bergimax/music-popularity-prediction/
```
- Move into the project's folder, running :
``` 
cd music-popularity-prediction
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
docker build -t pop_prediction .
```
- Run the docker image created:
```
docker run -it --rm -p 9696:9696 pop_prediction:latest
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

The model is build using saturn cloud (https://saturncloud.io/ ) because it required a lot of computational memory. If you run train.py you can have error on memory space allocate, it is bypassed using this amazing environment
