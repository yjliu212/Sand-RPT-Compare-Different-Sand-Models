# Sand RPT: Compare Different Models

Sand RPT: Compare Different Sand Models

This Jupiter Notebook compares different sand models including: stiff sand, soft sand, contact cement, constant cement and the sand model using Raymer-Hunt-Gardner (RHG) equation. 

Note: 
All the .py files are functions that will be called in the Jupiter Notebook: Sand_RPT_Compare_Different_Models.ipynb.

We start with comparing the P-wave velocity vs Porosity for different sand models at Vclay = 0.1 and Vclay = 0, as below.
![image](https://github.com/user-attachments/assets/a61ff148-3e9a-4a01-af20-c3c11e7ca745)
![image](https://github.com/user-attachments/assets/e1906f87-a213-4537-98a6-28884cae4e8f)

We can see the difference between different sand models. While stiff sand has a faster Vp than soft sand, constant contact model offers a flexible control of how fast the sand velocity will be.

Then, we compare these sand models to the model from Raymer-Hunt-Gardner (RHG) equation, which is relatively easy and intuitive to create. The figure below shows the comparison between sand model from RHG equation in dash lines from Vclay range from 0 to 1 from top to bottom dash curves. And we can see the stiff sand model gives a similar results to the RHG equation, while the soft sand and constant contact model provide a slower Vp for sands in general.
