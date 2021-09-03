%data = xlsread('C:\Users\aqcru\Desktop\School\Fall 2020\ME195A\Data\Magnetometer Calibration\Rpi_Uncalibrated_data_1.xlsx');
data = xlsread('C:\Users\aqcru\Desktop\School\Spring 2021\ME195B\Calibration\Mag_raw_4_30_21.xlsx');

x = data(:,1);
y = data(:,2);
z = data(:,3);

% Uncalibrated
figure(1);
plot(x,y,'Color','r','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(x,z,'Color','b','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(y,z,'Color','g','Marker','o','LineWidth',2,'LineStyle','none')
%axis([-1 1 -1 1])
title("Uncalibrated")
legend("XY","XZ","YZ")

% Hard Iron Calibration
% This algorithm give the best results
% Enter these values into Python code
offset_x = (max(x) + min(x)) / 2;
offset_y = (max(y) + min(y)) / 2;
offset_z = (max(z) + min(z)) / 2;

for i=1:length(x)
    corrected_x(i) = x(i) - offset_x;
    corrected_y(i) = y(i) - offset_y;
    corrected_z(i) = z(i) - offset_z;
end

figure(2);
plot(corrected_x,corrected_y,'Color','r','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(corrected_x,corrected_z,'Color','b','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(corrected_y,corrected_z,'Color','g','Marker','o','LineWidth',2,'LineStyle','none')
axis([-1 1 -1 1])
title("Hard Iron Removal")
legend("XY","XZ","YZ")

%% Soft Iron Calibration
% This calibration alogrithm gives a more elliptical data 
% shape than Hard Iron cal
avg_x = (max(x) - min(x)) / 2;
avg_y = (max(y) - min(y)) / 2;
avg_z = (max(z) - min(z)) / 2;

avg = (avg_x + avg_y + avg_z) / 3;

scale_x = avg / avg_x;
scale_y = avg / avg_y;
scale_z = avg / avg_z;

for i=1:length(x)
    corrected_soft_x(i) = corrected_x(i) * scale_x;
    corrected_soft_y(i) = corrected_y(i) * scale_y;
    corrected_soft_z(i) = corrected_z(i) * scale_z;
end

figure(3);
plot(corrected_soft_x,corrected_soft_y,'Color','r','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(corrected_soft_x,corrected_soft_z,'Color','b','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(corrected_soft_y,corrected_soft_z,'Color','g','Marker','o','LineWidth',2,'LineStyle','none')
axis([-1 1 -1 1])
title("Soft & Hard Iron Removal")
legend("XY","XZ","YZ")

%% Soft Iron Calibration 2
% This calibration alogrithm is not working for some reason
avg_x = (max(x) - min(x)) / 2;
avg_y = (max(y) - min(y)) / 2;
avg_z = (max(z) - min(z)) / 2;

avg = (avg_x + avg_y + avg_z) / 3;

for i=1:length(x)
    corrected_soft_x(i) = avg / (x(i) - offset_x);
    corrected_soft_y(i) = avg / (y(i) - offset_y);
    corrected_soft_z(i) = avg / (z(i) - offset_z);
end

figure(4);
plot(corrected_soft_x,corrected_soft_y,'Color','r','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(corrected_soft_x,corrected_soft_z,'Color','b','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(corrected_soft_y,corrected_soft_z,'Color','g','Marker','o','LineWidth',2,'LineStyle','none')
%axis([-1 1 -1 1])
title("Soft & Hard Iron Removal (Calibrated)")
legend("XY","XZ","YZ")

%% Calibrated Data
cal_data = xlsread('C:\Users\aqcru\Desktop\School\Fall 2020\ME195A\Data\Magnetometer Calibration\Rpi_Calibrated_data_1.xlsx');

x_cal = cal_data(:,1);
y_cal = cal_data(:,2);
z_cal = cal_data(:,3);

% Calibrated
figure(5);
plot(x_cal,y_cal,'Color','r','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(x_cal,z_cal,'Color','b','Marker','o','LineWidth',2,'LineStyle','none')
hold on
plot(y_cal,z_cal,'Color','g','Marker','o','LineWidth',2,'LineStyle','none')
axis([-1 1 -1 1])
title("Calibrated Data from LSM9DS1")
legend("XY","XZ","YZ")
