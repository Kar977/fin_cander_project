function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function getSummary(year, month, dataType){
    const summaryUrl = `http://127.0.0.1:8000/api/${dataType}/${year}/${month}/`;

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

async function createSummaryChart() {
    let currentUrl = window.location.href;
    let chart = am4core.create("chartdiv", am4charts.PieChart);

    [year, month] = getCurrentYearAndMonth(currentUrl);

    let summaryJson = await getSummary(year, month, "total");
    let totalIncome = summaryJson["total_income"];
    let totalExpense = summaryJson["total_expense"];
    let totalPlan = summaryJson["total_plan"];

    chart.data = [{
      "type": "Expense",
      "value": totalExpense
    }, {
      "type": "Plan",
      "value": totalPlan
    }];

    return [chart, summaryJson];
}

async function createPlanChart() {
    let currentUrl = window.location.href;
    let planChart = am4core.create("chartdiv-plan", am4charts.PieChart);
    [year, month] = getCurrentYearAndMonth(currentUrl);

    let planJson = await getSummary(year, month, "plan");

    let	totalPlanDebtPayments = planJson["debt_payments"];
	let totalPlanInvesting = planJson["investing"];
	let totalPlanSaving = planJson['saving'];
	let totalPlanHousing = planJson['housing'];
	let totalPlanFood = planJson['food'];
	let totalPlanUtilities = planJson['utilities'];
	let totalPlanMedical = planJson['medical'];
	let totalPlanPersonalSpending = planJson['personal_spending'];
	let totalPlanRecreation = planJson['recreation'];
	let totalPlanMiscellaneous = planJson['miscellaneous'];

	planChart.data = [
	{
      "type": "Debt Payments",
      "value": totalPlanDebtPayments
    }, {
      "type": "Investing",
      "value": totalPlanInvesting
    }, {
      "type": "Savings",
      "value": totalPlanSaving
	},
	{
      "type": "Housing",
      "value": totalPlanHousing
    }, {
      "type": "Food",
      "value": totalPlanFood
    }, {
      "type": "Utilities",
      "value": totalPlanUtilities
	},
		{
      "type": "Medical",
      "value": totalPlanMedical
    }, {
      "type": "Personal Spending",
      "value": totalPlanPersonalSpending
    }, {
      "type": "Recreation",
      "value": totalPlanRecreation
	}, {
	  "type": "Miscellaneous",
	  "value": totalPlanMiscellaneous
	}
	]
	return [planChart, planJson];
}

async function createExpenseChart() {
    let currentUrl = window.location.href;

    let expenseChart = am4core.create("chartdiv-expense", am4charts.PieChart);

    [year, month] = getCurrentYearAndMonth(currentUrl);

    let expenseJson = await getSummary(year, month, "expense");

    let	totalExpenseDebtPayments = expenseJson["debt_payments"];
	let totalExpenseInvesting = expenseJson["investing"];
	let totalExpenseSaving = expenseJson['saving'];
	let totalExpenseHousing = expenseJson['housing'];
	let totalExpenseFood = expenseJson['food'];
	let totalExpenseUtilities = expenseJson['utilities'];
	let totalExpenseMedical = expenseJson['medical'];
	let totalExpensePersonalSpending = expenseJson['personal_spending'];
	let totalExpenseRecreation = expenseJson['recreation'];
	let totalExpenseMiscellaneous = expenseJson['miscellaneous'];

	expenseChart.data = [
	{
      "type": "Debt Payments",
      "value": totalExpenseDebtPayments
    }, {
      "type": "Investing",
      "value": totalExpenseInvesting
    }, {
      "type": "Savings",
      "value": totalExpenseSaving
	},
	{
      "type": "Housing",
      "value": totalExpenseHousing
    }, {
      "type": "Food",
      "value": totalExpenseFood
    }, {
      "type": "Utilities",
      "value": totalExpenseUtilities
	},
		{
      "type": "Medical",
      "value": totalExpenseMedical
    }, {
      "type": "Personal Spending",
      "value": totalExpensePersonalSpending
    }, {
      "type": "Recreation",
      "value": totalExpenseRecreation
	}, {
	  "type": "Miscellaneous",
	  "value": totalExpenseMiscellaneous
	}
	]

	return [expenseChart, expenseJson];
}

function configureChart(chart, calcType, data = null) {
        let pieSeries = chart.series.push(new am4charts.PieSeries());
        pieSeries.dataFields.value = "value";
        pieSeries.dataFields.category = "type";
        pieSeries.labels.template.disabled = true;
        pieSeries.ticks.template.disabled = true;

        chart.legend = new am4charts.Legend();
        chart.legend.position = "right";

        chart.innerRadius = am4core.percent(60);

        let label = pieSeries.createChild(am4core.Label);
        if(calcType == "sum"){
            label.text = "${values.value.sum}";
        }
        else if(calcType == "div" && data !== null){
            let divResult = data["total_plan"] - data["total_expense"];
            label.text = `$${divResult}`;
        }
        label.horizontalCenter = "middle";
        label.verticalCenter = "middle";
        label.fontSize = 40;
}


window.onload = async () => {
    let [chart, chartData] = await createSummaryChart();
    let [planChart, planData] = await createPlanChart();
    let [expenseChart, expenseData] = await createExpenseChart();

    configureChart(chart, "div", chartData);
    configureChart(planChart, "sum");
    configureChart(expenseChart, "sum");
}