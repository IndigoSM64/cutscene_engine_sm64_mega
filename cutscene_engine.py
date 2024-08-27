import bpy


    


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
        row = layout.row()
        row.operator("object.setup_parent_trigger", text="Add Trigger Parent")
        row = layout.row()
        row.operator("object.export_triggers", text="Export Trigger")


def register_properties():
    bpy.types.Object.cynematic_number_prop = bpy.props.IntProperty(
        name="Value Cutscene",
        description="Enter your value for your cutscene",
        default=0,
        min=0,  
        max=255
    )

    bpy.types.Object.is_a_cutscene_trigger = bpy.props.BoolProperty(
        name="Its a cutscene Trigger",
        description="Allow the object to be a cutscene trigger",
        default=False
    )

    bpy.types.Object.cutscene_trigger_area = bpy.props.IntProperty(
        name="Trigger Area",
        description="Enter the area of the trigger",
        default=0,
        min=0,
        max=255
    )

    bpy.types.Object.is_a_parent_trigger = bpy.props.BoolProperty(
        name="Trigger Area",
        description="Enter the area of the trigger",
        default=False,
    )

def unregister_properties():
    del bpy.types.Object.cynematic_number_prop


class OBJECT_PT_my_custom_panel(bpy.types.Panel):
    bl_label = "Trigger Number"
    bl_idname = "OBJECT_PT_my_custom_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    
    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'EMPTY'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if obj.is_a_cutscene_trigger:
            layout.prop(obj, "cynematic_number_prop")
            layout.prop(obj, "areaIndex")
        else: 
            layout.label(text="This object is not a cutscene trigger")
        

    


def cutscene_engine_register():
    register_properties()
    bpy.utils.register_class(TriggerPanel)
    bpy.utils.register_class(OBJECT_PT_my_custom_panel)


def cutscene_engine_unregister():
    unregister_properties()
    bpy.utils.unregister_class(TriggerPanel)
    bpy.utils.unregister_class(OBJECT_PT_my_custom_panel)
