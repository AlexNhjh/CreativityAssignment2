def collide(mass1, mass2, velocity1, velocity2):
    v1new = (((mass1 - mass2) * velocity1) + 2 * (mass2 * velocity2)) / (mass1+mass2)
    v2new = (((mass2 - mass1) * velocity2) + 2 * (mass1 * velocity1)) / (mass1 + mass2)
    return v1new, v2new


mass1 = 1
mass2 = 2
velocity1 = 30
velocity2 = -20

print(collide(mass1, mass2, velocity1, velocity2))