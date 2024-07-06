import bpy

class SetupBoxEmpty(bpy.types.Operator):
    bl_idname = "object.setup_box_empty"
    bl_label = "Setup Box Empty"

    def execute(self, context):
        bpy.ops.object.empty_add(type='CUBE')
        obj = bpy.context.selected_objects[0]
        obj.name = "cutscene_trigger_cube"
        return {'FINISHED'}
    
class SetupConeEmpty(bpy.types.Operator):
    bl_idname = "object.setup_cone_empty"
    bl_label = "Setup Cone Empty"

    def execute(self, context):
        bpy.ops.object.empty_add(type='CONE')
        obj = bpy.context.selected_objects[0]
        obj.name = "cutscene_trigger_cone"
        return {'FINISHED'}
    


class TriggerPanel(bpy.types.Panel):
    bl_idname = "TriggerPanel"
    bl_label = "Cutscene Exporter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Cutscene SM64"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.setup_box_empty", text="Add Box")
        row = layout.row()
        row.operator("object.setup_cone_empty", text="Add Cylinder")
