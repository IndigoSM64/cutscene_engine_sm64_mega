bl_info = {
    "name": "Cutscene Engine SM64",
    "blender": (4, 0, 2),
    "category": "Import/Export",
    "version": (0, 1),
    "author": "IndigoSM64 & C0c0 San",
    "description": "Cutscene Engine SM64 is a Blender addon that adds cutscenes to SM64! WARNING: YOU MUST USE FAST64"
}

import bpy

from .cutscene_engine import SetupBoxEmpty, TriggerPanel, SetupConeEmpty

def register():
    bpy.utils.register_class(SetupBoxEmpty)
    bpy.utils.register_class(SetupConeEmpty)

    bpy.utils.register_class(TriggerPanel)

def unregister():
    bpy.utils.unregister_class(SetupBoxEmpty)
    bpy.utils.register_class(SetupConeEmpty)

    bpy.utils.unregister_class(TriggerPanel)

if __name__ == "__main__":
    register()
