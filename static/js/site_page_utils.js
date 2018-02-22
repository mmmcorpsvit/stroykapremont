    // Init Isotope
    var $grid = $('.grid').isotope({
        // options
    });

    // filter items on button click
    $('.filter-button-group').on('click', 'button', function () {

        var filterValue = $(this).attr('data-filter');
        $grid.isotope({filter: filterValue});
        $(this).addClass('is-checked');
    });


    // change is-checked class on buttons
    $('.button-group').each(function (i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });


    // Custom click event - open fancyBox manually
    $('.fancybox').on('click', function () {
        var visibleLinks = $('.fancybox:visible');

        $.fancybox.open(visibleLinks, {}, visibleLinks.index(this));

        return false;
    });
    <!--portfoilo end-->


    $(document).ready(function (e) {
        $('#test').scrollToFixed();
        $('.res-nav_click').click(function () {
            $('.main-nav').slideToggle();
            return false

        });

    });


    wow = new WOW(
        {
            animateClass: 'animated',
            offset: 100
        }
    );
    wow.init();


    $(window).load(function () {

        $('.main-nav li a, .servicelink').bind('click', function (event) {
            var $anchor = $(this);

            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 102
            }, 1500, 'easeInOutExpo');
            /*
            if you don't want to use the easing effects:
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1000);
            */
            if ($(window).width() < 768) {
                $('.main-nav').hide();
            }
            event.preventDefault();
        });
    });


    $(window).load(function () {
        var $container = $('.portfolioContainer'),
            $body = $('body'),
            colW = 375,
            columns = null;


        $container.isotope({
            // disable window resizing
            resizable: true,
            masonry: {
                columnWidth: colW
            }
        });

        $(window).smartresize(function () {
            // check if columns has changed
            var currentColumns = Math.floor(($body.width() - 30) / colW);
            if (currentColumns !== columns) {
                // set new column count
                columns = currentColumns;
                // apply width to container manually, then trigger relayout
                $container.width(columns * colW)
                    .isotope('reLayout');
            }

        }).smartresize(); // trigger resize to set container width
        $('.portfolioFilter a').click(function () {
            $('.portfolioFilter .current').removeClass('current');
            $(this).addClass('current');

            var selector = $(this).attr('data-filter');
            $container.isotope({

                filter: selector,
            });
            return false;
        });

    });