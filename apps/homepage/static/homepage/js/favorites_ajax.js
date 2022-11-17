function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

 const add_to_favorites_url = '/favorites/add/'
 const remove_from_favorites_url = '/favorites/remove/'
 const favorites_api_url = '/favorites/api/'
 const added_to_favorites_class = 'added'

 function add_to_favorites() {
    $('.add-to-favorites').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()

            const type = $(el).data('type')
            const id = $(el).data('id')

            if ( $(e.target).hasClass(added_to_favorites_class) ) {
                $.ajax({
                    url: remove_from_favorites_url,
                    headers: {'X-CSRFToken': csrftoken},
                    dataType: 'json',
                    type: 'POST',
                    data: {
                        type: type,
                        id: id,
                    },
                    success: (data) => {
                        $(el).removeClass(added_to_favorites_class)
                        $(el).parent().removeClass('fav-bc')
                        get_session_favorites_statistics()
                    }
                })
            } else {
                $.ajax({
                    url: add_to_favorites_url,
                    type: 'POST',
                    headers: {'X-CSRFToken': csrftoken},
                    dataType: 'json',
                    data: {
                        type: type,
                        id: id,
                    },
                    success: (data) => {
                        $(el).addClass(added_to_favorites_class)
                        $(el).parent().addClass('fav-bc')
                        get_session_favorites_statistics()
                    }
                })
            }
        })
    })
 }

 function get_session_favorites() {
    get_session_favorites_statistics()

    $.getJSON(favorites_api_url, (json) => {
        if (json !== null) {
            for (let i = 0; i < json.length; i ++) {
                $('.add-to-favorites').each((index, el) => {
                    const  type = $(el).data('type')
                    const id = $(el).data('id')

                    if ( json[i].type == type && json[i].id == id) {
                        $(el).addClass(added_to_favorites_class)
                        $(el).parent().addClass('fav-bc')
                    }
                })
            }
        }
    })
 }


 function get_session_favorites_statistics() {
    $.getJSON(favorites_api_url, (json) => {
        if (json !== null) {
            $('.favorites-statistics').empty()
            $('.favorites-statistics').append('(' + json.length + ')')
        }
        if (json == null) {
            $('.favorites-statistics').empty()
        }
    })
 }

 $(document).ready(function() {
    add_to_favorites()
    get_session_favorites()
 })