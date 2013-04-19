#!/usr/bin/python
import yaml

class Territory:
    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = neighbours

    def __str__(self):
        return "Territory(%s):" % self.name + ", ".join(self.neighbours)


class World:
    territories = {}

    def __init__(self, yml):
        for name in yml['world']:
            self.territories[name] = Territory(name, yml['world'][name])

    def __repr__(self):
        return "World: " + " ".join(map(lambda x: str(x), self.territories.values()))


def parse():
    with open('fixtures/3_territories.yml', 'r') as f:
        yml = yaml.load(f)

    w = World(yml)

    print w

parse()
