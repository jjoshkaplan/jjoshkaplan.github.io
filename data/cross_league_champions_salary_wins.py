import pandas as pd
import plotly.express as px


def cross_league_salary_wins_champions():
    # Load and prep
    x_league_df = pd.read_csv("data/x_league.csv")
    x_league_df["year"] = x_league_df["year"].astype(str)

    # Max regular season wins by sport
    max_wins_dict = {"NFL": 17, "NBA": 82, "MLB": 162}
    x_league_df["max_wins"] = x_league_df["sport"].map(max_wins_dict)
    x_league_df["win_pct"] = x_league_df["wins"] / x_league_df["max_wins"]
    x_league_df["champion"] = x_league_df["champion"].astype(int)

    # Drop 2020 and missing values
    x_league_df = x_league_df[x_league_df["year"] != "2020"]
    df = x_league_df.dropna(subset=["win_pct", "team_salary"])

    # Calculate average salary per sport-year
    avg_salary_df = (
        df.groupby(["sport", "year"])["team_salary"]
        .mean()
        .reset_index()
        .rename(columns={"team_salary": "avg_salary"})
    )

    # Merge average into main df
    df = df.merge(avg_salary_df, on=["sport", "year"], how="left")

    # Compute salary deviation from year average
    df["salary_vs_avg"] = df["team_salary"] - df["avg_salary"]

    # Champion label for legend
    df["champion_label"] = df["champion"].map({1: "Champion", 0: "Non-Champion"})

    # Custom color mapping
    sport_color_map = {"NBA": "orange", "NFL": "green", "MLB": "blue"}

    # Scatter plot: Deviation from Avg Salary vs Win %
    fig = px.scatter(
        df,
        x="salary_vs_avg",
        y="win_pct",
        color="sport",
        color_discrete_map=sport_color_map,
        symbol="champion_label",
        size=df["champion"].apply(lambda x: 8 if x else 1),
        hover_data=[
            "team",
            "year",
            "wins",
            "team_salary",
            "avg_salary",
            "salary_vs_avg",
            "spend_tier",
        ],
        title="Champions vs. Non-Champions: Salary vs League-Year Average and Win Percentage",
        labels={
            "salary_vs_avg": "Salary vs Year Average (USD)",
            "win_pct": "Regular Season Win %",
            "sport": "League",
            "champion": "Champion",
        },
        height=700,
    )

    # Unified layout styling for Jekyll blog embedding
    fig.update_layout(
        title="Champions vs. Non-Champions: Salary vs League-Year Average and Win Percentage",
        autosize=True,
        margin=dict(
            l=40, r=40, t=60, b=80
        ),  # Extra bottom margin to make space for legend
        xaxis_title="Salary Compared to League-Year Average ($)",
        yaxis=dict(title="Win Percentage", tickformat=".0%"),
        legend=dict(
            title="Legend",
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5,
        ),
        font=dict(size=12),
        title_x=0.5,
    )

    # Add vertical line at 0 (league average)
    fig.add_vline(x=0, line_dash="dash", line_color="gray")

    # Export with blog-friendly HTML config
    fig.write_html(
        "assets/plots/Cross_league_wins_salary_champions.html",
        include_plotlyjs="cdn",
        full_html=True,
        config={"responsive": True},
    )
