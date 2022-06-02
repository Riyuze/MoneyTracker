const searchField = document.querySelector('#searchField');
const appTable = document.querySelector('.app-table');
const tableOutput = document.querySelector('.table-output');
const paginationContainer = document.querySelector('.pagination-container');
const tableBody = document.querySelector('.table-body');
const noResults = document.querySelector('.no-results');

tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0){
        paginationContainer.style.display = 'none';
        tableBody.innerHTML = "";
        fetch("/incomes/search-incomes", {
            body: JSON.stringify({ searchText: searchValue }),
            method: 'POST',
        })
            .then((res) => res.json())
            .then((data) => {
                appTable.style.display = 'none';
                tableOutput.style.display = 'block';
    
                if (data.length === 0){
                    tableOutput.style.display = 'none';
                    noResults.style.display = 'block';
                }
                else{
                    data.forEach((item) => {
                        noResults.style.display = 'none';
                        tableBody.innerHTML += `
                        <tr>
                            <td>${item.amount}</td>
                            <td>${item.description}</td>
                            <td>${item.source}</td>
                            <td>${item.date}</td>
                            <td></td>
                        </tr>
                    `;
                    });
                }
            });
    }
    else {
        appTable.style.display = 'block';
        paginationContainer.style.display = 'block';
        tableOutput.style.display = 'none';
        noResults.style.display = 'none';
    }
});