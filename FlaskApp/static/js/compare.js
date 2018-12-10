$(function() {
    $('#btnCompare').click(function() {
 
        $.ajax({
            url: '/testCompare',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                window.location = '/compareFinished';
            },
            error: function(error) {
                console.log(error);
                window.location = '/compareError';
            }
        });
    });
});