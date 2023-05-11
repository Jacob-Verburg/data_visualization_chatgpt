import sys
import csv
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QDateEdit, QPushButton
from PyQt5.QtCore import Qt, QDate
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class TemperatureGraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Graph App")
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        # Date range selection
        date_label = QLabel("Select Date Range:")
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QDate.currentDate().addMonths(-1))  # Default start date: one month ago
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())  # Default end date: today

        # Graph display
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(date_label)
        self.layout.addWidget(self.start_date_edit)
        self.layout.addWidget(self.end_date_edit)
        self.layout.addWidget(self.canvas)

        # Button to generate the graph
        generate_button = QPushButton("Generate Graph")
        generate_button.clicked.connect(self.generate_graph)
        self.layout.addWidget(generate_button)

        self.setLayout(self.layout)

    def generate_graph(self):
        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate()

        dates = []
        temperatures = []

        # Read temperature data from the CSV file
        with open("temperature_data.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                current_date = datetime.strptime(row["Date"], "%Y-%m-%d").date()
                if start_date <= current_date <= end_date:
                    dates.append(current_date)
                    temperatures.append(float(row["Temperature"]))

        self.plot_graph(dates, temperatures)

    def plot_graph(self, dates, temperatures):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(dates, temperatures)
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature")
        ax.set_title("Temperature Graph")
        ax.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureGraphApp()
    window.show()
    sys.exit(app.exec_())
