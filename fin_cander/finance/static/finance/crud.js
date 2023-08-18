async function deleteIncomeRecord(incomeID) {
    // send delete request to backend with sepcific plan record
    console.log("HELLO WORLD!", incomeID);
    const deleteIncomeUrl = `http://127.0.0.1:8000/api/delete-income/${incomeID}/`;
    let resp = await fetch(deleteIncomeUrl,
    {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken")
        },
    });

    let statusCode = await resp.status;

    if (statusCode == 200) {
        let divToRemove = document.getElementById(`income-record-${incomeID}`);
        divToRemove.remove();
    }
}
async function deletePlanRecord(planID) {
    console.log("HELLO WORLD!", planID);
    const deletePlanUrl = `http://127.0.0.1:8000/api/delete-plan/${planID}/`;
    let resp = await fetch(deletePlanUrl,
    {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken")
        },
    });

    let statusCode = await resp.status;

    if (statusCode == 200) {
        let divToRemove = document.getElementById(`plan-record-${planID}`);
        divToRemove.remove();
    }
}
async function deleteExpenseRecord(expenseID) {
    console.log("HELLO WORLD!", expenseID);
    const deleteExpenseUrl = `http://127.0.0.1:8000/api/delete-expense/${expenseID}/`;
    let resp = await fetch(deleteExpenseUrl,
    {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken")
        },
    });

    let statusCode = await resp.status;

    if (statusCode == 200) {
        let divToRemove = document.getElementById(`expense-record-${expenseID}`);
        divToRemove.remove();
    }
}
