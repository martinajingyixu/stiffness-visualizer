# stiffness-visualizer
## A script to visualize object stiffness map

## Installation
- Install the package using 
```bash
pip install -e . 
```
- Tested with Python 3.7
### Dependencies
- numpy
- matplotlib
- trimesh
	```bash
	pip install trimesh
	```
    - Details see https://github.com/mikedh/trimesh
- pyrender (optional)
	```bash
	pip install pyrender
	```
    - Details see https://pypi.org/project/pyrender/
    
## Quick Start
- Visualize the stiffness map for the default mesh (plastic_cup)
```bash
python tools/visualize_stiffness_map.py
```
- Visualize the stiffness map for a mesh, e.g. shampoo, in the dataset
```bash
python tools/visualize_stiffness_map.py -s stiffness_maps/shampoo.json -m meshes/shampoo.obj
```

## How to cite?
```
@inproceedings{xu2020minimal,
   title={Minimal Work: A Grasp Quality Metric for Deformable Hollow Objects},
   author={Xu, Jingyi and Danielczuk, Michael and Ichnowski, Jeff and Mahler, Jeffrey and Steinbach, Eckehard and Goldberg, Ken},
   booktitle={{IEEE} International Conference on Robotics and Automation (ICRA)}, 
   pages={1546--1552},
   year={2020}
}
```
### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

