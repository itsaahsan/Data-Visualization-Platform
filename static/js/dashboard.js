document.addEventListener('DOMContentLoaded', function() {
    const chartForm = document.getElementById('chartForm');
    const chartsContainer = document.getElementById('chartsContainer');
    const chartTemplate = document.getElementById('chartTemplate');
    const chartTypeSelect = document.getElementById('chartType');
    const clearChartsBtn = document.getElementById('clearCharts');

    let chartCounter = 0;

    // Handle chart type changes to show/hide Y column selector
    chartTypeSelect.addEventListener('change', function() {
        const yColumnGroup = document.getElementById('yColumnGroup');
        const chartType = this.value;

        // Pie chart and histogram don't need Y column
        if (chartType === 'pie' || chartType === 'histogram') {
            yColumnGroup.style.display = 'none';
        } else {
            yColumnGroup.style.display = 'block';
        }
    });

    // Handle form submission
    chartForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const chartData = {
            chart_type: formData.get('chartType'),
            x_column: formData.get('xColumn'),
            y_column: formData.get('yColumn'),
            color_column: formData.get('colorColumn')
        };

        // Get filename from URL
        const urlParams = new URLSearchParams(window.location.search);
        const filename = window.location.pathname.split('/').pop();

        generateChart(filename, chartData);
    });

    // Generate chart via AJAX
    async function generateChart(filename, chartData) {
        const form = document.getElementById('chartForm');
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;

        // Show loading state
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Generating...';
        submitBtn.disabled = true;

        try {
            const response = await fetch(`/api/generate_chart/${filename}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(chartData)
            });

            const result = await response.json();

            if (response.ok) {
                addChart(chartData, result.chart);
                showAlert('Chart generated successfully!', 'success');
            } else {
                showAlert('Error: ' + result.error, 'error');
            }
        } catch (error) {
            showAlert('Network error: ' + error.message, 'error');
        } finally {
            // Reset button state
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }
    }

    // Add chart to container
    function addChart(chartData, chartJson) {
        chartCounter++;

        // Clone template
        const chartWrapper = chartTemplate.content.cloneNode(true);
        const chartElement = chartWrapper.querySelector('.chart-wrapper');
        const chartContainer = chartWrapper.querySelector('.chart-container');
        const chartTitle = chartWrapper.querySelector('.chart-title');

        // Set chart title
        const title = getChartTitle(chartData);
        chartTitle.textContent = title;

        // Set unique ID for chart container
        const chartId = `chart-${chartCounter}`;
        chartContainer.id = chartId;

        // Add remove functionality
        const removeBtn = chartWrapper.querySelector('.chart-remove');
        removeBtn.addEventListener('click', function() {
            chartElement.remove();
        });

        // Add to container
        chartsContainer.appendChild(chartWrapper);

        // Render Plotly chart
        setTimeout(() => {
            Plotly.newPlot(chartId, chartJson.data, chartJson.layout, {responsive: true});
        }, 100);
    }

    // Generate chart title based on data
    function getChartTitle(chartData) {
        const chartType = chartData.chart_type;
        const x = chartData.x_column;
        const y = chartData.y_column;
        const color = chartData.color_column;

        switch(chartType) {
            case 'bar':
                return y ? `${y} by ${x}` : `Count of ${x}`;
            case 'line':
                return `${y} over ${x}`;
            case 'scatter':
                return `${x} vs ${y}`;
            case 'pie':
                return `Distribution of ${x}`;
            case 'histogram':
                return `Distribution of ${x}`;
            default:
                return 'Chart';
        }
    }

    // Clear all charts
    clearChartsBtn.addEventListener('click', function() {
        if (confirm('Are you sure you want to clear all charts?')) {
            const charts = chartsContainer.querySelectorAll('.chart-wrapper');
            charts.forEach(chart => chart.remove());
            chartCounter = 0;
        }
    });

    // Show alert messages
    function showAlert(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type === 'error' ? 'danger' : 'success'} alert-dismissible fade show`;
        alertDiv.setAttribute('role', 'alert');
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

        // Insert at top of container
        const container = document.querySelector('.container-fluid');
        container.insertBefore(alertDiv, container.firstChild);

        // Auto dismiss after 5 seconds
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }

    // Initialize - trigger change event for initial chart type
    chartTypeSelect.dispatchEvent(new Event('change'));
});