$(function() {
    $('#btnSignIn').click(function() {
 
        $.ajax({
            url: '/signIn',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});