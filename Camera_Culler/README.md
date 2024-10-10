# Camera Culler for Blender

## Overview
The Camera Culler is a custom tool developed for Blender to significantly improve rendering efficiency through optimized camera culling. It enables faster rendering by selectively processing only the objects within the camera’s view, reducing computation time and memory usage.

## How It Works
The initial proof of concept relied on ray casting to determine point positions in screen space, but this was later revised to a more efficient method. The final version directly projects point positions onto the camera’s screen space, resulting in substantial performance gains. This approach not only improves culling but also generates free screen space UV coordinates, allowing for additional optimizations such as culling points based on an image.

## Key Features
 - **Up to 50% faster render times** compared to rendering without the Camera Culler.
 - Efficient memory usage and reduced computational load.
 - Screen space UV coordinates that enable advanced culling techniques, such as image-based point culling.

## Outcome
This tool delivers improved rendering speeds and offers greater control over scene optimization, making it ideal for complex 3D environments. It maintains high visual fidelity while reducing the resources needed for rendering.

## Skills & Technologies
 - Blender Development
 - 3D Rendering Optimization
 - Screen Space Projections
 - Culling Algorithms
