var main = {
    init: function(){
        $(".flash-message").fadeOut(4000);

        $("#loginlink").on("click", function(){
                $(".register").hide();
                $(".login").show();
            });

        $("#registerlink").on("click", function(){
                $(".register").show();
                $(".login").hide();
            });
    }
}

// $(document).ready(main);
// if (window.location.href.indexOf('login') != -1) {
//     $(".register").hide();
//     $(".login").show();
// }

$(document).ready(function() {
    var url = window.location.href;
    $(function() {
        if ( url.indexOf('login') > -1) {
            $(".register").hide();
            $(".login").show();
        }
    });

    main.init();
});