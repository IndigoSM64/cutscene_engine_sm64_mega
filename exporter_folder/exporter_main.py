from .exporter_trigger import ExportTriggers
import bpy 

def register_export():
    bpy.utils.register_class(ExportTriggers)

def unregister_export():
    bpy.utils.unregister_class(ExportTriggers)