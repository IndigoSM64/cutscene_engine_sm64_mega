import bpy
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "Cutscene Engine SM64",
    "blender": (4, 0 ,2),
    "category": "Import/export",
    "version": (0, 1),
    "author": "IndigoSM64 & C0c0 San",
    "description": "Cutscene Engine SM64 is a blender addon that add cutscene to SM64 ! WARNING: YOU MUST USE FAST64"
}

from .cutscene_trigger_exporter import cutscene_trigger_register
from .cutscene_trigger_exporter import cutscene_trigger_unregister

def register():
    cutscene_trigger_register()

def unregister():
    cutscene_trigger_unregister()