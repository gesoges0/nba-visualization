function barchart(data, stats_key, colors) {
  // set the dimensions and margins of the graph
  const margin = { top: 20, right: 30, bottom: 40, left: 90 },
    width = 500 - margin.left - margin.right,
    height = 200 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  const svg = d3
    .select("#stats_" + stats_key)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Add X axis
  const x = d3
    .scaleLinear()
    .domain([0, d3.max(data, (d) => d.stats)])
    .range([0, width]);
  svg
    .append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x))
    .selectAll("text")
    .attr("transform", "translate(-10,0)rotate(-45)")
    .style("text-anchor", "end");

  // Y axis
  const y = d3
    .scaleBand()
    .range([0, height])
    .domain(data.map((d) => d.TEAM))
    .padding(0.1);
  svg.append("g").call(d3.axisLeft(y));

  //Bars
  svg
    .selectAll("myRect")
    .data(data)
    .join("rect")
    .attr("x", x(0))
    .attr("y", (d) => y(d.TEAM))
    .attr("width", (d) => x(d.stats))
    .attr("height", y.bandwidth())
    .attr("fill", (d) => colors[d.TEAM]);

  // title
  svg
    .append("text")
    .attr("x", x(d3.max(data, (d) => d.stats) / 2))
    .attr("y", y(0))
    .attr("font-size", "13px")
    .attr("text-anchor", "top")
    .attr("font-weight", 700)
    .text(stats_key);
}
