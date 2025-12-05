js = """
// Подсчет статусов
const statuses = {
    "Пройден": 0,
    "Провален": 0
};

const rows = document.querySelectorAll("tbody tr");
rows.forEach(row => {
    const status = row.cells[2].textContent.trim();
    if (status === "Пройден") {
        statuses["Пройден"]++;
    } else if (status === "Провален") {
        statuses["Провален"]++;
    }
});

// Создание круговой диаграммы
const ctx = document.getElementById('statusChart').getContext('2d');
const statusChart = new Chart(ctx, {
    type: 'pie', // Изменено на 'pie' для круговой диаграммы
    data: {
        labels: ['Пройден', 'Провален'],
        datasets: [{
            label: 'Количество тестов',
            data: [statuses["Пройден"], statuses["Провален"]],
        backgroundColor: [
            'rgba(169, 208, 141, 0.6)',
            'rgba(255, 43, 30, 0.6)'
        ],
        borderColor: [
            'rgba(57, 86, 35, 1)',
              'rgba(130, 59, 11, 1)'
        ],
        borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
            display: true,
            position: 'top',
            },
        title: {
            display: true,
            text: 'Статус тестов'
            }
        }
    }
});
"""