"""
Created by: Jingyi Xu
Date: May 10, 2021

Script for visualizing a precollected stiffness or deformation map.

Arguments
---------
mesh_name : str
    The name of the mesh to visualize the stiffness map for.
stiffness_map_filename : str
    Json file that contains the stiffness map, including the stiffness locations and values
"""

import trimesh
import argparse
import numpy as np
import json 
import matplotlib.pyplot as plt
import os

GRASP_FORCE = 8.0 # gripper grasp force

def check_file_exist(filename):
    if not os.path.exists(filename):
        raise OSError("File {} does not exist.".format(filename))

def normalize_data(data):
    if abs((data.max() - data.min())) < 1e-15: 
        raise ValueError("Data range is 0")
    data =  (data - data.mean()) / (data.max() - data.min()) 
    data = data - data.min()
    return data

def compute_interpolated_stiffness_map(stiffness_locations, stiffness_map, obj):
    # adjust stiffness min and max for visualization
    stiffness_map[stiffness_map>1e10] = 1e10
    stiffness_map[stiffness_map<1e-10] = 1e-10
    deformation_map = GRASP_FORCE/stiffness_map

    subdivided_obj = obj.subdivide().subdivide().subdivide()
    interpolated_stiffness = np.zeros(len(subdivided_obj.vertices))
    interpolated_deformation = np.zeros(len(subdivided_obj.vertices))

    # compute deformation and stiffness value of each vertex based on the distance to all collected stiffness map values
    for i,vertex in enumerate(subdivided_obj.vertices):
        diff =  vertex - stiffness_locations
        dists = np.linalg.norm(diff,axis=1)**3
        coeff = 1.0/dists
        interpolated_stiffness[i] = np.dot(coeff,stiffness_map)/np.sum(coeff)
        interpolated_deformation[i] = np.dot(coeff,deformation_map)/np.sum(coeff)

    normalized_interpolated_deformation_map = normalize_data(interpolated_deformation)
    clr = plt.get_cmap('jet')
    subdivided_obj.visual.vertex_colors = clr(normalized_interpolated_deformation_map)
    return subdivided_obj

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize a precollected stiffness map')
    parser.add_argument('-s', '--stiffness_filename', type=str, default='stiffness_maps/plastic_cup.json', help='filename of the stiffness map')
    parser.add_argument('-m', '--mesh_filename', type=str, default='meshes/plastic_cup.obj', help='filname of the mesh')
    # meshes in the dataset are: 'plastic_cup','w5','mustard','shampoo','box'

    args = parser.parse_args()
    stiffness_filename = args.stiffness_filename
    mesh_filename = args.mesh_filename

    check_file_exist(mesh_filename)
    check_file_exist(stiffness_filename)

    mesh_trimesh = trimesh.load(mesh_filename)

    with open(stiffness_filename) as f:
        st_map = json.load(f)
    # locations where the object is squeezed by the gripper to collect deformation
    stiffness_locations = np.array(st_map['stiffness_locations'])
    # computed stiffness value based on the deformation
    stiffness_map = np.array(st_map['stiffness_map'])

    # computed interpolated stiffness and deformation map as vertics colors
    subdivided_obj = compute_interpolated_stiffness_map(stiffness_locations,stiffness_map,mesh_trimesh)

    # visualization 
    try:
        # visualize the mesh with pyrender
        import pyrender
        mesh = pyrender.Mesh.from_trimesh(subdivided_obj)
        scene = pyrender.Scene()
        scene.add(mesh)
        pyrender.Viewer(scene, use_raymond_lighting=True)
    except ImportError as error:
        print(error.__class__.__name__ + ": " + error.message)
        # visualize with trimesh if pyrender is not installed. 
        subdivided_obj.show()