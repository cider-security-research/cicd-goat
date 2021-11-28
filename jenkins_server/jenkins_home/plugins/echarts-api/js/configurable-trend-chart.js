/* global echarts, jQuery3, bootstrap5, EChartsJenkinsApi */
/**
 * Renders a configurable trend chart in the specified div using ECharts.
 *
 * @param {String} chartDivId - the ID of the div where the chart should be shown in
 * @param {String} model - the line chart model
 * @param {String} settingsDialogId - the optional ID of the div that provides a settings dialog (might be set to null
 *     if there is no such dialog)
 * @param {Function} chartClickedEventHandler - the optional event handler that receives click events
 */
EChartsJenkinsApi.prototype.renderConfigurableZoomableTrendChart
    = function (chartDivId, model, settingsDialogId, chartClickedEventHandler) {
    const chartModel = JSON.parse(model);
    const chartPlaceHolder = document.getElementById(chartDivId);
    const chart = echarts.init(chartPlaceHolder);
    chartPlaceHolder.echart = chart;

    const textColor = getComputedStyle(document.body).getPropertyValue('--text-color') || '#333';
    const showSettings = document.getElementById(settingsDialogId);

    const options = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            }
        },
        toolbox: {
            show: showSettings != null,
            itemSize: 16,
            feature: {
                myTool1: {
                    title: 'Setup',
                    icon: 'ipath://M487.4 315.7l-42.6-24.6c4.3-23.2 4.3-47 0-70.2l42.6-24.6c4.9-2.8 7.1-8.6 5.5-14-11.1-35.6-30-67.8-54.7-94.6-3.8-4.1-10-5.1-14.8-2.3L380.8 110c-17.9-15.4-38.5-27.3-60.8-35.1V25.8c0-5.6-3.9-10.5-9.4-11.7-36.7-8.2-74.3-7.8-109.2 0-5.5 1.2-9.4 6.1-9.4 11.7V75c-22.2 7.9-42.8 19.8-60.8 35.1L88.7 85.5c-4.9-2.8-11-1.9-14.8 2.3-24.7 26.7-43.6 58.9-54.7 94.6-1.7 5.4.6 11.2 5.5 14L67.3 221c-4.3 23.2-4.3 47 0 70.2l-42.6 24.6c-4.9 2.8-7.1 8.6-5.5 14 11.1 35.6 30 67.8 54.7 94.6 3.8 4.1 10 5.1 14.8 2.3l42.6-24.6c17.9 15.4 38.5 27.3 60.8 35.1v49.2c0 5.6 3.9 10.5 9.4 11.7 36.7 8.2 74.3 7.8 109.2 0 5.5-1.2 9.4-6.1 9.4-11.7v-49.2c22.2-7.9 42.8-19.8 60.8-35.1l42.6 24.6c4.9 2.8 11 1.9 14.8-2.3 24.7-26.7 43.6-58.9 54.7-94.6 1.5-5.5-.7-11.3-5.6-14.1zM256 336c-44.1 0-80-35.9-80-80s35.9-80 80-80 80 35.9 80 80-35.9 80-80 80z',
                    onclick: function () {
                        new bootstrap5.Modal(showSettings).show();
                    }
                }
            }
        },
        dataZoom: [
            {
                type: 'inside'
            },
            {
                type: 'slider',
                height: 25,
                bottom: 0,
                moveHandleSize: 0
            }],
        legend: {
            orient: 'horizontal',
            type: 'scroll',
            x: 'center',
            y: 'top',
            textStyle: {
                color: textColor
            }
        },
        grid: {
            left: '20',
            right: '10',
            bottom: '30',
            top: '40',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            data: chartModel.domainAxisLabels,
            axisLabel: {
                color: textColor
            }
        }],
        yAxis: [{
            type: 'value',
            min: 'dataMin',
            axisLabel: {
                color: textColor
            },
            minInterval: chartModel.integerRangeAxis ? 1 : null
        }],
        series: chartModel.series
    };
    chart.setOption(options);
    chart.resize();
    if (chartClickedEventHandler !== null) {
        chart.getZr().on('click', params => {
            const offset = 30;
            if (params.offsetY > offset && chart.getHeight() - params.offsetY > offset) { // skip the legend and data zoom
                const pointInPixel = [params.offsetX, params.offsetY];
                const pointInGrid = chart.convertFromPixel('grid', pointInPixel);
                const buildDisplayName = chart.getModel().get('xAxis')[0].data[pointInGrid[0]]
                chartClickedEventHandler(buildDisplayName);
            }
        })
    }
    jQuery3(window).resize(function () {
        chart.resize();
    });
}
