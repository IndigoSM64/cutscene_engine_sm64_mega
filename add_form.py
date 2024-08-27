import bpy
from math import radians

class SetupBoxEmpty(bpy.types.Operator):
    bl_idname = "object.setup_box_empty"
    bl_label = "Setup Box Empty"

    def execute(self, context):
        if context.object is None:
            self.report({'ERROR'}, "no object selected")
            return {'FINISHED'}
        if context.object.sm64_obj_type != "Area Root" and context.object.is_a_parent_trigger == False :
            self.report({'ERROR'}, "object selected is not a area")
            return {'FINISHED'}   
        


        parent_obj = context.object 
        bpy.ops.object.empty_add(type='CUBE')
        obj = bpy.context.selected_objects[0]
        obj.name = "cutscene_trigger_cube"
        obj.is_a_cutscene_trigger = True 
        obj.parent = parent_obj
        obj.areaIndex = parent_obj.areaIndex
        obj.rotation_euler = (0, 0, 0)  
        obj.scale = (1, 1, 1)  

        bpy.ops.object.select_all(action='DESELECT')  # Désélectionner tous les objets
        parent_obj.select_set(True)  # Sélectionner l'objet parent
        context.view_layer.objects.active = parent_obj  # Définir l'objet parent comme actif

        self.report({'INFO'}, "Cube Empty created")
        return {'FINISHED'}
    
class SetupConeEmpty(bpy.types.Operator):
    bl_idname = "object.setup_cone_empty"
    bl_label = "Setup Cone Empty"

    def execute(self, context):
        if context.object is None:
            self.report({'ERROR'}, "no object selected")
            return {'FINISHED'}
        if context.object.sm64_obj_type != "Area Root" and context.object.is_a_parent_trigger == False :
            self.report({'ERROR'}, "object selected is not a area")
            return {'FINISHED'}
        

        parent_obj = context.object
        bpy.ops.object.empty_add(type='CONE')
        obj = bpy.context.selected_objects[0]
        obj.name = "cutscene_trigger_cone"
        obj.rotation_euler = (radians(90), 0, 0)
        obj.is_a_cutscene_trigger = True 
        obj.parent = parent_obj
        obj.areaIndex = parent_obj.areaIndex


        bpy.ops.object.select_all(action='DESELECT')  # Désélectionner tous les objets
        parent_obj.select_set(True)  # Sélectionner l'objet parent
        context.view_layer.objects.active = parent_obj  # Définir l'objet parent comme actif
        
        self.report({'INFO'}, "Cone Empty created")
        return {'FINISHED'}
    

class SetupParentTrigger(bpy.types.Operator):
    bl_idname = "object.setup_parent_trigger"
    bl_label = "Setup Cone Cutscene Parent Trigger"

    def execute(self, context):
        if context.object is None:
            self.report({'ERROR'}, "no object selected")
            return {'FINISHED'}
        if context.object.sm64_obj_type != "Area Root" :
            self.report({'ERROR'}, "object selected is not a area")
            return {'FINISHED'}
        for child in context.object.children:
            if child.is_a_parent_trigger:
                self.report({'ERROR'}, "object selected is already a parent trigger")
                return {'FINISHED'}
        

        parent_obj = context.object
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        obj = bpy.context.selected_objects[0]
        obj.name = "cutscene_trigger_parent"

        obj.parent = parent_obj
        obj.areaIndex = parent_obj.areaIndex
        obj.is_a_parent_trigger = True

        self.report({'INFO'}, "Parent Trigger created")
        return {'FINISHED'}
    


def add_box_register():
    bpy.utils.register_class(SetupBoxEmpty)
    bpy.utils.register_class(SetupConeEmpty)
    bpy.utils.register_class(SetupParentTrigger)

def add_box_unregister():
    bpy.utils.unregister_class(SetupBoxEmpty)
    bpy.utils.unregister_class(SetupConeEmpty)
    bpy.utils.unregister_class(SetupParentTrigger)


