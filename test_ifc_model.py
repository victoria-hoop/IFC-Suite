from bimify.ifc_modeling import IFCModelHandler
from shapely.geometry import Polygon

# Dummy classes
class DummyWall:
    def __init__(self, id, polygon):
        self.id = id
        self.polygon = polygon
        self.ifc_element = None

class DummyRoomCategory:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color

class DummyRoom:
    def __init__(self, id, name, polygon, category):
        self.id = id
        self.name = name
        self.polygon = polygon
        self.category = category
        self.ifc_element = None

# Dummy data
walls_list = [
    DummyWall(1, Polygon([(0, 0), (0, 5), (5, 5), (5, 0)])),
    DummyWall(2, Polygon([(5, 0), (5, 5), (10, 5), (10, 0)])),
    DummyWall(3, Polygon([(30, 0), (30, 30), (30, 30), (50, 0)]))
]

room_category = DummyRoomCategory(0, "Living Room", (0.5, 0.8, 0.5))
rooms = [
    DummyRoom(1, "Room A", Polygon([(0.5, 0.5), (0.5, 4.5), (4.5, 4.5), (4.5, 0.5)]), room_category),
    DummyRoom(2, "Room B", Polygon([(5.5, 0.5), (5.5, 4.5), (9.5, 4.5), (9.5, 0.5)]), room_category)
]

# Run the IFC model creation
handler = IFCModelHandler()
handler.create_project()
#handler.load_library_file()
handler.create_ifc_walls_from_polygons(walls_list)
handler.create_ifc_spaces_from_enclosed_areas(rooms)
handler.save_ifc()

print("✅ Dummy IFC model created and saved.")
