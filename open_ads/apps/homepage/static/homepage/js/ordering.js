$(document).on("click", "#order_c .nice-select .option:not(.disabled)", function (t) {
    let s = $(this),
    n = s.closest(".nice-select");
    value = s.data("value")


    const url = new URL(location);
    url.searchParams.delete('orderby');
    history.replaceState(null, null, url)
    console.log(url.href)
    if (window.location.search) {
        window.location.replace(url + '&orderby=' + value);
    } else {
        window.location.replace(url + '?orderby=' + value);
    }

})

let params = (new URL(document.location)).searchParams;
order_val = params.get("orderby");

if (order_val === 'price') {
    order_val = 'сначала дешевые';
} else if (order_val === '-price') {
    order_val = 'сначала дорогие';
} else if (order_val === '-date_add') {
    order_val = 'по умолчанию';
} else if (order_val === 'date_add') {
    order_val = 'по дате добавления';
}


if (order_val) {
    document.querySelector('#order_c .nice-select span').textContent = order_val
}
