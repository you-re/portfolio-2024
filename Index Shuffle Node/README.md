# Index Shuffle Node for Randomized Point Distribution in Blender

## Problem: Predictable Point Distribution

In Blender, the Distribute Points on Faces and Distribute Points in Volume nodes generate points in a predictable order—starting from the first face or voxel to the last. This creates uniform patterns, which aren't ideal when projects require random yet evenly distributed points.

## Solution: Index Shuffle Node

To overcome this, I developed the Index Shuffle Node, which randomizes point indices by randomly splitting points into two groups and rejoining them. This method allows for a fast, intuitive way to achieve more randomized distributions, ideal for creating natural layouts.

| Left: _Shuffled Points_ | Right: _Standard Distribution_ |
| ---------------------- | ---------------------- |
| <video width=500 alt="Shuffled points video" src="https://github.com/user-attachments/assets/ead40cd9-548b-466e-84f2-4e55e3a65625"></video> | <video width=500 alt="Standard distribution points video" src="https://github.com/user-attachments/assets/974ee8a6-327e-42e0-a3c4-6d006d7510af"></video>

## Customization and Performance

The node allows users to specify the number of shuffle repetitions for greater randomness. However, more repetitions increase processing time, so users can balance randomness and performance based on their project needs.

### Tools Used: Blender (Geometry Nodes)
