# Sand RPT: Compare Different Models

Sand RPT: Compare Different Sand Models

Reference: 

Dvorkin, J., M. Gutierrez, and D. Grana, 2014, Seismic reflections of  rock properties: Cambridge University Press.

This Jupiter Notebook compares different sand models including: stiff sand, soft sand, contact cement, constant cement and the sand model using Raymer-Hunt-Gardner (RHG) equation. 

Note: 
All the .py files are functions that will be called in the Jupiter Notebook: Sand_RPT_Compare_Different_Models.ipynb.

We start with comparing the P-wave velocity vs Porosity for different sand models at Vclay = 0.1 and Vclay = 0, as below.

![image](https://github.com/user-attachments/assets/a61ff148-3e9a-4a01-af20-c3c11e7ca745)
![image](https://github.com/user-attachments/assets/e1906f87-a213-4537-98a6-28884cae4e8f)

We can see the difference between different sand models. While stiff sand has a faster Vp than soft sand, constant contact and contact cement models offer flexible control of how the sand velocity will be.

Then, we compare these sand models to the model from Raymer-Hunt-Gardner (RHG) equation, which is relatively easy and intuitive to create. The figure below shows the comparison between sand model from RHG equation (black dash curves), with Vclay ranging from 0 to 1 from top to bottom, and other sand models as shown above. We can see that the stiff sand model (with Vclay=0) gives a similar result to the RHG model, while the soft sand and constant contact model give slower Vp in general.

![image](https://github.com/user-attachments/assets/14079120-2e6a-40b1-a99d-fab6c013e8e1)

Which model to choose still depends on data. However, these sand models will be handy for modeling sand RPT for different area.
