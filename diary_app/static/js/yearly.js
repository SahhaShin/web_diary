
      
      $(document).ready(function () {
            $('nav a').on('click', function () {
                $(this).addClass('on');
                $(this).siblings().removeClass('on');

            });

        });


    