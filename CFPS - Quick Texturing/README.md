# CFPS - Quick Texturing

## Project Scope

For the CFPS (Cyber First Person Shooter) project, I was tasked with developing a workflow to streamline the customization of 3D gun models using user-provided images. I created a Python script within Blender that reads an image from the user's drive, extracts colors with the extcolors library, and applies these colors to the gun's materials.

[Video of a 3D shotgun game model](https://github.com/user-attachments/assets/aa87f0bb-d638-4afb-b85e-571f3d8bc4f0)

| Image 1 | Image 2 |
| ------------- | ------------- |
| ![](https://github.com/user-attachments/assets/b4dccbe5-5b05-4a46-b1e8-a7d0ac81b61c) | ![](https://github.com/user-attachments/assets/1cf44141-ff1a-4ec4-9570-445777a0da08) |

## Challenges
A major challenge was ensuring accurate color representation, as the extracted colors were in a linear format. To resolve this, I wrote a function to convert them back to sRGB. The script was designed to apply the most prominent color (typically the background) to the base material, ensuring a seamless blend with the image on the gun surface. Additionally, the PBR textures were created in Substance Designer to allow for easy recoloring within Blender.

## Tools Used:
Blender (Python scripting), Python (extcolors library), Substance Designer
