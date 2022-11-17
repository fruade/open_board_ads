var showFile = (function () {
    var fr = new FileReader,
        i = 0,
        files, file;

    fr.onload = function (e) {
        var li;


        if (file.type.match('image.*') && document.getElementById("fln").files.length < 7) {
            li = document.createElement('li');
            if (file.size > (5 * 1024 * 1024)) {
                li.innerHTML = "<div class='del-photos'><div style='width: 100px; height: 100px; class='card'><div class='alert-error card'>Размер фото превышает 5 мб</div></div><div class='del-photo-btn'><button class='delb' type='button'><i class='fa fa-trash-o'></i>Удалить</button></div></div>";
            } else {
                li.innerHTML = "<div class='del-photos'><img class='card' src='" + e.target.result + "' style='width: 100px; height: 100px;'><div class='del-photo-btn'><button class='delb' type='button'><i class='fa fa-trash-o'></i>Удалить</button></div></div>";
            }
            document.getElementById('list').appendChild(li);
        }
            file = files[++i];
            if (file) {
                fr.readAsDataURL(file)
            } else {
                i = 0;
            }
    }

    return function (e) {
        files = e.target.files;
        file = files[i];
        if (files) {
            while (i < files.length && !file.type.match('image.*')) {
                file = files[++i];
            }
            if (file) fr.readAsDataURL(files[i])
        }
    }
 
})()


$('#fln').on('change', function(){
    console.log()
});


$( document ).on('click', '.del-photo-btn', function() {
    $(this).parent().parent().remove();
    return false;
})


if (document.getElementById('fln')) {
    document.getElementById('fln').addEventListener('change', showFile, false);
}

