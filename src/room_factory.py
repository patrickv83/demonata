from random import choice
from importlib import import_module
from room import Room
from artifact_room import ArtifactRoom
from enemy_room import EnemyRoom

class RoomFactory(object):
    # Create Room
    @staticmethod
    def create(x, y, text):
        roomTypes = Room.__subclasses__()
        roomTypes.append(Room)
        return roomTypes[choice(roomTypes)](x, y, text)
        except NameError:
            assert 0, "No such room type: " + roomType

