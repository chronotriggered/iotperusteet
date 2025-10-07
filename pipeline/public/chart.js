google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  fetch("/data")
    .then((res) => res.json())
    .then((result) => {
      const feeds = result.data;

      const DataForChart = [["Time", "Temperature", "Humidity"]];
      feeds.forEach((feed) => {
        const time = new Date(feed.time).toLocaleDateString();
        const temperature = parseFloat(feed.temperature);
        const humidity = parseFloat(feed.humidity);

        if (!isNaN(temperature) && !isNaN(humidity)) {
          DataForChart.push([time, temperature, humidity]);
        }
      });

      const dataTable = google.visualization.arrayToDataTable(DataForChart);

      const options = {
        title: "Temperature and Humidity",
        curveType: "function",
        legend: { position: "bottom" },
        hAxis: { title: "Date" },
        vAxis: { title: "Values", viewWindow: { min: 0, max: 100 } },
      };

      const chart = new google.visualization.LineChart(
        document.getElementById("curve_chart")
      );

      chart.draw(dataTable, options);
    })
    .catch(() => {
      document.getElementById("output").textContent = "Error fetching data";
    });
}
