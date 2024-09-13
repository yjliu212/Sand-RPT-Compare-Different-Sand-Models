# Sand RPT: Compare Different Models

Sand RPT: Compare Different Sand Models

Reference: 

Dvorkin, J., M. Gutierrez, and D. Grana, 2014, Seismic reflections of  rock properties: Cambridge University Press.

Note: 

All the .py files are functions that will be called in the Jupiter Notebook: [Sand_RPT_Compare_Different_Models.ipynb](/Sand_RPT_Compare_Different_Models.ipynb).

Description:

This Jupyter Notebook provides a comparison of various sand models, including stiff sand, soft sand, contact cement, constant cement, and the Raymer-Hunt-Gardner (RHG) equation-based sand model.

We begin by comparing the P-wave velocity (Vp) versus porosity for these different sand models at two clay volume conditions: Vclay = 0.1 and Vclay = 0.0. The comparison highlights key differences between the models. Stiff sand exhibits a higher Vp than soft sand, while the contact cement and constant cement models provide more flexible control over sand velocity behavior.

![image](https://github.com/user-attachments/assets/a61ff148-3e9a-4a01-af20-c3c11e7ca745)
![image](https://github.com/user-attachments/assets/e1906f87-a213-4537-98a6-28884cae4e8f)

Next, we compare these sand models to the Raymer-Hunt-Gardner (RHG) equation model, which is relatively simple and intuitive to construct. The figure below shows the RHG sand model (represented by black dashed curves) with Vclay values ranging from 0 to 1 (from top to bottom), alongside other sand models where Vclay = 0. The stiff sand model (Vclay = 0) aligns closely with the RHG model, whereas the soft sand and constant cement models (Vclay = 0) generally result in lower Vp values.

![image](https://github.com/user-attachments/assets/14079120-2e6a-40b1-a99d-fab6c013e8e1)

The choice of model depends on the data at hand, though the RHG equation is my preferred option due to its simplicity and flexibility. Nonetheless, all these sand models are valuable tools for modeling sand rock physics templates (RPT) across different regions.
