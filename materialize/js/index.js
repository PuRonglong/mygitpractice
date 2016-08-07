/*!
 * author: puronglong
 */

$(document).ready(function () {
	'use strict';
	$('.slider').slider({
		full_width: true,
		indicators: true,  // 导航标识
		interval: 7000,   // 间隔时间设置
		transition: 700    // 持续时间设置
	});

	$('.button-previous-left').on('click', function () {
		$('.slider').slider('prev');
	});

	$('.button-previous-right').on('click', function () {
		$('.slider').slider('next');
	});
});



