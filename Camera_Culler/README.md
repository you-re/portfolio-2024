# Camera Culler for Blender

![Screenshoot of the Camera Culler in action](https://github.com/user-attachments/assets/534f401e-2803-4299-9631-57459fb383ae)

## Overview
The Camera Culler is a custom tool developed for Blender to significantly improve rendering efficiency through optimized camera culling. It enables faster rendering by selectively processing only the objects within the camera’s view, reducing computation time and memory usage.

## How It Works
The initial proof of concept used ray casting to determine whether a point was visible to the camera. However, this was later optimized for greater efficiency. In the final version, point positions are directly projected onto the camera’s screen space, which leads to significant performance improvements. This method not only streamlines culling but also generates free screen space UV coordinates, enabling further enhancements like image-based point culling.



The toolset includes:
 - **Frustum culling:** Basic culling of objects outside the camera’s view.
 - **Image-based culling:** Uses image luminosity to cull points based on visibility.
 - **Occlusion detection:** Detects occlusion from terrain or other objects in the scene.
 - **Automated setup script:** Automatically pulls camera data (lens length, sensor size, clipping distance, render resolution) and dynamically adjusts parameters, eliminating manual configuration.

## Key Features
 - **Up to 50% faster render times** compared to rendering without the Camera Culler.
 - Efficient memory usage and reduced computational load.
 - Screen space UV coordinates that enable advanced culling techniques, such as image-based point culling.

## Earlier Versions and usecases
| Culling in space | Grass culling |
| -------------- | -------------- |
| <video width=500 alt="Meteorites culling" src="https://github.com/user-attachments/assets/f5919d59-1cda-444a-97e9-b9588e76801f"></video> | <video width=500 alt="Grass culling" src="https://github.com/user-attachments/assets/6c34f10b-116c-47be-9a30-0b3aea72bff1"></video> |

## Outcome
This tool delivers improved rendering speeds and offers greater control over scene optimization, making it ideal for complex 3D environments. It maintains high visual fidelity while reducing the resources needed for rendering.

## Skills & Technologies
 - Blender Development
 - 3D Rendering Optimization
 - Screen Space Projections
 - Culling Algorithms
