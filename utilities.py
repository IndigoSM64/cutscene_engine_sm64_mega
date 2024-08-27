import bpy
from math import degrees


def convert_position_blender_to_sm_64(posx, posy, posz):
                    pos_inter = posy
                    posx = posx * bpy.context.scene.blenderF3DScale
                    posy = posz * bpy.context.scene.blenderF3DScale
                    posz = pos_inter * bpy.context.scene.blenderF3DScale *-1
                    
                    posx = round(posx)
                    posy = round(posy)
                    posz = round(posz)
                
                    return posx, posy, posz

def convert_scale_blender_to_sm_64(scalex, scaley, scalez):
                    scale_inter = scaley
                    scalex = scalex * bpy.context.scene.blenderF3DScale
                    scaley = scalez * bpy.context.scene.blenderF3DScale
                    scalez = scale_inter * bpy.context.scene.blenderF3DScale *-1
                    
                    scalex = round(scalex)
                    scaley = round(scaley)
                    scalez = round(scalez)
                
                    return scalex, scaley, scalez

def convert_scale_z_blender_to_sm_64(scalez):
                    scaley = scalez * bpy.context.scene.blenderF3DScale
                    
                    scaley = round(scaley)
                
                    return scaley

def convert_scale_x_blender_to_sm_64(scalex):
                    scalex = scalex * bpy.context.scene.blenderF3DScale
                    scalex = round(scalex)
                
                    return scalex


def convert_angle_yaw_blender_to_sm_64(angleYaw):
                angleYaw = degrees(angleYaw)
                if angleYaw < 0:
                    angleYaw = 360 + angleYaw
                angle_s16 = int((angleYaw / 360.0) * 65536.0) 
                
                return angle_s16