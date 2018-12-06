$(function() {
    $('#btnSignIn').click(function() {
 
        $.ajax({
            url: '/signIn',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                window.location = '/dashboard';
            },
            error: function(error) {
                console.log(error);
                window.location = '/errorSignIn';
            }
        });
    });
});