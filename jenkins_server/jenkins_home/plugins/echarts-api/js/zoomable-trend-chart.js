/* global echarts, jQuery3, EChartsJenkinsApi */
/**
 * Renders a trend chart in the specified div using ECharts.
 *
 * @param {String} chartDivId - the ID of the div where the chart should be shown in
 * @param {String} model - the line chart model
 * @param {Function} redrawCallback - callback that will be invoked if the user toggles date or build domain
 */
EChartsJenkinsApi.prototype.renderZoomableTrendChart = function (chartDivId, model, redrawCallback) {
    const chartModel = JSON.parse(model);
    const chartPlaceHolder = document.getElementById(chartDivId);
    const chart = echarts.init(chartPlaceHolder);
    chartPlaceHolder.echart = chart;

    const textColor = getComputedStyle(document.body).getPropertyValue('--text-color') || '#333';

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
            itemSize: 16,
            feature: {
                myTool1: {
                    show: true,
                    title: 'Date',
                    icon: 'path://M148 288h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm108-12v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm96 0v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm-96 96v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm-96 0v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm192 0v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm96-260v352c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V112c0-26.5 21.5-48 48-48h48V12c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v52h128V12c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v52h48c26.5 0 48 21.5 48 48zm-48 346V160H48v298c0 3.3 2.7 6 6 6h340c3.3 0 6-2.7 6-6z',
                    onclick: function () {
                        localStorage.setItem('#trendBuildAxis', 'date');
                        redrawCallback();
                    }
                },
                myTool2: {
                    show: true,
                    title: 'Build#',
                    icon: 'ipath://M440.667 182.109l7.143-40c1.313-7.355-4.342-14.109-11.813-14.109h-74.81l14.623-81.891C377.123 38.754 371.468 32 363.997 32h-40.632a12 12 0 0 0-11.813 9.891L296.175 128H197.54l14.623-81.891C213.477 38.754 207.822 32 200.35 32h-40.632a12 12 0 0 0-11.813 9.891L132.528 128H53.432a12 12 0 0 0-11.813 9.891l-7.143 40C33.163 185.246 38.818 192 46.289 192h74.81L98.242 320H19.146a12 12 0 0 0-11.813 9.891l-7.143 40C-1.123 377.246 4.532 384 12.003 384h74.81L72.19 465.891C70.877 473.246 76.532 480 84.003 480h40.632a12 12 0 0 0 11.813-9.891L151.826 384h98.634l-14.623 81.891C234.523 473.246 240.178 480 247.65 480h40.632a12 12 0 0 0 11.813-9.891L315.472 384h79.096a12 12 0 0 0 11.813-9.891l7.143-40c1.313-7.355-4.342-14.109-11.813-14.109h-74.81l22.857-128h79.096a12 12 0 0 0 11.813-9.891zM261.889 320h-98.634l22.857-128h98.634l-22.857 128z',
                    onclick: function () {
                        localStorage.setItem('#trendBuildAxis', 'build');
                        redrawCallback();
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
            top: '15%',
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
            axisLabel: {
                color: textColor
            }
        }],
        series: chartModel.series
    };
    chart.setOption(options);
    chart.resize();

    jQuery3(window).resize(function () {
        chart.resize();
    });
}

// Make the API change backward compatible
renderZoomableTrendChart = echartsJenkinsApi.renderZoomableTrendChart;
