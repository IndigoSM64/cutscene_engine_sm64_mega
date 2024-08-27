import bpy
import os
from ..utilities import convert_position_blender_to_sm_64, convert_angle_yaw_blender_to_sm_64, convert_scale_blender_to_sm_64, convert_scale_z_blender_to_sm_64, convert_scale_x_blender_to_sm_64
from .edit_files_for_trigger import export_header_file, export_in_level_data, export_in_the_script



def get_triggers_area(area_index):
    empty_cubes = []
    empty_cones = []
    for obj in bpy.context.scene.objects:
        if obj.type == 'EMPTY' and area_index == obj.areaIndex:
            if obj.empty_display_type == 'CUBE':
                empty_cubes.append(obj)
            elif obj.empty_display_type == 'CONE':
                empty_cones.append(obj)
    return empty_cubes, empty_cones

def get_area_root():
    area_list = []
    for obj in bpy.context.scene.objects:
        if obj.sm64_obj_type == "Area Root":
            area_list.append(obj)
    return area_list



def get_postion_angle_and_scale_triggers(empty_cubes, empty_cones, context):
        str_trigger = ""

        for obj in empty_cubes:
            str_trigger += f"    CUTSCENE_TRIGGER_CUBE,\n"
            str_trigger += f"        TRIGGER_ACTIVE,\n"
            sm64_pos = convert_position_blender_to_sm_64(obj.location.x, obj.location.y, obj.location.z)
            sm64_angle = convert_angle_yaw_blender_to_sm_64(obj.rotation_euler.z)
            sm64_scale = convert_scale_blender_to_sm_64(obj.scale.x, obj.scale.y, obj.scale.z)
            str_trigger += f"        POSITION_TRIGGER_CUTSCENE_SHAPE({sm64_pos[0]}, {sm64_pos[1]}, {sm64_pos[2]}),\n"
            str_trigger += f"        CUBE_SIZE_TRIGGER_CUTSCENE_SHAPE({sm64_scale[0]}, {sm64_scale[1]}, {sm64_scale[2]}),\n"
            str_trigger += f"        CUBE_ANGLE_YAW_TRIGGER_CUTSCENE_SHAPE(0x{sm64_angle:X}),\n"
            str_trigger += f"        CUTSCENE_ID_TRIGGER_CUTSCENE_SHAPE({obj.cynematic_number_prop}),\n"
 


        for obj in empty_cones:
            str_trigger += f"    CUTSCENE_TRIGGER_CYLINDRE,\n"
            str_trigger += f"        TRIGGER_ACTIVE,\n"
            sm64_pos = convert_position_blender_to_sm_64(obj.location.x, obj.location.y, obj.location.z)
            sm64_hight_cone = convert_scale_z_blender_to_sm_64(obj.scale.y)
            sm64_radius = convert_scale_x_blender_to_sm_64(obj.scale.x)
            str_trigger += f"        POSITION_TRIGGER_CUTSCENE_SHAPE({sm64_pos[0]}, {sm64_pos[1]}, {sm64_pos[2]}),\n"
            str_trigger += f"        CYLINDRE_RADIUS_TRIGGER_CUTSCENE_SHAPE({sm64_radius}),\n"
            str_trigger += f"        CYLINDRE_HEIGHT_TRIGGER_CUTSCENE_SHAPE({sm64_hight_cone}),\n"
            str_trigger += f"        CUTSCENE_ID_TRIGGER_CUTSCENE_SHAPE({obj.cynematic_number_prop}),\n"


        return str_trigger





class ExportTriggers(bpy.types.Operator):
    bl_idname = "object.export_triggers"
    bl_label = "Export Trigger"

    def execute(self, context):
        str_trigger = ""
        empty_cubes = []
        empty_cones = []
        area_root = []
        number_of_triggers = 0

        area_root = get_area_root()

        if area_root is None:
            self.report({'ERROR'}, "No area root found")
            return {'FINISHED'}
        
        i= 0
        for area in area_root:
            i += 1
            empty_cubes, empty_cones = get_triggers_area(area.areaIndex)
            number_of_triggers = len(empty_cubes) + len(empty_cones)
            if number_of_triggers == 0:
                self.report({'ERROR'}, "No triggers found")
                return {'FINISHED'}
            str_structure_name = f"{context.scene.levelOption}_area_{i}_seg7_cutscene_trigger"
            str_trigger += f'#include "src/game/cutscene_systeme_trigger.h" \n const cutsceneDataTrigger '+ str_structure_name + '[] = { \n    CUTSCENE_TRIGGER_START, \n'
            str_trigger += get_postion_angle_and_scale_triggers(empty_cubes, empty_cones, context)
            str_trigger += f'    CUTSCENE_TRIGGER_END, \n}}; \n'
            path = bpy.path.abspath(os.path.join(context.scene.decompPath, "levels", context.scene.levelOption, "areas", str(i), "cutscene_trigger.inc.c"))

            # Créer tous les répertoires nécessaires si ils n'existent pas
            os.makedirs(os.path.dirname(path), exist_ok=True)

            # Maintenant, écrire dans le fichier
            try:
                with open(path, 'w') as file:

                    file.write(str_trigger)
                print(f"Triggers écrits avec succès dans : {path}")

            except IOError as e:
                print(f"Erreur lors de l'écriture dans le fichier : {e}")

            export_header_file(self, context, str_structure_name, i)
            export_in_level_data(self, context, i)
            export_in_the_script(self, context, str_structure_name, i)
        self.report({'INFO'}, "Triggers exported " + context.scene.levelOption)

        return {'FINISHED'}
    


