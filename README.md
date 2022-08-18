##  Attendance Management system using Face👦🏻👧 Recognition [![](https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg)](https://github.com/Spidy20/Attendace_management_system/blob/master/LICENSE)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.10.6](https://img.shields.io/badge/python-3.10.6-blue.svg)](https://www.python.org/ftp/python/3.10.6/)
### Sourcerer
<a href="https://github.com/erahulkumar"><img src="https://avatars.githubusercontent.com/u/91170678?s=96&v=4" style="border-radius: 50%;" height="50px" width="50px" alt="erahulkumar"/></a>

### Code Requirements
* Opencv(`pip install opencv-python`)
* Tkinter(Available in python)
* PIL (`pip install Pillow`)
* Pandas(`pip install pandas`)

### What steps you have to follow??
* Download my Repository 
- Create a `TrainingImage` folder in a project.
- Open a `SAS_Runner.py` and change the all paths with your system path
- Run `SAS_Runner.py`.

### Project Structure

- After run you need to give your face data to system so enter your ID and name in box than click on `Take Images` button.
- It will collect 200 images of your faces, it save a images in `TrainingImage` folder
- After that we need to train a model(for train a model click on `Train Image` button.
- It will take 5-10 minutes for training(for 10 person data).
- After training click on `Automatic Attendance And Seat Allotment` ,it can fill attendace by your face using our trained model (model will save in `TrainingImageLabel` )
- it will create `.csv` file of attendance according to time & subject.
- You can store data in database (install wampserver),change the DB name according to your in `AMS_Run.py`.
- `Manually Fill Attendace` Button in UI is for fill a manually attendance (without facce recognition),it's also create a `.csv` and store in a database.

### Screenshots

### Basic UI
<img src="https://github.com/erahulkumar/Seat-Allotment-System-based-Face-Recognition/blob/main/Att.png">

### Next Step
<img src="https://github.com/erahulkumar/Seat-Allotment-System-based-Face-Recognition/blob/main/Screenshot%20(10).png">

### Next Step 
<img src="https://github.com/erahulkumar/Seat-Allotment-System-based-Face-Recognition/blob/main/Screenshot%20(11).png">

### Manually attendance filling UI
<img src="https://github.com/erahulkumar/Seat-Allotment-System-based-Face-Recognition/blob/main/Screenshot%20(12).png">


### How it works? See:)

<img src="https://youtu.be/9kz-GF7XoEs">

### Video demo




### Notes
- It will require high processing power(I have 8 GB RAM & 2 GB GC)
- If you think it will recognise person just like humans,than leave it ,its not possible.
- Noisy image can reduce your accuracy so quality of images matter.

## Just follow☝️ me and Star⭐ my repository
