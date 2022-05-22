function getTeamColorsObject() {
    return {
        "BOS": "#007A33",
        "DAL": "#00538C",
        "GSW": "#FFC72C",
        "MIA": "#98002E",
        "MIL": "#00471B",
    }
}


function getTeamColor(teamAbbreviation) {
    var teamColors = getTeamColorsObject();
    return teamColors[teamAbbreviation];
}