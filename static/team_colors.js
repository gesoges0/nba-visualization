function getTeamColorsObject() {
    return {
        "ATL": "#E03A3E",
        "BOS": "#007A33",
        "BKN": "#000000",
        "CHA": "#00788C",
        "CHI": "#CE1141",
        "CLE": "#860038",
        "DAL": "#00538C",
        "DEN": "#0E2240",
        "DET": "#1D42BA",
        "GSW": "#FFC72C",
        "HOU": "#CE1141",
        "IND": "#FDBB30",
        "LAC": "#1D428A",
        "LAL": "#552583",
        "MEM": "#5D76A9",
        "MIA": "#98002E",
        "MIL": "#00471B",
        "MIN": "#78BE20",
        "NOP": "#0C2340",
        "NYK": "#F58426",
        "OKC": "#007AC1",
        "ORL": "#0077C0",
        "PHI": "#006BB6",
        "PHX": "#E56020",
        "POR": "#E03A3E",
        "SAC": "#5A2D81",
        "SAS": "#C4CED4",
        "TOR": "#CE1141",
        "UTA": "#002B5C",
        "WAS": "#002B5C",
    }
}


function getTeamColor(teamAbbreviation) {
    var teamColors = getTeamColorsObject();
    return teamColors[teamAbbreviation];
}