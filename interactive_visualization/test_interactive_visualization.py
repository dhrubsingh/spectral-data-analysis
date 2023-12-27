import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data_extraction.data_extraction import DataExtraction
from matplotlib.widgets import RectangleSelector

class VisualizeSpectraInteractive:
    
    def __init__(self) -> None:
        """
        Initialize a VisualizeSpectraInteractive object instance.
        """
        self.data = None
        self.df = None

    def get_spectrum_data(self, plate_id, mjd, fiberid) -> None:
        """
        Fetch spectrum data using plate ID, MJD, and fiber ID and save it as a CSV file.
        
        Args:
        - plate_id (int): Plate ID
        - mjd (int): Modified Julian Date
        - fiberid (int): Fiber ID
        """
        data_extractor = DataExtraction(plate_id, mjd, fiberid)
        self.data = data_extractor.get_spectrum_data()

    def get_data_from_csv(self, csv_file_path) -> None:
        """
        Load spectrum data from a CSV file.
        
        Args:
        - csv_file_path (str): Path to the CSV file containing spectrum data.
        """
        self.data = pd.read_csv(csv_file_path)
  
    def visualize_interactive(self) -> None:
        """
        Visualize spectrum data interactively using matplotlib.
        
        Functionalities:
        - Select a Rectangular Region to zoom.
        - Dynamic Wavelength/Flux annotations while moving your cursor.
        - Reset Plot to Default by pressing the 'escape' key.
        """
        # Create Plot
        fig, ax = plt.subplots()
        ax.set_title('Interactive Spectral Line Plot')
        ax.plot(self.data['Wavelength'], self.data['Flux'])
        ax.set_xlabel('Wavelength')
        ax.set_ylabel('Flux')
        original_x = ax.lines[0].get_xdata()
        original_y = ax.lines[0].get_ydata()
        x_start, x_end = min(original_x), max(original_x)
        y_start, y_end = min(original_y), max(original_y)
        ax.set_xlim(x_start, x_end)
        ax.set_ylim(y_start, y_end)

        def toggle_select(event):
           if event.key == 'escape':
              ax.set_xlim(x_start, x_end)
              ax.set_ylim(y_start, y_end)
              fig.canvas.draw_idle()

        def onselect(eclick, erelease):
            x1, y1 = eclick.xdata, eclick.ydata
            x2, y2 = erelease.xdata, erelease.ydata
            ax.set_xlim(x1, x2)
            ax.set_ylim(y1, y2)
            fig.canvas.draw_idle()
            print(f"Selected area: x1={x1}, y1={y1}, x2={x2}, y2={y2}")



        rs = RectangleSelector(ax, onselect, useblit=True,
            button=[1, 3], minspanx=5, minspany=5, spancoords='pixels',
            interactive=True)
        # Connect event handler
        fig.canvas.mpl_connect('key_press_event', toggle_select)

        annotation = ax.annotate('', xy=(0, 0), xytext=(-20, 20), textcoords='offset points',
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
                         visible=False)

        def on_hover(event):
            if event.inaxes == ax:
                x, y = event.xdata, event.ydata
                annotation.set_text(f'X: {x:.2f}, Y: {y:.2f}')
                annotation.xy = (x, y)
                annotation.set_visible(True)
                fig.canvas.draw_idle()

        def on_leave(event):
            annotation.set_visible(False)
            fig.canvas.draw_idle()

        fig.canvas.mpl_connect('motion_notify_event', on_hover)
        fig.canvas.mpl_connect('axes_leave_event', on_leave)

        # fig.canvas.mpl_connect('motion_notify_event', on_hover)
        plt.show()

if __name__ == '__main__':
    vs = VisualizeSpectraInteractive()
    vs.get_spectrum_data(4055, 55359, 596)
    print(vs.data.head())
    vs.visualize_interactive()