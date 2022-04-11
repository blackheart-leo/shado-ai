# before run this script, add the sound in the video senquence editor and adjust the end of timeline which by default is 250
import bpy
import math


angle_rad = 0


# 142 recommended for a sound visualizer with all frequencies
max_range = 142


radius = 7


# put  the title of song
song = "Koven - More Than You"


for i in range(0, max_range):
    
    
    step_rad = ((360 / max_range) * math.pi) / 180


    x = radius * math.sin(angle_rad)
    z = radius * math.cos(angle_rad)
    
    bpy.ops.mesh.primitive_cube_add(radius = 1, location=(0, 0, 1))
    bpy.ops.object.origin_set( type="ORIGIN_CURSOR" )
    
    # feel free to change this values for the scale of the objects  
    bpy.context.active_object.scale.x = 0.35
    bpy.context.active_object.scale.y = 0.35
    bpy.context.active_object.scale.z = 10
    
    bpy.ops.object.transform_apply(location = False, rotation = False, scale = True)
    
    bpy.ops.transform.translate( value=(x,0,z) )
    bpy.ops.transform.rotate( value=(angle_rad), axis = (0,1,0))
    
    angle_rad += step_rad
    
    bpy.ops.anim.keyframe_insert_menu( type="Scaling" )
    
    
    bpy.context.area.type = "GRAPH_EDITOR"
    bpy.context.active_object.animation_data.action.fcurves[0].lock = True
    bpy.context.active_object.animation_data.action.fcurves[1].lock = True
   
    
    l = i ** 2 + 20
    
    h = (i + 1) ** 2 + 20
    
    print(str(i))
    print("Low: %d" % l)
    print("High: %d" % h)
    
    # put your music folder or file path and change file format.
    bpy.ops.graph.sound_bake(filepath = "sound/%s.mp3" % song, low=l, high=h)
    
    bpy.context.area.type = "TEXT_EDITOR"