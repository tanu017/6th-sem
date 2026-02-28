import pandas as pd
import matplotlib.pyplot as plt 
data = pd.read_csv(r"C:\Users\totan\OneDrive\Desktop\study_data.csv")
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.scatter(data['Study Hours'], data['Exam Score'], color = 'dodgerblue', edgecolor = 'k', alpha = 0.7)
plt.title('Study Hours vs Exam Score')
plt.xlabel('Study Hours')   
plt.ylabel('Exam Score')
plt.grid(True)
bins = [0, 2, 4, 6, 8, 10, 12]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12']
data['Study Hours Range'] = pd.cut(data['Study Hours'], bins=bins, labels=labels, right=False)
grouped_data = data.groupby('Study Hours Range')['Exam Score'].mean()
plt.subplot(1, 2, 2)
grouped_data.plot(kind='bar', color='salmon')
plt.title('Average Exam Score by Study Hours Range')
plt.xlabel('Study Hours Range')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()