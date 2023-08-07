function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function getSummary(year, month){
    const summaryUrl = `http://127.0.0.1:8000/api/total/${year}/${month}/`;

    let resp = await fetch(summaryUrl,
    {
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken")
                },
    });
    let jsonData = await resp.json();

    return jsonData;
}

function getCurrentYearAndMonth(currentUrl){
    let url = new URL(currentUrl);
    let year = url.pathname.substring(15, 19);
    let month = url.pathname.substring(20, 22).replace("/", "");

    return [year, month]
}

window.onload = async () => {
    var chart = am4core.create("chartdiv-plan", am4charts.PieChart);

    let currentUrl = window.location.href;
    [year, month] = getCurrentYearAndMonth(currentUrl);

    let summaryJson = await getSummary(year, month);
    let totalIncome = summaryJson["total_income"];
    let totalExpense = summaryJson["total_expense"];
    let totalPlan = summaryJson["total_plan"];

    // Add data
    chart.data = [{
      "type": "Income",
      "value": totalIncome
    }, {
      "type": "Expense",
      "value": totalExpense
    }, {
      "type": "Plan",
      "value": totalPlan
    }];

    // Add and configure Series
    var pieSeries = chart.series.push(new am4charts.PieSeries());
    pieSeries.dataFields.value = "value";
    pieSeries.dataFields.category = "type";
    pieSeries.labels.template.disabled = true;
    pieSeries.ticks.template.disabled = true;

    chart.legend = new am4charts.Legend();
    chart.legend.position = "right";

    chart.innerRadius = am4core.percent(60);

    var label = pieSeries.createChild(am4core.Label);
    label.text = "${values.value.sum}";
    label.horizontalCenter = "middle";
    label.verticalCenter = "middle";
    label.fontSize = 40;
}