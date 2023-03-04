import numpy as np
import open3d as o3d

def main():
    points = o3d.io.read_point_cloud('hw5/filtered.ply')
    points.paint_uniform_color(np.array([0.1, 0.1, 0.1]))
    pcd = o3d.io.read_point_cloud('hw5/00.ply')
    pcd.paint_uniform_color(np.array([1, 0.706, 0]))
    o3d.visualization.draw_geometries([pcd, points], 'Demonstration', 1080, 720)
    

if __name__ == "__main__":
    main()