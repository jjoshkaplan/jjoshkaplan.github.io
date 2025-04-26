import pandas as pd
import plotly.express as px


def cross_league_salary_wins():
    # Load and preprocess
    x_league_df = pd.read_csv("data/x_league.csv")
    x_league_df["year"] = x_league_df["year"].astype(str)

    # Drop 2020 (COVID-affected season)
    x_league_df = x_league_df[x_league_df["year"] != "2020"]

    # Map max regular season wins per sport
    max_wins_dict = {"NFL": 17, "NBA": 82, "MLB": 162}
    x_league_df["max_wins"] = x_league_df["sport"].map(max_wins_dict)

    # Compute win percentage
    x_league_df["win_pct"] = x_league_df["wins"] / x_league_df["max_wins"]
    x_league_df = x_league_df.dropna(subset=["team_salary", "win_pct"])

    # Calculate league-year average salary
    avg_salary_df = (
        x_league_df.groupby(["sport", "year"])["team_salary"]
        .mean()
        .reset_index()
        .rename(columns={"team_salary": "avg_salary"})
    )

    # Merge to get average salary for each row
    df = x_league_df.merge(avg_salary_df, on=["sport", "year"], how="left")

    # Calculate salary difference from league-year average
    df["salary_vs_avg"] = df["team_salary"] - df["avg_salary"]

    # Color map
    sport_color_map = {"NBA": "orange", "NFL": "green", "MLB": "blue"}

    # Plot
    fig = px.scatter(
        df,
        x="salary_vs_avg",
        y="win_pct",
        color="sport",
        color_discrete_map=sport_color_map,
        hover_data=[
            "team",
            "year",
            "wins",
            "team_salary",
            "avg_salary",
            "salary_vs_avg",
        ],
        title="Regular Season Efficiency Across Sports:<br>Winning Percentage vs Salary Compared to League-Year Average",
        labels={
            "salary_vs_avg": "Salary vs Year Average (USD)",
            "win_pct": "Winning Percentage",
        },
        height=950,
    )

    # Jekyll-style layout
    fig.update_layout(
        title="Regular Season Efficiency Across Sports:<br>Winning Percentage vs Salary Compared to League-Year Average",
        autosize=True,
        margin=dict(l=40, r=40, t=60, b=60),
        xaxis_title="Salary Compared to League-Year Average ($)",
        yaxis=dict(title="Winning Percentage", tickformat=".0%"),
        legend=dict(
            title="League",
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="center",
            x=0.5,
        ),
        font=dict(size=12),
        title_x=0.5,
    )

    # Add vertical line at average salary
    fig.add_vline(x=0, line_dash="dash", line_color="gray")

    # Write HTML for Chirpy embed
    fig.write_html(
        "assets/plots/Cross_League_Winning_Percentage_Salary.html",
        include_plotlyjs="cdn",
        full_html=True,
        config={"responsive": True},
    )
