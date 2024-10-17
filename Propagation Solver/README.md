# Propagation Solver - Geometry Nodes Simulation

## Task Description
The Propagation Solver was a personal project aimed at testing the capabilities of Blender's new Geometry Nodes workflow for creating custom simulation solvers. The goal was to simulate a growth or propagation effect by manipulating point attributes, which I later used to instance foliage geometry. I explored the feasibility of using Geometry Nodes for such simulations, but after testing, I realized that alternative workflows would yield better performance in future projects.

[![Propagation Solver Render](https://github.com/user-attachments/assets/a05a1f5d-4cd8-435c-93b8-dbb76cccddee)](https://www.youtube.com/watch?v=ZwkmGAm5ChI)

## Thought Process
My initial approach involved using Geometry Nodes to check attributes of multiple neighboring points to simulate propagation. However, Blender’s current system for this operation proved too slow for practical use. To overcome this, I adopted a faster method by blurring the points' active attributes, simulating the effect of propagation in a more efficient manner. This blurring technique provided the necessary performance boost while maintaining the desired growth effect.

Once the points were processed, I used them to instance foliage geometry, creating a dynamic simulation of plant growth. After rendering the animation, I composited the final sequence in DaVinci Fusion to ensure the highest quality output and fine-tune visual effects.

## Optimizations
To enhance performance further, I integrated a custom camera culler node that I had previously developed. This node automatically culled off-screen geometry, reducing both viewport and render time significantly. Despite achieving my goals with this setup, I concluded that future projects would benefit more from switching to Houdini, as it offers faster simulation times, more control, and a more versatile workflow—especially for making adjustments during development.

## Tools Used
 - Blender: Used primarily for building the propagation solver using Geometry Nodes and instancing foliage.
 - Custom Camera Culler: Integrated to optimize performance by reducing out-of-view geometry load.
 - DaVinci Fusion: Composited the final rendered animation for post-processing and visual refinement.
