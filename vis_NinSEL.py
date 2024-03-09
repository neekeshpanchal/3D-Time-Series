import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def plot_3d_motion(excel_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Create a figure for 3D plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each point's movement in the enclosure over time
    for i in range(1, 2):  # Assuming there are 8 body points as before
        x_column = f'degu_1_BP_{i}_x'
        y_column = f'degu_1_BP_{i}_y'

        # Now 'Frames' represents time on the z-axis
        # x body point coordinates are used for the x-axis
        # y body point coordinates are used for the y-axis
        ax.plot(df[x_column], df[y_column], df['Frames'], label=f'Body Point {i}')

    # Set labels and title
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Frames (Time)')
    ax.set_title('3D Motion Analysis Over Time')
    
    # Show legend
    ax.legend()

    # Show the plot
    plt.show()

def upload_action():
    # File dialog to choose an Excel file
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        plot_3d_motion(file_path)

root = tk.Tk()
root.title("3D Motion Analysis")

# Button to upload an Excel file and plot
upload_button = tk.Button(root, text="Upload Excel and Plot", command=upload_action)
upload_button.pack(pady=20)

root.mainloop()
