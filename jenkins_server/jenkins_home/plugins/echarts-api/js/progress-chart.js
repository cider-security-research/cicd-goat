/* global jQuery3 */
jQuery3(document).ready(function () {
    /**
     * Renders all div elements that have the class 'echarts-progress-chart' using ECharts.
     */
    function renderProgressChart() {
        /**
         * Renders a trend chart in the a div using ECharts.
         *
         * @param {String} chartDivId - the ID of the div where the chart should be shown in
         */
        function renderProgressChart(chartDivId) {
            const chartPlaceHolder = jQuery3("#" + chartDivId);
            const model = JSON.parse(chartPlaceHolder.attr('data-chart-model'));
            const title = chartPlaceHolder.attr('data-title');
            const tooltip = chartPlaceHolder.attr('data-tooltip');
            const chartDiv = chartPlaceHolder[0];
            const chart = echarts.init(chartDiv);
            chartDiv.echart = chart;

            const options = {
                tooltip: {
                    trigger: 'item',
                    formatter: tooltip
                },
                series: [{
                    type: 'pie',
                    radius: ['70%', '100%'],
                    avoidLabelOverlap: false,
                    color: model.colors,
                    hoverAnimation: false,
                    label: {
                        show: true,
                        position: 'center',
                        fontSize: '38',
                        fontWeight: 'bold',
                        color: "#000",
                        formatter: title
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: model.data
                }
                ]
            };
            chart.setOption(options);
            chart.resize();

            return chart;
        }

        const allProgressCharts = jQuery3('div.echarts-progress-chart');
        const progressChartInstances = [];
        allProgressCharts.each(function () {
            const chart = jQuery3(this);
            const id = chart.attr('id');

            progressChartInstances.push(renderProgressChart(id));
        });

        if (progressChartInstances.length > 0) {
            jQuery3(window).resize(function () {
                progressChartInstances.forEach(function (chartInstance) {
                    chartInstance.resize();
                });
            });
        }
    }

    renderProgressChart();
});
