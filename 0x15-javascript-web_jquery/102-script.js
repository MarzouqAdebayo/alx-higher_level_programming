$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    $.getJSON(url + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
