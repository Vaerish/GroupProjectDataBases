$(function() {
    $('#btnSignUp').click(function() {
 
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                window.location = '/success';
            },
            error: function(error) {
                console.log(error);
                window.location = '/errorSignUp';
            }
        });
    });
});