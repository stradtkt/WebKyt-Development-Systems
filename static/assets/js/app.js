$(function() {
	var $window = $(window);
	$('section[data-type="background"]').each(function() {
		var $bgobj = $(this);
		$(window).scroll(function() {
			var yPos = -($window.scrollTop() / $bgobj.data('speed'));
			var coords = '50% ' + yPos + 'px';
			$bgobj.css({backgroundPosition: coords});
		});
	});
});

$(document).ready(function(){
    $("#testimonial-slider").owlCarousel({
        items:2,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,1],
        pagination:false,
        navigation:true,
        navigationText:["",""],
        autoPlay:true
    });
});
