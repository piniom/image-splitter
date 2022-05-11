# image-splitter
This is a quick side project.
The app uses cv2 to extract individual images from a single picture, like a scan of a couple of photos, or a photo of some pictures hanging on the white wall.
To run the app place your photos in the ```images-source``` folder and run:
```
python src/app.py
```
The output should appear in the ```images-target``` folder. <br>
The extraction algotihm's parameters (mainly ```RADIUS``` and ```THRESHOLD```) can be changed in the ```src/app.py``` file.
