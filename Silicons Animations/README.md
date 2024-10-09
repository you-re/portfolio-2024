# Silicons Animations

## Task Description
The client needed an efficient method to create thousands of NFT animations from a set of 100+ assets. My responsibilities included character animation, clothing simulations, automating the rendering and optimizing the workflow.

![Video of 3D assets]https://github.com/user-attachments/assets/c7b7180f-1604-43c2-82d3-74b278747077

## Thought Proccess
Initially, I considered rendering each combination of assets separately, but I quickly realized this would lead to extremely long render times. Instead, I chose to render each asset as a separate layer and then composite them in After Effects.

## Optimizations
This approach avoided redundant rendering of the same assets multiple times, reducing the overall render time by reusing the same renders across combinations. It also allowed for fast fixes in case any of the assets needed that.


After optimizing and simulating garments, I batch imported everything into Blender, ensuring materials and animations were correct. I used a Python script to automate individual asset rendering.
