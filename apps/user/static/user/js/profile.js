let flag = false


$( document ).ready(function(){
    $('#menu-profile').click( function() {
        if(!flag) {
            $('#wrapper-profile').show()
            $('.menu-element').slideDown();
            
        } else {
            $('.menu-element').slideUp();
            $('#wrapper-profile').hide();
        }
        flag = !flag;
    })
    $( document ).mouseup( function(e) {
        if (flag) {
            $('.menu-element').slideUp();
            $('#wrapper-profile').hide();
            
        }
    })
    $(window).scroll(function() {
        if (flag) {
            $('.menu-element').slideUp();
            $('#wrapper-profile').hide();
        }
        
    });
    
})