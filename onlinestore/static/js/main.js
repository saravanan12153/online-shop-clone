var main = function(){
    $(".flash-message").fadeOut(4000);

    $("#loginlink").on("click", function(){
            $(".register").hide();
            $(".login").show();
        });

    $("#registerlink").on("click", function(){
            $(".register").show();
            $(".login").hide();
        });

    $('.modal-trigger').leanModal();
    $(".button-collapse").sideNav();
};

$(document).ready(main);
