# Plant-Disease-Prediction

This project is about predicting plant disease from an image. The project contains fron end and backend operation. The dataset are collected from PiAnalytix and prediction is done with Convolution Neural network. here is the organization of the files:

* Plant_Disease_Prediction.ipynb - Backend Operation
* plant_disease.h5 - Backend Operation
* Requirements.txt - Frontend Operation
* Main_app.py - Frontend Operation

zip file contains the sample image data to predict plant disease. For this project concerning the volume plant disease is limited to:

* Corn common rust
* Potato early blight
* Tomato Bacterial spot

After running ipynb file, .h5 file is generated for transfer learning. Then in terminal following command are executed:

* pip install -r requirement.txt
* streamlit run main_app.py

After running those command the app will appear in browser as app_screen.png shows.

![app_screen](https://user-images.githubusercontent.com/70243598/172761686-1913d184-0fbf-4290-99dd-903f521ecaaf.png)
