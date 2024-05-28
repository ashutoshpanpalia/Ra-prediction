
# Estimation of Surface Roughness in Turning Operations Using Multivariate Polynomial Regression
DOI: https://doi.org/10.1007/978-981-33-4320-7_86
# Authors
Ashutosh Panpalia
Hrishabh Jha
Devanshu Suneja
Geetanshu Ashpilya
Hitesh Kumar
Vijay Gautam

# Abstract

Surface roughness is a critical factor in determining the durability and performance of machined components. Predicting surface roughness without using stylus-based instruments can significantly reduce tool changing and measuring time, thereby decreasing overall machining time. This project presents a statistical approach to predict surface roughness in turning operations based on **multivariate polynomial regression**. The model uses the cumulative length of the chips generated and three cutting parameters (cutting speed, feed, and depth of cut) to predict surface roughness. The experiments were conducted on a mild steel rod using an HSS tool. The dynamic prediction model aims to optimize tool life by determining the appropriate time for tool changes.

# Introduction

Surface roughness in turning operations is influenced by cutting speed, feed, and depth of cut. Predicting surface roughness accurately helps in maintaining the desired performance and durability of components. This project explores the use of multivariate polynomial regression to predict surface roughness, thereby minimizing the reliance on stylus-based measurement instruments. The experiments utilized a mild steel rod and a high-speed steel (HSS) tool to collect data and develop a predictive model.

# Experimental Procedure

## Materials and Setup:

Mild Steel Rod: Diameter 30 mm, Length 220 mm.

CNC Turning Centre: Model LL20TL3.

H-400 10% Cobalt High-Speed Steel Tool.

## Surface Roughness Tester: 

Taylor Hobson Surtronic 3+.

## Cutting Parameters:

Cutting speed: 20-32 m/min.
Feed: 0.05-0.45 mm/rev.
Depth of cut: 0.3-1.3 mm.

## Data Collection and Analysis:

Surface roughness measured using a surface roughness tester at multiple locations on the workpiece.

Polynomial regression model developed using scikit-learn library in Python.

Error analysis performed using R-squared, RMSE, MAE, and MAPE metrics.

# Results 
Error Analysis after introduction of novel parameter **Peripheral Length**:
![image](https://github.com/ashutoshpanpalia/Ra-prediction/assets/43078289/09797830-2159-47da-a344-f2fb1c31952c)

The polynomial regression model provided an accurate prediction of surface roughness with an R-squared value of 0.8151

RMSE for testing data was 0.9600, indicating good model performance.

The predictive model showed that surface roughness values increase with the cumulative peripheral length of chips generated during machining.

The model successfully identified the tool's working limits and the point at which surface roughness values exceed acceptable levels.


# Setup photos:
![image](https://github.com/ashutoshpanpalia/Surface_roughness_prediction_with_AI/assets/43078289/ef01b20e-5d02-407e-b495-8225237d6926)

![image](https://github.com/ashutoshpanpalia/Surface_roughness_prediction_with_AI/assets/43078289/815ab3d5-f53e-4805-a290-6858c941d35f)

![image](https://github.com/ashutoshpanpalia/Surface_roughness_prediction_with_AI/assets/43078289/ce3d6334-7bc4-40b2-834f-81e169783d69)


# Conclusion and Future Scope

The multivariate polynomial regression model developed in this project effectively predicts surface roughness based on cutting parameters and cumulative chip length. This predictive capability can significantly enhance tool life management and machining efficiency. Future work could involve scaling the experiment to industrial levels with more extensive data to improve accuracy. Additionally, similar models could be developed for other machining operations to further optimize production processes.

# Please contact the authors for further details
