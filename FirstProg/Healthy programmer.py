import time
from pygame import mixer


def getdate():
    import datetime
    return datetime.datetime.now()


sleepTime = 60


def IsOfficeTime(current_time):
    if current_time > '09:00' and current_time < '17:01':
        return True
    else:
        return False


WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()

WaterAfterEvery = 1200  # Seconds  - 20 minutes
EyeExerciseAfterEvery = 1800  # Seconds - 30 minutes
PhysicalExerciseAfterEvery = 2700  # Seconds  - 45 minutes


def water():
    mixer.init()
    mixer.music.load("water.mp3")  # Loading the song
    mixer.music.set_volume(0.7)  # Setting the volume
    mixer.music.play()


def eyes():
    mixer.init()
    mixer.music.load("eyes-exercise.mp3")  # Loading the song
    mixer.music.set_volume(0.7)  # Setting the volume
    mixer.music.play()


def health_exercise():
    mixer.init()
    mixer.music.load("health-exercise.mp3")  # Loading the song
    mixer.music.set_volume(0.7)  # Setting the volume
    mixer.music.play()


def stop_music():
    mixer.music.stop()


named_tuple = time.localtime()  # get struct_time
current_time = time.strftime("%H:%M", named_tuple)

while (IsOfficeTime(current_time)):
    if (time.time() - WaterTakenAt) > WaterAfterEvery:
        while True:
            water()
            value = "done"
            input1 = str(input("type done to stop music  "))
            if value == input1:
                stop_music()
                with open("water.txt", "a") as op:
                    op.write(str([str(getdate())]) + ": " + "Drank" + "\n")
                    WaterTakenAt = time.time()
                    break
            else:
                print("type 'done' to stop music")

    if (time.time() - EyeExerciseAt) > EyeExerciseAfterEvery:
        while True:
            eyes()
            value = "done"
            input1 = str(input("type done to stop music  "))
            if value == input1:
                stop_music()
                with open("eyes.txt", "a") as op:
                    op.write(str([str(getdate())]) + ": " + "EyDone" + "\n")
                    EyeExerciseAt = time.time()
                    break
            else:
                print("type 'done' to stop music")

    if (time.time() - PhysicalExerciseAt) > PhysicalExerciseAfterEvery:
        while True:
            health_exercise()
            value = "done"
            input1 = str(input("type done to stop music  "))
            if value == input1:
                stop_music()
                with open("physical_ex.txt", "a") as op:
                    op.write(str([str(getdate())]) + ": " + "PyDone" + "\n")
                    PhysicalExerciseAfterEvery = time.time()
                    break
            else:
                print("type 'done' to stop music")
time.sleep(sleepTime)

