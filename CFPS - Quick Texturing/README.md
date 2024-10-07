# CFPS - Quick Texturing

## Project Scope

For the CFPS (Cyber First Person Shooter) project, I was tasked with developing a workflow to streamline the customization of 3D gun models using user-provided images. I created a Python script within Blender that reads an image from the user's drive, extracts colors with the extcolors library, and applies these colors to the gun's materials.

![Video of a 3D shotgun game model](https://github.com/you-re/portfolio-2024/blob/main/CFPS%20-%20Quick%20Texturing/QuickTex.gif)

![Image 1](https://github.com/user-attachments/assets/dfee5844-488c-4769-9643-79ed0936c8be) | ![image](https://github.com/user-attachments/assets/18b6acc5-da03-4fb9-ad5b-0040e61aacf8)


A major challenge was ensuring accurate color representation, as the extracted colors were in a linear format. To resolve this, I wrote a function to convert them back to sRGB. The script was designed to apply the most prominent color (typically the background) to the base material, ensuring a seamless blend with the image on the gun surface. Additionally, the PBR textures were created in Substance Designer to allow for easy recoloring within Blender.

### Tools Used: Blender (Python scripting), Python (extcolors library), Substance Designer
