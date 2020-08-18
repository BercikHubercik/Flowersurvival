

class FlowerBase():
    def __init__(self, filename):
        self.filename = filename
        self.plants = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.plants = {}

        for line in self.file:
            plantName, waterFreq, lastWaterdate, lastWaterhour = line.split(";")
            self.plants[plantName] = (waterFreq, lastWaterdate, lastWaterhour)

        self.file.close()

    def add_plant(self, plantName, waterFreq, lastWaterdate, lastWaterhour):

        self.plants[plantName] = (waterFreq, lastWaterdate, lastWaterhour)
        self.save()


    def save(self):
        with open(self.filename, "w") as f:
            for plant in self.plants:
                f.write(str(plant) + ";" + str(self.plants[plant][0]) + ";" + str(self.plants[plant][1]) + ";" + str(self.plants[plant][2]) + "\n")
