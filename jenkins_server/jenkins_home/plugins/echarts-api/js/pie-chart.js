/* global jQuery3 */
jQuery3(document).ready(function () {
    /**
     * Renders all div elements that have the class 'echarts-pie-chart' using ECharts.
     */
    function renderPieCharts() {
        /**
         * Renders a trend chart in the a div using ECharts.
         *
         * @param {String} chartDivId - the ID of the div where the chart should be shown in
         */
        function renderPieChart(chartDivId) {
            function isEmpty(string) {
                return (!string || string.length === 0);
            }

            /**
             * Returns the title properties of the chart.
             *
             * @param {String} title - the title
             */
            function getTitle(title) {
                if (!isEmpty(title)) {
                    return {
                        text: title,
                        textStyle: {
                            fontWeight: 'normal',
                            fontSize: '16'
                        },
                        left: 'center'
                    };
                }
                else {
                    return null;
                }
            }

            const chartPlaceHolder = jQuery3("#" + chartDivId);
            const model = JSON.parse(chartPlaceHolder.attr('data-chart-model'));
            const title = chartPlaceHolder.attr('data-title');
            const chartDiv = chartPlaceHolder[0];
            const chart = echarts.init(chartDiv);
            chartDiv.echart = chart;

            const textColor = getComputedStyle(document.body).getPropertyValue('--text-color') || '#333';

            const options = {
                title: getTitle(title),
                tooltip: {
                    trigger: 'item',
                    formatter: '{b}: {c} ({d}%)'
                },
                legend: {
                    orient: 'horizontal',
                    x: 'center',
                    y: 'bottom',
                    type: 'scroll',
                    textStyle: {
                        color: textColor
                    }
                },
                series: [{
                    type: 'pie',
                    radius: ['30%', '70%'],
                    avoidLabelOverlap: false,
                    color: model.colors,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: false
                        }
                    },
                    labelLine: {
                        normal: {
                            show: true
                        }
                    },
                    data: model.data
                }
                ]
            };
            chart.setOption(options);
            chart.resize();

            const useLinks = chartPlaceHolder.attr('data-links');
            if (useLinks && useLinks !== "false") {
                chart.on('click', function (params) {
                    window.location.assign(params.name);
                });
            }

            return chart;
        }

        const allPieCharts = jQuery3('div.echarts-pie-chart');
        const pieChartInstances = [];
        allPieCharts.each(function () {
            const chart = jQuery3(this);
            const id = chart.attr('id');

            pieChartInstances.push(renderPieChart(id));
        });
        if (pieChartInstances.length > 0) {
            jQuery3(window).resize(function () {
                pieChartInstances.forEach(function (chartInstance) {
                    chartInstance.resize();
                });
            });
        }
    }

    renderPieCharts();
});


