import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 10))


#This scatters one point on the x-axis
ax.scatter(2,4)

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 24)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = 'both', which ='major', labelsize = 14)

plt.show()