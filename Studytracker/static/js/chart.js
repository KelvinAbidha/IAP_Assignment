document.addEventListener('DOMContentLoaded', () => {
  fetch('/chart_data/')
    .then(response => response.json())
    .then(data => {
      const ctx = document.getElementById('progressChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: Object.keys(data),
          datasets: [{
            label: 'Hours Spent',
            data: Object.values(data),
            backgroundColor: 'rgba(30, 144, 255, 0.7)',
            borderColor: 'rgba(30, 144, 255, 1)',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: { beginAtZero: true }
          }
        }
      });
    });
});
