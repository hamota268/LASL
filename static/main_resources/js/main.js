;(function () {
	
	'use strict';



	// iPad and iPod detection	
	var isiPad = function(){
		return (navigator.platform.indexOf("iPad") != -1);
	};

	var isiPhone = function(){
	    return (
			(navigator.platform.indexOf("iPhone") != -1) || 
			(navigator.platform.indexOf("iPod") != -1)
	    );
	};


	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};

	var burgerMenu = function() {

		$('.js-colorlib-nav-toggle').on('click', function(event) {
			event.preventDefault();
			var $this = $(this);
			if( $('body').hasClass('menu-show') ) {
				$('body').removeClass('menu-show');
				$('#colorlib-main-nav > .js-colorlib-nav-toggle').removeClass('show');
			} else {
				$('body').addClass('menu-show');
				setTimeout(function(){
					$('#colorlib-main-nav > .js-colorlib-nav-toggle').addClass('show');
				}, 900);
			}
		})
	};

	// Animations

	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated') ) {
				
				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn animated');
							} else {
								el.addClass('fadeInUp animated');
							}

							el.removeClass('item-animate');
						},  k * 200, 'easeInOutExpo' );
					});
					
				}, 100);
				
			}

		} , { offset: '85%' } );
	};


	var counter = function() {
		$('.js-counter').countTo({
			 formatter: function (value, options) {
	      return value.toFixed(options.decimals);
	    },
		});
	};

	var counterWayPoint = function() {
		if ($('#colorlib-counter').length > 0 ) {
			$('#colorlib-counter').waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {
					setTimeout( counter , 400);					
					$(this.element).addClass('animated');
				}
			} , { offset: '90%' } );
		}
	};

	// Owl Carousel
	var owlCarouselFeatureSlide = function() {
		var owl2 = $('.owl-carousel');
		owl2.owlCarousel({
		   animateOut: 'fadeOut',
		   animateIn: 'fadeIn',
		   autoplay: true,
		   autoplayTimeout: 4000, // Time between slides (in milliseconds)
		   autoplayHoverPause: true, // Pause on hover
		   loop:true,
		   margin:0,
		   nav: true,
		   dots: false,
		   autoHeight: true,
		   mouseDrag: false,
		   autoplayHoverPause: true,
		   items: 1,
		   navText: [
		      "<i class='icon-arrow-left3 owl-direction'></i>",
		      "<i class='icon-arrow-right3 owl-direction'></i>"
	     	]
		});
		var owl3 = $('.owl-carousel3');
		owl3.owlCarousel({
			animateOut: 'fadeOut',
			animateIn: 'fadeIn',
			autoplayTimeout: 4000, // Time between slides (in milliseconds)
			autoplayHoverPause: true, // Pause on hover
			autoplay: true, // Autoplay enabled
			loop: true, // Enable infinite looping
			margin: 0,
			nav: true, // Enable navigation arrows
			dots: true, // Enable dot navigation
			dotData: true, // Ensure dots are linked to slides
			autoHeight: true,
			mouseDrag: false, // Disable dragging with the mouse
			touchDrag: false, // Disable dragging on touch devices
			items: 1, // Display one item at a time
			navText: [
			    "<i class='icon-arrow-left3 owl-direction'></i>",
			    "<i class='icon-arrow-right3 owl-direction'></i>"
			] // Custom icons for navigation buttons

		   
		});	
		function updateBackgroundImage(event) {
			const currentIndex = event.item.index;
			const newBg = $(".owl-carousel3 .owl-item")
			    .eq(currentIndex)
			    .find(".item")
			    .data("bg");
			console.log("Updating background to:", newBg); // Debug log
			$(".about-img").css("background-image", `url(${newBg})`);
		  }
  }

	


	// Document on load.
	$(function(){
		fullHeight();
		burgerMenu();
		// counterWayPoint();
		contentWayPoint();
		owlCarouselFeatureSlide();
	});


}());