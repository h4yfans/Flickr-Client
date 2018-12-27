$(document).ready(function () {
    $('img').click(e => {
        let selectedImageURL = $(e.currentTarget).attr('src');

        $.ajax({
            url: '/post-like/',
            type: 'POST',
            dataType: 'json',
            data: {
                image_url: selectedImageURL,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function (data) {
                if (data.message) {
                    let heartNo = $(e.currentTarget).attr('id');
                    let heart = $('#heart-' + heartNo);
                    data.is_saved ? heart.addClass('liked-heart') : heart.removeClass('liked-heart')
                } else {
                    window.location.href = "/users/login"
                }
            }
        });
    });
});