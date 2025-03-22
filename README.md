# 📊 A/B Testing Analysis for User Interface Redesign at Vanguard

## 📈 Key Performance Indicators (KPIs) Analyzed

In this project, we conducted an A/B testing analysis to evaluate the impact of a user interface redesign at Vanguard. We focused on four key performance indicators (KPIs) to measure the effectiveness of the new design:

### 1. 📊 Completion Rate (CR) per Client
- **Notebook**: [1_2_CR- completion-rate-client.ipynb](src/kpi/1_2_CR-%20completion-rate-client.ipynb)
- **Description**: This KPI measures the proportion of clients who completed the process at least once. It helps us understand if the new interface increases the likelihood of clients completing their tasks.
- **Image**: ![Completion Rate](img/1_2_CR-completion-rate-client.jpg)

### 2. 💰 Cost-Effectiveness (CE) Rate
- **Notebook**: [2_CE-cost-effectiveness.ipynb](src/kpi/2_CE-cost-effectiveness.ipynb)
- **Description**: This KPI evaluates the cost-effectiveness of the process by considering the number of calls made by clients. It helps us determine if the new interface reduces the support costs while maintaining or improving completion rates.
- **Image**: ![Cost-Effectiveness](img/2_CE-cost-effectiveness.jpg)

### 3. ⏱️ Time to Complete (TTC)
- **Notebook**: [3_TTC-time-to-complete.ipynb](src/kpi/3_TTC-time-to-complete.ipynb)
- **Description**: This KPI measures the time taken by clients to complete the process. It helps us assess if the new interface speeds up the completion time, enhancing user experience.
- **Image**: ![Time to Complete](img/3_TTC-time-to-complete.jpg)

### 4. 📅 Activity per Day
- **Notebook**: [4_activity-per-day.ipynb](src/kpi/4_activity-per-day.ipynb)
- **Description**: This KPI analyzes the activity levels of clients on different days of the week. It helps us understand if there are any significant changes in user behavior with the new interface.
- **Image**: ![Activity per Day](img/4_activity-per-day.jpg)

## 📊 Summary of Findings

- **Completion Rate**: The new interface showed a statistically significant improvement in the completion rate.
- **Cost-Effectiveness**: The new interface was more cost-effective, reducing the number of support calls while maintaining a high completion rate.
- **Time to Complete**: There was no significant reduction in the time to complete the process with the new interface.
- **Activity per Day**: No significant changes were observed in user activity levels across different days of the week.

## 📂 Project Structure

- **data**: Contains the raw and processed data files.
- **img**: Contains images related to the KPIs analyzed.
- **src**: Contains the Jupyter notebooks used for the analysis.

## 🚀 Getting Started

To replicate the analysis, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the Jupyter notebooks in the `src` directory.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- Scipy
