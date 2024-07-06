import bpy

class SetupBoxEmpty(bpy.types.Operator):
    bl_idname = "object.setup_box_empty"
    bl_label = "Setup Box Empty"

    def execute(self, context):
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        obj = bpy.context.selected_objects[0]
        obj.name = "cutscene_trigger"
        return {'FINISHED'}

class TriggerPanel(bpy.types.panel):

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
        row.operator("object.setup_box_empty", text="Add Cylinder")

    def cutscene_trigger_register():
        bpy.utils.register_class(TriggerPanel)
        bpy.utils.register_class(SetupBoxEmpty)
        bpy.utils.register_class(SetupConeEmpty)


    def cutscene_trigger_unregister():
        bpy.utils.unregister_class(TriggerPanel)
        bpy.utils.unregister_class(SetupBoxEmpty)
        bpy.utils.register_class(SetupBoxEmpty)

