$(function() {
    $('#btnTest').click(function() {
 
        $.ajax({
            url: '/testResult',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                window.location = '/testFinished';
            },
            error: function(error) {
                console.log(error);
                window.location = '/errorTest';
            }
        });
    });
});