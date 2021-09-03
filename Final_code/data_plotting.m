%trial = xlsread('C:\Users\aqcru\Desktop\School\Spring 2021\ME195B\Data\Test\SU-library-longway-4-24-test2.xlsx');
trial = xlsread('C:\Users\aqcru\Desktop\School\Spring 2021\ME195B\Data\Final_Test\SU-library-longway-5-11-test1-SULibrary.xlsx');
%trial = xlsread('C:\Users\aqcru\Desktop\School\Spring 2021\ME195B\Data\Final_Test\SU-library-longway-5-8-test1.xlsx');

time = 1:length(trial(:,1));
sat = trial(:,2);
lat = trial(:,3);
long = trial(:,4);
latA = trial(:,5);
longA = trial(:,6);
latB = trial(:,7);
longB = trial(:,8);
desired_heading = trial(:,9);
current_heading = trial(:,10);
crosstrack_error = trial(:,11);
heading_error = trial(:,12);
steering_angle = trial(:,13);
straight_steering_angle( 1:length(steering_angle) ) = 90;
desired_crosstrack_error = zeros(length(lat),1);

%%
fh = figure;
for i=1:50:length(trial(:,1))
    figure(fh);
    plot([longA longB],[latA latB],'Color','b','Marker','x','LineWidth',2,'LineStyle','--')
    hold on;
    
    plot(long(i),lat(i),'Color','g','Marker','o','LineWidth',2,'LineStyle','--')
    
    hold on;
    title("Coordinates")
    xlabel("Longitude [°]")
    ylabel("Latitude [°]")
    %
    %axis([0,3,0,5]);
    drawnow;
end

%%

figure(3);
plot([longA longB],[latA latB],'Color','b','Marker','x','LineWidth',2,'LineStyle','--')
hold on
plot(long,lat,'Color','g','Marker','o','LineWidth',2,'LineStyle','--')
title("Coordinates")
xlabel("Longitude [°]")
ylabel("Latitude [°]")
%legend("Desired","Actual")

figure(4);
plot(time,current_heading,'Color','r','LineWidth',2)
hold on
plot(time,desired_heading,'Color','b','LineWidth',2)
title("Desired vs. Actual Heading")
xlabel("Time [ms]")
ylabel("Heading [°]")
legend("Desired","Actual")

figure(5);
plot(time,crosstrack_error,'Color','r','LineWidth',2)
hold on
plot(time,desired_crosstrack_error,'Color','b','LineWidth',2)
title("Crosstrack Error")
xlabel("Time [ms]")
ylabel("Crosstrack Error [m]")
legend("Desired","Actual")

figure(6);
plot(time,steering_angle,'Color','r','LineWidth',2)
hold on
plot(time,straight_steering_angle,'Color','b','LineWidth',2)
title("Corrected Steering Angle")
xlabel("Time [ms]")
ylabel("Steering Angle [°]")
legend("Desired","Actual")

figure(7);
plot(time,current_heading,'Color','r','LineWidth',2)
hold on
plot(time,crosstrack_error,'Color','r','LineWidth',2)
hold on
plot(time,desired_heading,'Color','b','LineWidth',2)
legend("Heading","Crosstrack","Desired Heading")

%%

figure(8);
plot(time,heading_error,'Color','r','LineWidth',2)
hold on
plot(time,desired_crosstrack_error,'Color','b','LineWidth',2)
legend("Heading Error","Desired Heading Error")

figure(9);
plot(time,sat,'Color','r','LineWidth',2)

%%

subplot(2,1,1);
plot(time,current_heading,'Color','r','LineWidth',2)
hold on
plot(time,desired_heading,'Color','b','LineWidth',2)
title("Desired vs. Actual Heading")
xlabel("Time [ms]")
ylabel("Heading [°]")
legend("Desired","Actual")

subplot(2,1,2);
plot(time,crosstrack_error,'Color','r','LineWidth',2)
hold on
plot(time,desired_crosstrack_error,'Color','b','LineWidth',2)
title("Crosstrack Error")
xlabel("Time [ms]")
ylabel("Crosstrack Error [m]")
legend("Desired","Actual")