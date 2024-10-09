# Index Shuffle Node for Randomized Point Distribution in Blender

## Problem: Predictable Point Distribution

In Blender, the Distribute Points on Faces and Distribute Points in Volume nodes generate points in a predictable order—starting from the first face or voxel to the last. This creates uniform patterns, which aren't ideal when projects require random yet evenly distributed points.

## Solution: Index Shuffle Node

To overcome this, I developed the Index Shuffle Node, which randomizes point indices by randomly splitting points into two groups and rejoining them. This method allows for a fast, intuitive way to achieve more randomized distributions, ideal for creating natural layouts.

| Left: _Shuffled Points_ | Right: _Standard Distribution_ |
| ---------------------- | ---------------------- |
| <video width=500 alt="Shuffled points video" src="https://github.com/user-attachments/assets/2b478542-a433-43ba-a847-c8a54b1942af"></video> | <video width=500 alt="Standard distribution points video" src="https://github.com/user-attachments/assets/d4b30ae5-6006-4e2a-8483-ab04ea15fd70"></video>

## Customization and Performance

The node allows users to specify the number of shuffle repetitions for greater randomness. However, more repetitions increase processing time, so users can balance randomness and performance based on their project needs.

### Tools Used: Blender (Geometry Nodes)
