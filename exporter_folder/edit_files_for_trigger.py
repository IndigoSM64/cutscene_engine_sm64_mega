import bpy
import os

def export_header_file(self, context, triggers_include, indexArea):
    path = bpy.path.abspath(os.path.join(context.scene.decompPath, "levels", context.scene.levelOption, "header.h"))
    
    try:
        str_triggers_include = f"extern const cutsceneDataTrigger {triggers_include}[];"

        with open(path, 'r') as file:
            content = file.read()

        if str_triggers_include in content:
            return

        insertion_index = content.find('#endif')

        if insertion_index == -1:
            self.report({"ERROR"}, "Le '#endif' n'a pas été trouvé dans le fichier.")
            return {'CANCELLED'}

        content = content[:insertion_index] + str_triggers_include + '\n' + content[insertion_index:]

        with open(path, 'w') as file:
            file.write(content)

        self.report({"INFO"}, "La ligne a été ajoutée avec succès.")

    except Exception as e:
        self.report({"ERROR"}, f"Erreur lors de la modification du fichier: {e}")
        return {'CANCELLED'}

    return {'FINISHED'}



def export_in_the_script(self, context, triggers_include, areaIndex):
    path = bpy.path.abspath(os.path.join(context.scene.decompPath, "levels", context.scene.levelOption, "script.c"))
    
    try:
        str_triggers_include = f"\n       OBJECTOFCUTSCENETRIGGER({triggers_include}),\n"

        with open(path, 'r') as file:
            content = file.read()

        if str_triggers_include in content:
            return

        i = 0
        insertion_index = 0
        j = 0

        while areaIndex != i :
            break_loop = False
            insertion_index = content.find(' AREA', insertion_index + 1)

            if insertion_index == -1:
                self.report({"ERROR"}, "pas d'area trouvé")
                return {'CANCELLED'}
            j = 0
            
            while content[insertion_index + j] != "\n":
                j += 1
                if(content[insertion_index + j].isdigit()):
                    if areaIndex == int(content[insertion_index + j]):
                        break_loop = True
                    

            i += 1
            if break_loop:
                break

        insertion_index += j
    



        content = content[:insertion_index] + str_triggers_include + '\n' + content[insertion_index:]

        with open(path, 'w') as file:
            file.write(content)

        self.report({"INFO"}, "La ligne a été ajoutée avec succès.")

    except Exception as e:
        self.report({"ERROR"}, f"Erreur lors de la modification du fichier: {e}")
        return {'CANCELLED'}

    return {'FINISHED'}

def export_in_level_data(self, context, area_index):
    path = bpy.path.abspath(os.path.join(context.scene.decompPath, "levels", context.scene.levelOption, "leveldata.c"))

    try:
        str_triggers_include = f'\n#include "levels/{context.scene.levelOption}/areas/{area_index}/cutscene_trigger.inc.c"\n'

        with open(path, 'r') as file:
            content = file.read()

        if str_triggers_include in content:
            return
        
        content += str_triggers_include
        with open(path, 'w') as file:
            file.write(content)

    except Exception as e:
        self.report({"ERROR"}, f"Erreur lors de la lecture du fichier: {e}")
        return {'CANCELLED'}