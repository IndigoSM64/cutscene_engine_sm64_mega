bl_info = {
    "name": "Cutscene Engine SM64",
    "blender": (4, 0, 2),
    "category": "Import/Export",
    "version": (0, 1),
    "author": "IndigoSM64 & C0c0 San",
    "description": "Cutscene Engine SM64 is a Blender addon that adds cutscenes to SM64! WARNING: YOU MUST USE FAST64"
}

import bpy

from .cutscene_engine import cutscene_engine_register, cutscene_engine_unregister
from .add_form import add_box_register, add_box_unregister
from .exporter_folder.exporter_main import register_export, unregister_export




def register():
    add_box_register()
    cutscene_engine_register()
    register_export()


def unregister():
    add_box_unregister()
    cutscene_engine_unregister()
    unregister_export()

if __name__ == "__main__":
    register()
