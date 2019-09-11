class SpaceAge(object):
    def __init__(self, seconds):
        self.earthYearInSecs = 31557600
        self.mercuryOrbital = 0.2408467
        self.venusOrbital = 0.61519726
        self.marsOrbital = 1.8808158
        self.jupiterOrbital = 11.862615
        self.saturnOrbital = 29.447498
        self.uranusOrbital = 84.016846
        self.neptuneOrbital = 164.79132
        self.seconds = seconds

    #each function takes a gievn age in secs of a person, and tells them their age on different planets in the solar system.
    def on_mercury(self):
        return round(self.seconds / self.earthYearInSecs / self.mercuryOrbital, 2)

    def on_venus(self):
        return round(self.seconds / self.earthYearInSecs / self.venusOrbital, 2)

    def on_earth(self):
        return round(self.seconds / self.earthYearInSecs, 2)

    def on_mars(self):
        return round(self.seconds / self.earthYearInSecs / self.marsOrbital, 2)

    def on_jupiter(self):
        return round(self.seconds / self.earthYearInSecs / self.jupiterOrbital, 2)

    def on_saturn(self):
        return round(self.seconds / self.earthYearInSecs / self.saturnOrbital, 2)

    def on_uranus(self):
        return round(self.seconds / self.earthYearInSecs / self.uranusOrbital, 2)

    def on_neptune(self):
        return round(self.seconds / self.earthYearInSecs / self.neptuneOrbital, 2)