---
title: "Visualizing Team Salary Distributions Across Leagues"
date: 2025-04-19 09:00:00 -0400
categories: [Analysis, Spending]
tags: [mlb, nba, nfl, salary cap, covid, sports economics]
author: joshua
---

Before analyzing the relationship between financial investment and on-field success, it is important to first examine annual spending patterns across leagues.

The plot below presents each league in a distinct color, using box-and-whisker plots to visualize the distribution of team payrolls. These plots are particularly effective for highlighting spread and central tendency in financial data. The “box” represents the interquartile range (the middle 50% of teams), the horizontal line within the box indicates the median, and the “whiskers” extend to capture the outer 50% of values, providing insight into outliers and variability.

{% include embed/iframe.html src="/assets/plots/salary_boxplot.html" title="Team Salary Distribution by League and Year" %}

This plot reveals that **MLB teams exhibit the widest range in payrolls** over the past decade, with a significant gap between the highest and lowest spenders. In contrast, **NFL teams operate within a much narrower spending band** due to the enforcement of a hard salary cap and floor. Notably, NFL team spending began the period near the MLB median but has since surpassed it.

Meanwhile, **NBA payrolls started below** both the MLB’s interquartile range and the lowest-spending NFL teams. However, over time, NBA spending has **increased substantially**, with many teams now exceeding the median payroll of their MLB counterparts.

---

### 🦠 COVID-Era Impact

We can also observe how the pandemic affected each league differently:

- **MLB** was greatly impacted as the start of the 2020 season coincided with the beginning of the COVID-19 shutdown.
- **NFL** was minimally disrupted, as the 2020 Super Bowl occurred just before lockdowns.
- **NBA** was paused abruptly in March 2020 and later resumed in the “Disney Bubble” before delaying the 2021 season start.

These historical disruptions offer additional layers of context for understanding long-term financial trends.

{% include embed/iframe.html 
   src="/assets/plots/Cross_League_Distribution_of_Team_Spend_by_Year.html" 
   title="Cross-League Team Spend by Year" %}



