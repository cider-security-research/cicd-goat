/* global jQuery3, view, echartsJenkinsApi */
document.addEventListener('DOMContentLoaded', function () {
    redrawTrendCharts();
    storeAndRestoreCarousel('trend-carousel');

    /**
     * Redraws the trend charts. Reads the last selected X-Axis type from the browser local storage and
     * redraws the trend charts.
     */
    function redrawTrendCharts() {

        /**
         * Creates a build trend chart that shows the test duration across a number of builds.
         * Requires that a DOM <div> element exists with the ID '#test-duration-trend-chart'.
         */
        view.getTestDurationTrend(function (lineModel) {
            echartsJenkinsApi.renderZoomableTrendChart('test-duration-trend-chart', lineModel.responseJSON, redrawTrendCharts);
        });

        /**
         * Creates a build trend chart that shows the test results across a number of builds.
         * Requires that a DOM <div> element exists with the ID '#test-result-trend-chart'.
         */
        view.getTestResultTrend(function (lineModel) {
            echartsJenkinsApi.renderZoomableTrendChart('test-result-trend-chart', lineModel.responseJSON, redrawTrendCharts);
        });
    }

    /**
     * Store and restore the selected carousel image in browser's local storage.
     * Additionally, the trend chart is redrawn.
     *
     */
    function storeAndRestoreCarousel (carouselId) {
        const carousel = jQuery3('#' + carouselId);
        carousel.on('slid.bs.carousel', function (e) {
            localStorage.setItem(carouselId, e.to);
            const chart = jQuery3(e.relatedTarget).find('>:first-child')[0].echart;
            if (chart) {
                chart.resize();
            }
        });
        const activeCarousel = localStorage.getItem(carouselId);
        if (activeCarousel) {
            carousel.carousel(parseInt(activeCarousel));
        }
    }
})
