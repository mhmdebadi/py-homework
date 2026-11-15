"""
#1
import matplotlib.pyplot as plt

def line_plot(x, y, title):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='red', linestyle='--', label='Line')
    plt.title(title)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)
    plt.legend()
    plt.show()

# مثال استفاده:
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# line_plot(x, y, "Simple Line Plot")


#2
class ScatterPlotter:
    def init(self, x, y):
        self.x = x
        self.y = y
        plt.figure(figsize=(8, 5))
        
    def plot(self, color='blue', size=50):
        plt.scatter(self.x, self.y, c=color, s=size, alpha=0.7)
        
    def add_labels(self, xlabel, ylabel, title):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        plt.show()

# مثال استفاده:
# plotter = ScatterPlotter([1, 2, 3, 4], [10, 20, 25, 30])
# plotter.plot(color='purple', size=100)
# plotter.add_labels('X Values', 'Y Values', 'Scatter Plot Example')

#3
class BarChart(BaseChart):
    def init(self, categories, values):
        self.categories = categories
        self.values = values
        plt.figure(figsize=(8, 5))
        
    def plot(self, color='skyblue'):
        plt.bar(self.categories, self.values, color=color)
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title('Bar Chart Example')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

# مثال استفاده:
# chart = BarChart(['A', 'B', 'C', 'D'], [15, 30, 45, 20])
# chart.plot(color='orange')
# chart.show()


#4
import numpy as np

def plot_histogram(data, bins=10, color='green'):
    plt.figure(figsize=(8, 5))
    # رسم هیستوگرام
    plt.hist(data, bins=bins, color=color, edgecolor='black', alpha=0.7)
    
    # محاسبه و رسم خط میانگین
    mean_val = np.mean(data)
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    
    plt.title('Histogram with Mean Line')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

# مثال استفاده:
# data = np.random.randn(1000) * 10 + 50
# plot_histogram(data, bins=15, color='teal')


#6
def advanced_plot_styling(x, y):
    plt.figure(figsize=(8, 5))
    
    # تنظیم رنگ پس‌زمینه ناحیه رسم
    ax = plt.gca()
    ax.set_facecolor('lightgray')
    
    plt.plot(x, y, color='blue', linewidth=2)
    
    # تنظیمات عنوان و برچسب‌ها
    plt.title('Advanced Styled Plot', fontsize=16, color='darkblue', fontweight='bold')
    plt.xlabel('X Axis', fontsize=12)
    plt.ylabel('Y Axis', fontsize=12)
    
    plt.grid(True, color='white', linestyle='-', linewidth=1)
    
    # ذخیره نمودار با کیفیت بالا
    plt.savefig('output.png', dpi=300, bbox_inches='tight')
    plt.show()

# مثال استفاده:
# advanced_plot_styling([1, 2, 3, 4], [1, 4, 9, 16])

#7
import pandas as pd

class DataVisualizer:
    def init(self, data):
        # داده‌ها را به سری/دیتافریم پانداس تبدیل می‌کنیم
        self.data = pd.Series(data)
        
    def summary(self):
        print("--- Descriptive Statistics ---")
        print(self.data.describe())
        
    def all_plot(self):
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # 1. Line Plot
        axes[0, 0].plot(self.data.values, color='red', linestyle='--')
        axes[0, 0].set_title('Line Plot')
        axes[0, 0].grid(True)
        
        # 2. Scatter Plot
        axes[0, 1].scatter(range(len(self.data)), self.data.values, color='purple')
        axes[0, 1].set_title('Scatter Plot')
        axes[0, 1].grid(True)
        
        # 3. Bar Chart
        axes[0, 2].bar(range(len(self.data)), self.data.values, color='orange')
        axes[0, 2].set_title('Bar Chart')
        
        # 4. Histogram
        axes[1, 0].hist(self.data.values, bins=10, color='green', edgecolor='black')
        axes[1, 0].set_title('Histogram')
        
        # 5. Box Plot
        axes[1, 1].boxplot(self.data.values, patch_artist=True, boxprops=dict(facecolor='lightblue'))
        axes[1, 1].set_title('Box Plot')
        
        # پاک کردن نمودار ششم خالی
        fig.delaxes(axes[1, 2])
        
        plt.tight_layout()
        plt.show()
        
    def all_save(self, prefix='plot'):
        # ذخیره نمودار خطی
        plt.figure()
        plt.plot(self.data.values, color='red')
        plt.title('Line Plot')
        plt.savefig(f'{prefix}_line.png', dpi=300)
        plt.close()
        
        # ذخیره هیستوگرام
        plt.figure()
        plt.hist(self.data.values, bins=10, color='green')
        plt.title('Histogram')
        plt.savefig(f'{prefix}_hist.png', dpi=300)
        plt.close()
        
        print(f"Plots saved with prefix '{prefix}'.")
"""



