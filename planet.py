class Planet:
    counter=0
    def __init__(self,name,radius,mass,distance,planet_type):
        self.name=name
        self.radius=radius
        self.mass=mass
        self.distance=distance
        self.planet_type=planet_type
        Planet.counter+=1
        self.id=Planet.counter
        print(f"Добавление планеты (в RAM) с ID: {self.id}")


    def __str__(self):
        return (f'~~~~~~~~~Планета~~~~~~~~~\nНазвание: {self.name}\nРадиус: {self.radius}(км)\nМасса: {self.mass}(кг)\nРасстояние до солнца: {self.distance}(км)\nТип планеты: {self.planet_type}\nID планеты: {self.id}\n~~~~~~~~~~~~~~~~~~~~~~~~~')
    def __repr__(self):
        return (f"Planet(name='{self.name}',radius={self.radius}, "
                f"mass={self.mass},distance={self.distance}, "
                f"type='{self.planet_type}',id={self.id})")

    def __eq__(self, other):
        if not isinstance(other, Planet):
            return False
        return self.name == other.name


    def __ne__(self, other):
        if not isinstance(other, Planet):
            return True
        return self.mass != other.mass


    def __lt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.distance < other.distance


    def __gt__(self, other):#необязательно, но пусть будет
        if not isinstance(other, Planet):
            return NotImplemented
        return self.distance > other.distance


    def __le__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.radius <= other.radius


    def __ge__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.mass >= other.mass

    def __copy__(self):
        return Planet(
            self.name,
            self.radius,
            self.mass,
            self.distance,
            self.planet_type
        )
    def __del__(self):
        print(f'Удаление планеты (из RAM) с ID: {self.id}')

